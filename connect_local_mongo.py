from pymongo import MongoClient
from config import *
from helper import *

client = MongoClient("mongodb://localhost:27017")

db = client.get_database(database_name)
# collection = db.get_collection(collection_name)

# collections_details=extract_db_details(db)
# database_details = db.command("dbstats")
# print(json.dumps(collections_details,indent=4))
# print(json.dumps(database_details,indent=4))






client.close()
