# This detects if the current Operating system is macOS

if platform.system() != "Darwin":
    print ("Warning! It seems you aren't running this on a macOS system!")
    sleep(2)
    print ("This program will most definitely fail if it is not run on a Mac.")
    sleep(2.5)
    print ("I apologize for the inconvenience.")
    AbruptRestart()

# This detects if a previous save exists

if os.path.exists(indrafolder / "firstrun") == True:
    firstrun = True
    print("Hello!")
    sleep(2)
    print("I'm Your Friendly Conversation Program!")
    sleep(2)
    print("my name is Indra!")
    sleep(2)
    name = input("what is your name? ")
    exec(open(vitals / "NameEggs.py").read())
    StartEdit()
    Save()
    os.remove(indrafolder / "firstrun")
if firstrun == False:
    try:
        Load()
    except IndexError:
        print(
            "Sorry, something went wrong and I wasn't able to load data from the save file.")
        sleep(1.75)
        resetconfirm = input("Would you like me to reset the game? ")
        if resetconfirm.lower() == 'yes' or resetconfirm.lower() == 'yes please' or resetconfirm.lower() == 'y':
            exec(open(sysexecutes / "ExecLogDel.py").read())
        elif resetconfirm.lower() == 'no' or resetconfirm.lower() == 'not really' or resetconfirm.lower() == 'n':
            sys.exit("Sorry, but the game cannot run and has been Terminated.")
    print("Welcome back, " + name + ".")
    sleep(1.5)
