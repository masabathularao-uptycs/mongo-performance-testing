from config import *

client = connect(TAG)
db = client.get_database(database_name)
collection_names = db.list_collection_names()

# Iterate over each collection
for collection_name in collection_names:
    myColl = db[collection_name]
    print(collection_name)
    myColl.create_index([('event_time', 1)])
    myColl.create_index([('upt_table_key_value', 1), ('upt_table_key_name', 1), ('upt_table_name', 1)])
    myColl.create_index([('event_id', 1), ('upt_table_key_value', 1), ('upt_table_key_name', 1), ('upt_table_name', 1)])


client.close()
