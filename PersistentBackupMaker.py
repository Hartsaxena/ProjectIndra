# This script is used to create backups of Monika After Story's Persistent file
# Just run the script and you should find it in the Persistent Backups Folder!


import os
import shutil
from pathlib import Path

print("Attempting to create backup for Persistent file...")
try:
    os.makedirs(Path.home() / "Desktop/Persistent Backups", exist_ok=True)
    persistent = open(
        Path.home() / "Desktop/Persistent Backups/Monika After Story/persistent", 'w')
    persistent.close()
    shutil.copy2(Path.home() / "Library/RenPy/Monika After Story/persistent",
                 Path.home() / "Desktop/Persistent Backups/Monika After Story")
    print("Finished!")
except:
    print("Sorry! Something went wrong and the Program wasn't able to create a backup for the Persistent File.")
