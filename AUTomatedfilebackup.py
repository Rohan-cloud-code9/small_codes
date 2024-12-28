import os
import shutil
import datetime
import schedule
import time

Source = "C:/Users/Rohan/OneDrive/Pictures/Screenshots"
destination = "C:/Users/Rohan/OneDrive/Pictures/Saved Pictures"

def backup(source, desti):
    date = datetime.date.today()
    desti_dir = os.path.join(desti, str(date))
    try:
        shutil.copytree(source, desti_dir)
        print(f"Folder copied to : {desti_dir}")
    except FileExistsError:
        print(f"folde already exist in : {desti}")

backup(Source, destination)