from pymongo import MongoClient
from dotenv import load_dotenv
import os 
from pathlib import Path

env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(env_path)

mongodb_uri = os.getenv("MONGODB_URI")
db_name = os.getenv("DB_NAME")


client = MongoClient(mongodb_uri)
db = client[db_name]
video_collection=db["videos"]

print(video_collection)