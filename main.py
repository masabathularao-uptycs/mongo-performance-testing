from config import *
import time
import concurrent.futures
start_time = time.time()

client = connect(TAG)
db = client.get_database(database_name)
collection_names = list(db.list_collection_names())


variables_list= [(db[collection_name],collection_name) for collection_name in collection_names]
with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = [executor.submit(start_upsertion, *variables) for variables in variables_list]
    concurrent.futures.wait(futures)

# for collection_name in collection_names:
#     collection = db[collection_name]
#     start_upsertion(collection,collection_name)



client.close()
end_time = time.time()
execution_time = end_time - start_time

print("TOTAL TIME TAKEN : " , execution_time)