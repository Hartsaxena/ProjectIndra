# This ignores deprecation warnings when importing modules
import warnings
warnings.filterwarnings("ignore")

# This handles game imports

import subprocess
import sys
import time
from time import sleep

try:
    from datetime import *
    from pathlib import Path
    from time import ctime
    from time import strptime
    from word2number import w2n
    import calendar
    import git
    import json
    import os
    import PIL
    import platform
    import pyautogui as pag
    import random
    import requests
    import shutil
    import time
    if sys.version_info < (3, 0):
        import Tkinter as tk
    else:
        import tkinter as tk
        from tkinter import *
        from PIL import ImageTk,Image

# Installs all modules in case the user hasn't downloaded them already (which is very likely)
except ModuleNotFoundError:
    print ("")
    print ("Sorry, but it seems that there was a problem importing required modules.")
    sleep(2.5)
    print ("I can install the required modules if you like!")
    sleep(2)
    print("Would you like for me to help you install the packages?")
    yesno = input(" [Y / N] ")
    if yesno.lower() == 'y':
        print ("This might take a while, so please be patient.")
        sleep(2)

        install('pyobjc')
        install('pyobjc-core')
        install("requests")
        install('pillow')
        install('pyautogui')
        install('word2number')
        install("git-python")

        for i in range(1, 3):
            print ('\n')
        print ("Thank you for being patient and downloading the modules.")
        sleep(2)
        print ("The Program will now terminate.")
        sleep(2)
        print ("Please restart the program.")
        sleep(1.25)
        AbruptTerminate()

    elif yesno.lower() == 'n':
        print ("Sorry, but that means the program cannot run.")
        sleep(1)
        AbruptTerminate("ModuleNotFoundError")
