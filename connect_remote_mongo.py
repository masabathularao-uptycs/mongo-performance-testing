from pymongo import MongoClient
from config import *

mongo_uri = f"mongodb://root:rootpassword@{node}:30001/{database_name}?authSource=admin&w=1"

# Create a MongoClient instance with TLS settings
client = MongoClient(
    mongo_uri,
    tls=True,
    tlsCAFile="ca.crt",  # Specify the path to the CA certificate file
    tlsAllowInvalidHostnames=True
)

db = client.get_database()
collection = db.get_collection(collection_name)

document = {
    "key": "value",
    "another_key": "another_value"
}

result = collection.insert_one(document)
print("Inserted document ID:", result.inserted_id)

client.close()
