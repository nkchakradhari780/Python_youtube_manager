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
video_collection = db["videos"]

print(video_collection)

def list_all_videos():
    for video in video_collection.find():
        print(f"ID: {video['_id']}, Name: {video['name']}, and Time: {video['time']}")

def delete_video(video_id):
    video_collection.delete_one({"_id": video_id})

def update_video(video_id, name, time):
    video_collection.update_one(
        {"_id": video_id},
        {"$set": {"name": name, "time": time}}
    )

def add_video(name, time):
    video_collection.insert_one({"name": name, "time": time})

def main():
    while True:
        print("\n Youtube manager App")
        print("1. List all videos.")
        print("2. Add New video")
        print("3. Update video")
        print("4. Delete video")
        print("5. Exit the app")
        choice = input("Enter your choice: ")

        match choice:
            case '1':
                list_all_videos()
            case '2':
                name = input("Enter the video name: ")
                time = input("Enter the video time: ")
                add_video(name, time)
            case '3':
                video_id = input("Enter the video id to update: ")
                name = input("Enter the New video name: ")
                time = input("Enter the New video time: ")
                update_video(video_id, name, time)
            case '4':
                video_id = input("Enter the video id to delete: ")
                delete_video(video_id)
            case '5':
                break
            case _:
                print("Invalid choice")

if __name__ == "__main__":
    main()