from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os
import random
import time

# Load environment variables / secrets from .env file.
load_dotenv()

client = MongoClient(os.environ["MONGODB_URI"], server_api=ServerApi('1'))
database = client[os.environ["MONGODB_DATABASE"]]
collection = database[os.environ["MONGODB_COLLECTION"]]

while True:
    print("Checking for a job that needs doing...")
    result = collection.find({ "completedAt": { "$exists": False } }).sort({ "requestedAt": 1 }).limit(1)

    found_job = False

    for job in result:
        found_job = True
        print("Retrieved job:")
        print(job)

        print("Performing job...")
        time.sleep(random.randint(10, 20))
        r = collection.update_one({ "_id": job["_id"] }, { "$set": { "completedAt": int(time.time() * 1000), "completedBy": random.randint(1, 5)} })

        print("Completed job.")

    if not found_job:
        print("No outstanding jobs to do right now!")

    print("Sleeping...")
    time.sleep(random.randint(10, 15))
