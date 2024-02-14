from pymongo import MongoClient
from config import *
from helper import *
import json
# from create_collections import create_collections

client = MongoClient("mongodb://localhost:27017")

db = client.get_database(database_name)
# create_collections(db)
# collection = db.get_collection(collection_name)

# collections_details=extract_db_details(db)
# database_details = db.command("dbstats")
# print(json.dumps(collections_details,indent=4))
# print(json.dumps(database_details,indent=4))

collection_names = list(db.list_collection_names())

for collection_name in collection_names:
    collection = db[collection_name]
    start_upsertion(collection,collection_name)



client.close()
