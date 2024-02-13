from pymongo import MongoClient
from config import *

client = MongoClient("mongodb://localhost:27017")

db = client.get_database(database_name)
# collection = db.get_collection(collection_name)

collection_names = db.list_collection_names()

# Iterate over each collection
for collection_name in collection_names:
    collection = db[collection_name]
    count = collection.count_documents({})
    print(f"{collection} : {count}")
    if count == 0:
        db.drop_collection(collection_name)

client.close()
