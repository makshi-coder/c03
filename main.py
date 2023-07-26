import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/hp/Downloads"
to_dir = "C:/Users/hp/Downloads/PRO-C103-Student-Boilerplate-main/PRO-C103-Student-Boilerplate-main/myfolder"


dir_tree = {
    "Image_Files": ['.jpg', '.JPEG', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

# Event Hanlder Class

class FileMovementHandler(FileSystemEventHandler):

    def on_created(self, event):
        name, extension = os.path.splitext(event.src_path)
        for key,value in dir_tree.items():
            time.sleep(1)
            if extension in value:
                time.sleep(1)
                file_name=os .path.basename(event.src_path)
                print("downloaded "+file_name)
                path1 = from_dir + '/' + file_name 
                path2 = to_dir + '/' + key 
                path3 = to_dir + '/' + key + '/' + file_name
                if os.path.exists(path2):

                    print("moving")
                    shutil.move(path1,path3)
                    
                     
                else:

                    os.makedirs(path2)
                    print("moving")
                    shutil.move(path1,path3)
        
               
                   
        print(event)
        print(event.src_path)


# Initialize Event Handler Class
event_handler = FileMovementHandler()


# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)


# Start the Observer
observer.start()


while True:
    time.sleep(2)
    print("running...")

    