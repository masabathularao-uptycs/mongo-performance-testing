from pymongo import MongoClient
from config import *
import json
from helper import *

client = MongoClient("mongodb://localhost:27017")

db = client.get_database(database_name)
# collection = db.get_collection(collection_name)
collection_details=extract_db_details(db)

print(json.dumps(collection_details,indent=4))
print(db.command("dbstats"))
client.close()
