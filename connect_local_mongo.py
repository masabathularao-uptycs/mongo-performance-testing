from pymongo import MongoClient
from config import *
from helper import *
import json,time
import concurrent.futures
start_time = time.time()

client = MongoClient("mongodb://localhost:27017")

db = client.get_database(database_name)
collection_names = list(db.list_collection_names())

# collections_details=extract_db_details(db)
# database_details = db.command("dbstats")
# print(json.dumps(collections_details,indent=4))
# print(json.dumps(database_details,indent=4))


# variables_list= [(db[collection_name],collection_name) for collection_name in collection_names]
# with concurrent.futures.ThreadPoolExecutor() as executor:
#     futures = [executor.submit(start_upsertion, *variables) for variables in variables_list]
#     concurrent.futures.wait(futures)

for collection_name in collection_names:
    collection = db[collection_name]
    start_upsertion(collection,collection_name)



client.close()
end_time = time.time()
execution_time = end_time - start_time

print("TOTAL TIME TAKEN : " , execution_time)