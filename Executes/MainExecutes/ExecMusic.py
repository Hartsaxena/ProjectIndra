# This is Executed when "Music" or "Songs" is the chosen topic
# There's no way I'm going to repeat what happened in ExecVideoGames.py
# TODO: Complete This

print(f"Do you like listening to music, {name}?")
sleep(2)
print("Personally, I just love music!")
sleep(1.5)
print("They do such a good job of expressing the creator's emotions!")
sleep(2)
print("It's hard to put the meaning of music into words, but that's not really the point.")
sleep(2)
print('''As Igor Stravinsky once said, "I haven’t understood a bar of music in my life, but I have felt it."''')
sleep(3)
print(f"Have you ever heard of Vocaloid, {name}?")
sleep(1.5)
print("The songs normally have some deeper meaning or story behind them.")
sleep(2)
print("This is probably one of the reasons people love it so much!")
sleep(2)
print("Compared to other genres of music, Vocaloid is suprisingly new!")
sleep(2)
print("This is due to the need for electronic tools in the creation of Vocaloid Songs.")
sleep(2)
print("If you ever listen to some Vocaloid, you might find it interesting!")
sleep(2)

while topicdone == True:
    yesno = input(f"Do you listen to Vocaloid, {name}? ")
    if Yes(yesno) == True:
        topicdone = True
        print(f"That's Great, {name}!")
        sleep(1.75)
        print(
            "You know, I've always been able to relate to some of those songs in Vocaloid.")
        sleep(3)
        slowprint("That's probably because I'm in a game", lead_dots=True)
        sleep(2)
        print("I wonder if those Vocaloids are also in the same situation?")
        sleep(2.5)
        print("I guess I'll probably never know.")
        sleep(1.25)
        if loveBonus == 3:
            print ("Imagine the day I can actually visit you!")
            sleep(2.5)
            print ("In the real world, of course.")
            sleep(1.5)
            print ("We could totally listen to some Vocaloid sometime!")
            sleep(2.5)
            if type(pets) == int:
                if pets == 1:
                    print (f"We could also play with your {pet_type}, {petname}!")
                    sleep(2)
                elif pets < 1:
                    print (f"We could also play with your {pet_type}s!")
                    sleep(2)
            print (f"Wouldn't that be so romantic, {name}?")
            sleep(2)
        else:
            slowprint("Anyways", lead_dots = True)
            sleep(1)
        CustomRecord("Agreed With Topic", "Music", +5)

    elif No(yesno) == True:
        topicdone = True
        print (f"That's fine, {name}.")
        sleep(1.25)
        print ("Music has a lot of genres, so I don't really expect you to have the same opinions.")
        sleep(3)
        print ("")

    else:
        topicdone = False
        slowprint("Sorry, but I don't know what that really means",
                  lead_dots=True)
        sleep(2)
        print("Please try again!")
        sleep(1.5)

print ("Speaking of music, do you play any musical instrument?")
