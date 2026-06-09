import sqlite3

conn = sqlite3.connect('youtube_videos.db')

cursor = conn.cursor()

cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS videos(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        time TEXT NOT NULL,
    )
''')

def list_videos():
    pass

def add_video(name, time):
    pass

def update_video(video_id, name, time):
    pass

def delete_video(video_id):
    pass

def main():
    while True:
        print("\n Youtube manager app with DB")
        print("1. List videos")
        print("2. Add Videos")
        print("3. Update Videos")
        print("4. Delete Videos")
        print("5. exit app")
        choice = input("Enter your choice: ")

        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter the video name: ")
            time = input("Enter the video time ")
            add_video(name, time)
        elif choice == '3':
            video_id = int(input("Enter video Id to update: "))
            name = input("Enter the video name: ")
            time = input("Enter the video time ")
            update_video(video_id, name, time)
        elif choice == '4':
            video_id = int(input("Enter video Id to delete: "))
            delete_video(video_id)
        elif choice == '5':
            break
        else:
            print("Invalid Choice ")

if __name__ == "__main__":
    main()