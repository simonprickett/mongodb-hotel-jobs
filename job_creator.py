import os
import random
import time

from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

JOB_TYPES = [
    "cleaning",
    "room_service",
    "taxi",
    "extra_towels",
    "extra_pillows"
]

# Load environment variables / secrets from .env file.
load_dotenv()

client = MongoClient(os.environ["MONGODB_URI"], server_api=ServerApi('1'))
database = client[os.environ["MONGODB_DATABASE"]]
collection = database[os.environ["MONGODB_COLLECTION"]]

while True:
    job = {
        "room": random.randint(100, 500),
        "job": random.choice(JOB_TYPES),
        "requestedAt": int(time.time() * 1000)
    }

    response = collection.insert_one(job)
    
    print(f"Inserted {response.inserted_id}:")
    print(job)
    
    print("Sleeping until the next job comes in...")
    time.sleep(random.randint(5, 10))
