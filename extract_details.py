from config import *
import json

def extract_db_details(db):
    collection_names = db.list_collection_names()
    collection_details={}

    # Iterate over each collection
    for collection_name in collection_names:
        collection = db[collection_name]
        indexes = collection.list_indexes()
        indexes_dict={}
        for index in indexes:
            indexes_dict[index['name']] = list(index['key'].keys())
        # count = collection.count_documents({})   
        # print(f"{collection.name} : {count}")
        collection_stats= db.command("collstats", collection_name) 
        stats_dict={}
        stats_dict["collection_name"] = collection_stats['ns']
        stats_dict["uncompressed_data_size"] = collection_stats['size']
        stats_dict["count"] = collection_stats['count']
        stats_dict["storage_size_on_disk"] = collection_stats['storageSize']
        try:stats_dict["avg_obj_size"] = collection_stats['avgObjSize']
        except:pass
        stats_dict["num_indexes"] = collection_stats['nindexes']
        stats_dict["total_index_size_on_disk"] = collection_stats['totalIndexSize']
        stats_dict["each_index_sizes"] = collection_stats['indexSizes']
        stats_dict["total_collection_size_on_disk"] = collection_stats['totalSize']

        stats_dict["indexes"]=indexes_dict
        collection_details[collection_name] = stats_dict
    return collection_details

client = connect(TAG)
db = client.get_database(database_name)
collection_names = list(db.list_collection_names())

# collections_details=extract_db_details(db)
database_details = db.command("dbstats")
# print(json.dumps(collections_details,indent=4))
print(database_details)

# print(json.dumps(database_details,indent=4))