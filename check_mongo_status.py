from config import *

def check_mongo_nodes_health(client):
    # healthy_nodes = []
    # unhealthy_nodes = []

    # mongo_nodes = secondary_nodes[:]
    # mongo_nodes.append(remote_node)

    # for node in mongo_nodes:
    #     try:

    #         # Run serverStatus command to check node health
    #         server_status = client.admin.command('serverStatus')

    #         # Check if the node is reachable and its status
    #         if server_status['ok'] == 1:
    #             healthy_nodes.append(node)
    #         else:
    #             unhealthy_nodes.append(node)
    #     except Exception as e:
    #         unhealthy_nodes.append((node, str(e)))
        
    # print("Healthy Nodes:")
    # for node in healthy_nodes:
    #     print(node)

    # print("\nUnhealthy Nodes:")
    # for node, error in unhealthy_nodes:
    #     print(f"{node}: {error}")

    print("MONGO CLUSTER STATUS : ")

    repl_status = client.admin.command('replSetGetStatus')["members"]
    for member in repl_status:
        print("name " , member["name"])
        print("stateStr " , member["stateStr"])
        print("health " , member["health"])
        print("state " , member["state"])
        print("------------------")


