from config import *
import csv
import time
from datetime import datetime
import pytz


client = connect(TAG)
db = client.get_database(database_name)

start_time = time.time()


ist = pytz.timezone('Asia/Kolkata')
file_path = f"csv/{datetime.now(ist).strftime('%Y-%m-%d %H:%M')}_num_docs.csv"


with open(file_path, mode='a', newline='') as file:
    writer = csv.writer(file)
    while True:
        objects = int(db.command("dbstats")["objects"])
        if objects==0:continue
        curr_time = time.time()
        time_taken_till_now = curr_time - start_time
        ist_now = datetime.now(ist)
        ist_now_str = ist_now.strftime("%Y-%m-%d %H:%M")
        new_row = [ist_now_str,time_taken_till_now,objects]
        writer.writerow(new_row)
        file.flush()