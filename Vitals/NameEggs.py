# These Manage the Game's Naming Easter Eggs
# name or name.lower() is the name that is asked of you when you start the Main Program
if name.lower() == 'indra':
    print("Isn't that interesting...")
    sleep(2)
    print("We have the same name...")
    sleep(2)
elif name.lower() == 'james' or name.lower() == 'hartsaxena':
    print("Welcome back, James.")
    sleep(1.75)
elif name.lower() == 'guido rossum' or name.lower() == 'guido van rossum':
    print("You know, a person with that same name invented Python!")
    sleep(2)
elif name.lower() == 'scott cawthon':
    print("it's you...")
    sleep(1.5)
    print("Or should I say it's me...")
    sleep(1)

elif name.lower() == 'sans':
    print("nope.")
    sleep(1)
    namereject = True  # See Reset.py

elif name.lower() == 'monika':
    print("_J̷̩̍u̶͇͂s̵͚̽t̸͈̕ M̷̪̃ŏ̷͖n̸͕̂i̷̦͝k̵͍̕a̵̛̱_")

elif name.lower() == 'gaster':
    AbruptRestart()  # This Restarts the Game

elif name.lower() == 'dwight schrute':
    print("I wonder...")
    sleep(2)
    print("Sorry, I just thought I knew you from somewhere")
    sleep(2)

elif name.lower() == 'matpat':
    print("But that's just a Theory.")
    sleep(0.5)
    print("A ga-")
    sleep(0.5)
    namereject = True

elif name.lower() == 'baldi':
    print("Congratulations!")
    sleep(1)
    print("You found all Seven Notebooks!")
    sleep(1.25)
    print("Now all you have to do is...")
    namereject = True
else:
    print("Hello, "+name+"! Pleasure to meet you!")
    sleep(2)
    # if name.lower()==''

    # Executes if namereject is True and records it in the logs
if namereject == True:
    a = open(intlog, "a+")
    a.write('Name Rejected: '+name+"   Time: "+ctime())
    a.close()
    sys.exit()
