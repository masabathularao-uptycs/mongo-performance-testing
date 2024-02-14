from pymongo import UpdateOne, MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["your_database_name"]
collection = db["your_collection_name"]

# Define a list of update operations using UpdateOneModel
update_operations = [
    UpdateOne({"_id": 5}, {"$set": {"field1": "value10000"}},upsert=True),
    UpdateOne({"_id": 6}, {"$set": {"field2": "value200"}},upsert=True),
]

result = collection.bulk_write(update_operations)

print("Modified count:", result.modified_count)
print("Inserted count:", result.upserted_count)

