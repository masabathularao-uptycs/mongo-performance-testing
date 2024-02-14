from pymongo import MongoClient
from config import *
import json
client = MongoClient("mongodb://localhost:27017")

db = client.get_database(database_name)
# collection = db.get_collection(collection_name)
largest_size = 0
largest_doc = None
largest_collection = None

collection_names = db.list_collection_names()

# Iterate over each collection
for collection_name in collection_names:
    collection = db[collection_name]
    for document in collection.find():
        # Calculate the size of the document
        document_size = len(str(document))
        # Compare the document size with the current largest size
        if document_size > largest_size:
            print(largest_size)
            largest_size = document_size
            largest_doc = document
            largest_collection = collection_name

# Print the result
if largest_doc:
    print(f"Largest document found in collection '{largest_collection}':")
    print(largest_doc)
    print(largest_size)
else:
    print("No documents found in any collection.")

client.close()
