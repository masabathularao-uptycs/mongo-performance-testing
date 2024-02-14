from pymongo import UpdateOne, MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["your_database_name"]
collection = db["your_collection_name"]

# Define a list of update operations using UpdateOneModel
update_operations = [
    UpdateOne({"_id": 1}, {"$set": {"field1": "value1"}}),
    UpdateOne({"_id": 2}, {"$set": {"field2": "value2"}}),
    # Add more UpdateOneModel instances as needed
]

# Perform bulk write operation
result = collection.bulk_write(update_operations)

# Print result
print("Modified count:", result.modified_count)
