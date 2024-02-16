def generate_dictionary(kilobytes):
    print("kilobytes : ",kilobytes)
    # Calculate the number of bytes
    bytes_count = kilobytes * 1024
    
    # Each key-value pair in the dictionary will be a string of length 100 bytes
    key_value_size = 100
    
    # Calculate the number of key-value pairs needed to fill the specified size
    num_pairs = bytes_count // key_value_size

    # Create a dictionary with key-value pairs of a fixed size
    dictionary = {str(i): 'a' * (key_value_size - len(str(i))) for i in range(num_pairs)}

    return dictionary

# from config import *

# client = MongoClient("mongodb://localhost:27017")# db = client.get_database(database_name)
# db=client["database"]
# coll = db["collection"]
# coll.insert_one(generate_dictionary(0))