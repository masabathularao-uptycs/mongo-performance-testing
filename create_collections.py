from config import *

def create_collections(db):
    num = len(db.list_collection_names())
    print("Current no. of collections : " , num)
    if num < TOTAL_COLLECTIONS:
        for i in range(TOTAL_COLLECTIONS-num):
            print(i)
            collection_name = f"collection_{str(uuid.uuid4())}"
            db.create_collection(collection_name)

from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client.get_database(database_name)
create_collections(db)