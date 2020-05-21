# This is executed when the Player asks Indra to delete recorded logs through the topics "Reset" or "Clear Data"
ignoreinteract = True
topicdone = False
while topicdone == False:
    print("Are you sure? doing this will delete all recorded data\nthat this Program has created thus far.")
    sleep(2)
    print ("This will also effectively factory reset the game.")
    yesno = input("Yes or No? ")
    if Yes(yesno) == True:
        print("Deleting Logs Directory...")
        try:
            shutil.rmtree(indrafolder / "Logs")
            os.makedirs(indrafolder / "Logs")
            if os.path.exists(indrafolder / "Hello! I'm Indra!") == True:
                print("Deleting imindra Folder...")
                shutil.rmtree(indrafolder / "Hello! I'm Indra!")
            if os.path.exists(indrafolder / "You're_ok.txt") == True:
                print("Deleting opinion text...")
                os.remove(indrafolder / "you're_ok.txt")
            if os.path.exists(indrafolder / "Love_you.txt") == True:
                print("Deleting opinion text...")
                os.remove(indrafolder / "Love_you.txt")
            if os.path.exists(indrafolder / "Don't_Love_You.txt") == True:
                print("Deleting opinion text...")
                os.remove(indrafolder / "Don't_Love_You.txt")
            if os.path.exists(saves / "save.json") == True:
                print("Deleting Save file...")
                shutil.rmtree(saves)
                os.makedirs(indrafolder / "Saves")
            if os.path.exists(indrafolder/"Monika's_Room") == True:
                shutil.rmtree(indrafolder/"Monika's_Room")
            exec(open(misc / "RandomText.py").read())
            print("Finished!")
            sleep(2)
            print ("")
            print("This program will terminate in")
            print("3...")
            sleep(1)
            print("2...")
            sleep(1)
            print("1...")
            sleep(1)
        except:
            print("Sorry! Something went wrong and I am not able to delete the ProjectIndra files")
            sleep(2)
        sys.exit()
    if No(yesno) == True:
        print("Thank you for reconsidering.")
        sleep(1.75)
        topicdone = True
    else:
        print("Sorry, " + name + ", but I don't understand what you just said")
        sleep(2)
        topicdone = False
