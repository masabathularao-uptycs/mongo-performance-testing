from config import *

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


client = connect(TAG)
db = client.get_database(database_name)
create_collections(db)