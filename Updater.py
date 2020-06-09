# This is executed when the Player wishes to update the game
# Use this Program sparingly. Problems can happen.
# This only downloads the Filed version of the project, not the WIP app.


while topicdone == False:
    yesno = input(
        "Are you sure? doing this will update the game to the current\nversion (In the github page). This will also reset the game.\nIn order to save progress, make a copy of the 'save.json' file\nthat can be found in the Saves folder in the ProjectIndra folder.\n[y/n] ")
    if Yes(yesno) == True:
        print("Ok!")
        time.sleep(1)
        print("Warning! Don't terminate this program while this is being run.\nDoing so can and most likely will\ncause serious problems.")
        print("Removing old files...")
        if os.path.exists("Indra.py") == True:
            if os.path.isfile("Indra.py"):
                os.remove("Indra.py")
            elif os.path.isdir("Indra.py"):
                shutil.rmtree("Indra.py")  # Don't ask
        if os.path.exists(indrafolder) == True:
            shutil.rmtree(indrafolder)
        print("Downloading most recent version of Project Indra...")
        git.Git(Path.home() / "Documents").clone("https://github.com/Hartsaxena/ProjectIndra.git")
        url = 'https://raw.githubusercontent.com/Hartsaxena/Project-Indra/master/Indra.py'
        r = requests.get(url, allow_redirects=True)
        open("Indra.py", 'wb').write(r.content)
        print("Done!")
        sleep(1)
        print("This program will terminate in")
        sleep(2)
        print("3")
        sleep(1)
        print("2")
        sleep(1)
        print("1")
        sleep(1)
        AbruptTerminate()
    elif No(yesno) == True:
        print("Ok!")
        sleep(1)
        print("Thank you for reconsidering.")
        sleep(2)
        print("To be honest, the updater isn't close to perfect and can cause serious problems.")
        sleep(3)
        print("The creator is still working on it!")
        sleep(2)
        topicdone = True
    elif not yesno:
        topicdone = False
        if rep == 0:
            print("...")
            sleep(2)
            print(name + "...")
            sleep(2)
            print("You're supposed to say yes or no!")
            sleep(2)
            if negloveBonus == 3 or interest <= 60:
                print("Idiot.")
            else:
                print("You can be so silly sometimes.")
            sleep(2)
        elif rep == 1:
            print("...")
            sleep(2)
            print("I'm not sure you understand.")
            sleep(2)
            print("Read the clarification, and then answer yes or no depending\non whether or not you want to update the game to the most current version\nthrough the Github page.")
            sleep(4)
            print("c:")
            sleep(1)
        elif rep == 2:
            print("Ok.")
            sleep(1)
            print("It is clear to me that you don't quite get what is happening.")
            sleep(3)
            print("When a big paragraph comes up and you are asked to answer y or n,")
            sleep(2.75)
            print("Just answer n.")
        elif rep == 3:
            if interest >= 150 or loveBonus == 3:
                print("Oh.")
                sleep(1)
                print("Now i get it.")
                sleep(1)
                print("You're just goofing around!")
                sleep(2)
                print("No worries, I understand.")
                if loveBonus == 3:
                    print("I love you, " + name + ".")
                else:
                    print("Have a good day!")
                sleep(2)
            else:
                print("You're joking, right?")
                sleep(2)
                print("There can't possibly be someone as stupid as that.")
                sleep(2)
        elif rep == 50:
            print("You really don't have a life, do you?")
            sleep(2)
            IndraTerminate()
        else:
            print("Please answer with either yes or no.")
        rep = rep + 1
    else:
        print("Sorry, but I don't know exactly what you just said.")
        sleep(2)
        print("Please answer with either yes or no.")
        sleep(2)
        topicdone = False
