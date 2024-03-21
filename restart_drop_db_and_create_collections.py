from config import *
from time import sleep
import socket,paramiko

def create_collections(db):
    num = len(db.list_collection_names())
    print("Current no. of collections : " , num)
    if num < TOTAL_COLLECTIONS:
        for i in range(TOTAL_COLLECTIONS-num):
            print(i)
            collection_name = f"aws_{str(uuid.uuid4())}_cloudaudit"
            myColl=db.create_collection(collection_name)
            print(collection_name)
            myColl.create_index([('event_time', 1)])
            myColl.create_index([('upt_table_key_value', 1), ('upt_table_key_name', 1), ('upt_table_name', 1)])
            myColl.create_index([('event_id', 1), ('upt_table_key_value', 1), ('upt_table_key_name', 1), ('upt_table_name', 1)])


def execute_command_in_node(node,command):
    try:
        print(f"Executing the command in node : {node}")
        client = paramiko.SSHClient()
        client.load_system_host_keys() 
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            client.connect(node,"22", "abacus", "abacus")
            stdin, stdout, stderr = client.exec_command(command)
            out = stdout.read().decode('utf-8').strip()
            errors = stderr.read().decode('utf-8')
            if errors:
                print("Errors:")
                print(errors)
            return out
                
        except Exception as e:
            raise RuntimeError(f"ERROR : Unable to connect to {node} , {e}") from e
        finally:
            client.close()
    except socket.gaierror as e:
        raise RuntimeError(f"ERROR : Unable to connect to {node} , {e}") from e

def restart_nodes():
    command = "sudo docker restart mongo"
    execute_command_in_node(remote_node,command)
    for node in secondary_nodes:
        execute_command_in_node(node,command)

client = connect(TAG)
client.drop_database(database_name)
restart_nodes()
# sleep(60)
db = client.get_database(database_name)
create_collections(db)