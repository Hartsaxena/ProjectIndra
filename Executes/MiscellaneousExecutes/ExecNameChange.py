# This is executed when the player tells Indra to change his/her name (The player)


while topicdone == False:
    namechange = input("Oh! Would you like to change your name? ")
    if namechange.lower() == 'yes' or namechange.lower() == 'yep' or namechange.lower() == 'y':
        print("Ok!")
        sleep(1)
        changer = input('What would you like to change your name into?\nJust type in "Nevermind" if you change your mind! ')
        if changer.lower()=='nevermind':
            print ("Ok!")
            sleep(1.5)
            print ("If you ever want to change your name, just ask me, ok?")
            sleep(2.75)
        else:
            name = changer
            print("...")
            sleep(2)
            print("Ok!")
            sleep(1.5)
            print("From now on, I'll call you "+name+"!")
            sleep(2)
        topicdone = True

    elif namechange.lower() == 'no' or namechange.lower() == 'nope' or namechange.lower() == 'not really' or namechange.lower() == 'n':
        print("Ok!")
        sleep(1.5)
        print("If you ever want to change your name, just ask me, ok?")
        sleep(2.75)
        topicdone = True

    else:
        print ("Sorry! I don't know about too many ways to say yes or no...")
        sleep(2.75)
        print ("I hope you understand...")
        sleep(2)
        topicdone = False
