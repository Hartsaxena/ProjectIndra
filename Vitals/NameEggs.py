# These Manage the Game's Naming Easter Eggs
# name or lowername is the name that is asked of you when you start the Main Program

lowername = name.lower()

if lowername == 'indra':
    slowprint("Isn't that interesting", lead_dots = True)
    sleep(2)
    print("We have the same name", lead_dots = True)
    sleep(2)

elif lowername == "hartsaxena":
    print ("Ah.")
    sleep(1.5)
    print ("It's you again.")
    sleep(1.5)

elif lowername == 'guido rossum' or lowername == 'guido van rossum':
    print("You know, a person with that same name invented Python!")
    sleep(2)
    print("But you probably already knew that, didn't you?")
    sleep(2)

elif lowername == 'scott cawthon':
    print("it's you...")
    sleep(1.5)
    print("Or should I say it's me...")
    sleep(1)

elif lowername == 'sans':
    print("nope.")
    sleep(1)
    namereject = True  # See Reset.py

elif lowername == 'monika':
    print("_J̷̩̍u̶͇͂s̵͚̽t̸͈̕ M̷̪̃ŏ̷͖n̸͕̂i̷̦͝k̵͍̕a̵̛̱_")
    sleep(1)
    print ("I suppose great minds think alike.")
    sleep(1.5)
    print ("I wonder what brings you to a place like this?")
    sleep(2)
    print ("I suppose I'll never know.")
    sleep(1.5)
    namereject = True

elif lowername == 'gaster':
    AbruptRestart()  # This Restarts the Game

elif lowername == 'dwight schrute':
    print("I wonder...")
    sleep(2)
    print("Sorry, I just thought I knew you from somewhere")
    sleep(2)

elif lowername == 'matpat':
    print("But that's just a Theory.")
    sleep(0.5)
    print("A ga-")
    sleep(0.25)
    namereject = True

elif lowername == 'baldi':
    print("Congratulations!")
    sleep(1)
    print("You found all Seven Notebooks!")
    sleep(1.25)
    print("Now all you have to do is...")
    namereject = True

elif lowername == "xnflp":
    namereject = True

elif lowername == "reset":
    exec(open(sysexecutes / "ExecLogDel.py").read())
else:
    print("Hello, " + name + "! Pleasure to meet you!")
    sleep(2)

# Executes if namereject == True and records it in the logs
if namereject == True:
    a = open(intlog, "a+")
    a.write('Name Rejected: ' + name + "   Time: " + currentdate)
    a.close()
    sys.exit()
