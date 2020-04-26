# This is executed when "Virus" is the chosen subject


print("Of course not!")
sleep(1.25)
print("I would never try and sabotage your computer!")
sleep(2)
print('If you want to make sure, you can even check the files under the "Vitals" Folder if you like! ')
sleep(3)
print("I could add a little something to the Project Folder if you would like though...")
sleep(3)
while topicdone == False:
    alittlesomething = input(
        "Well? What do you say I add something to the Game Folder to spice things up a bit? ")
    if alittlesomething.lower() == 'yes' or alittlesomething.lower() == 'sure':
        print("Here we go!")
        exec(open(indrafolder/"Misc/FakeVirus.py").read())
        topicdone = True
    elif alittlesomething.lower() == 'no' or alittlesomething.lower() == 'nope' or alittlesomething.lower() == 'not really':
        if interest <= 50:
            print("Party Pooper...")
        else:
            print("Yeah... I guess we don't want to take any chances...")
        sleep(1.75)
        topicdone = True
    else:
        print("Sorry, "+name+", but I'm not sure I understand what you just said")
        sleep(2)
        topicdone = False
