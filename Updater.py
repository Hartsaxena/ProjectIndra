import git
import time
import shutil
import os
import os.path
from pathlib import Path
yesno = input("Are you sure? doing this will update the game to the current\nversion (In the github page). This will also reset the game.\nIn order to save progress, make a copy of the 'saves' file\nthat can be found in the Saves folder in the ProjectIndra folder.\n[y/n] ")
if yesno.lower() == 'yes' or yesno.lower() == 'y' or yesno.lower() == 'yep':
    print("Ok!")
    time.sleep(1)
    print("Warning! Don't terminate this program while this is being run.\nDoing so can and most likely will\ncause serious problems.")
    print("Checking if a Download folder currently exists...")
    if os.path.exists(Path.home()/"Downloads/Project-Indra"):
        shutil.rmtree(Path.home()/"Downloads/Project-Indra")
    print("Downloading most recent version of Project Indra...")
    git.Git(Path.home()/"Downloads").clone("https://github.com/Hartsaxena/Project-Indra.git")
    print("Removing old files...")
    indrafolder = Path(Path.home()/"Documents/ProjectIndra")
    shutil.rmtree(indrafolder/"Executes")
    shutil.rmtree(indrafolder/"Images")
    shutil.rmtree(indrafolder/"Misc")
    shutil.rmtree(indrafolder/"Vitals")
    os.remove(indrafolder/"DownloadGuide.txt")
    os.remove(indrafolder/"Sunlight.txt")
    os.remove(Path.home()/"Documents/Indra.py")
    print("Moving files...")
    original = Path(Path.home()/"Downloads/Project-Indra/ProjectIndra/")
    target = Path(Path.home()/"Documents/ProjectIndra")
    original1 = Path(Path.home()/"Downloads/Project-Indra/Indra.py")
    target1 = Path(Path.home()/"Documents")
    shutil.move(original.absolute(), target.absolute())
    shutil.move(original1.absolute(), target1.absolute())
    print ("Done!")
