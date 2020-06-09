# This is executed when the topic is "Pets"
# TODO: actually complete this

# I just couldn't resist trying some f-strings, sorry!
print ("I've never had any pets, so I don't really have an opinion on them.")
sleep(2.5)
print("I've heard there are plenty of different types of pets, though!")
sleep(2)
print("It can be anything from a Dog or a Cat,")
sleep(1.75)
print ("to something much more exotic like a Snake or a Frog!")
sleep(2)
while topicdone == False:
    petsinput = input(f"How many pets do you own, {name}? ")
    if petsinput.lower() == 'none' or petsinput.lower() == 'no pets' or petsinput.lower() == 'no pet':
        petsinput = 0
    try:
        petsinput = int(petsinput)
        error = False
    except ValueError:
        print(f"Sorry, {name}, but that's not an integer. Please try again!")
        error = True
        topicdone = False
    if error == False:
        if petsinput < 0:
            print ("...")
            sleep(2)
            print ("That's a bit bizzare, don't you think?")
            sleep(1.5)
            if loveBonus == 3:
                print (f"I know you're just joking, {name}.")
                sleep(1.5)
                print ("Love you!")
                sleep(1)
                print ("Please do try again, ok?")
                sleep(1.25)
            print ("Please try again, and be serious this time, ok?")
            sleep(2)
            topicdone = False
        if type(pets) == int:
            if pets > petsinput and petsinput < 0:
                print("Oh.")
                sleep(1)
                print(f"Sorry, {name}.")
                sleep(1.5)
                print(
                    f"I'm not exactly sure, but I think last time you told me it was {pets}.")
                sleep(2.5)
                print("I can only assume...")
                sleep(2)
                slowprint(lead_dots = True)
                sleep(1.75)
                print("Sorry.")
                sleep(1)
                sensitive = True
            elif pets < petsinput:
                print(f"Last time, you said you had {pets} pets!")
                sleep(1.5)
                print("Now, you have " + str(petsinput - pets) + " more pets!")
                sleep(1)
                print("Good for you!")
                sleep(1.5)
                sensitive = False
        else:
            if petsinput == 0:
                print(f"That's ok, {name}.")
                sleep(1.5)
                print("A lot of people don't own pets!")
                sleep(2)
                print("There are many legitimate reasons not to own one,\nlike allergies, your current economic state, and just not being particularly\nfond of animals!")
                sleep(3.5)
                print("I don't own a pet, and I'm not particularly sad about it!")
                sleep(3)
                if loveBonus == 3:
                    print(
                        "I don't ever need to worry about being lonely anymore, right?")
                    sleep(2)
                    print("After all, I've got you!")
                    sleep(1)
                    print("You're all I could ever ask for!")
                    sleep(1.5)
                    print("Hehehe~")
                    sleep(1.75)
                elif negloveBonus == 3 or interest <= 80:
                    print("Although I must say, it can get pretty lonely sometimes...")
                    sleep(2.5)
            elif petsinput == 1:
                print("That's nice!")
                sleep(1.5)
                print(
                    "It's not really good to have too many pets, since they can do some pretty nasty things.")
                sleep(2)
                slowprint("Not to mention health issues", lead_dots = True)
                sleep(1.5)
                print("You can never be too safe!")
                sleep(1.5)
            elif petsinput == 2 or petsinput == 3:
                print(
                    "It's always heartwarming to see 2 or 3 animals grow up with eachother, even if they're different species!")
                sleep(2.5)
                print(
                    "It allows them to grow a connection towards eachother, sometimes even more so than the owner!")
                sleep(2.5)
            elif petsinput == 4 or petsinput == 5:
                slowprint(lead_dots = True)
                sleep(2)
                print(f"That's slightly concerning, {name}.")
                sleep(1.5)
                print("Owning too many pets isn't good for you.")
                sleep(1.5)
                print("If you really love them, I won't judge though!")
                sleep(2)
                if loveBonus == 3:
                    print("I will always support anything you try to achieve in life!")
                    sleep(2)
                    print("<3")
                    sleep(1)
                elif negloveBonus == 3 or interest <= 130:
                    CustomRecord("Large Number", "Pets", -5)
                    print("Be careful, ok?")
                    sleep(1)
            elif petsinput >= 6:
                slowprint(lead_dots = True)
                sleep(1)
                print(f"That's not really normal, {name}.")
                sleep(1.5)
                print (f"Too many pets aren't good for you, {name}.")
                sleep(1.5)
                print ("I hope you're careful.")
                sleep(2)
                print("I'm sure you love each and everyone of them, though!")
                sleep(1.5)
                if loveBonus == 3:
                    print("Take care of them and yourself, ok?")
                    sleep(2)
                    print(
                        "I would hate it if you got hurt by your own pets, whether directly or indirectly.")
                    sleep(2.5)
                    print(
                        f"I love you, {name}, and I would hate to hear that you got hurt somehow.")
                    sleep(2)
        pets = petsinput
        topicdone = True
if sensitive == False:
    topicdone = False
    while topicdone == False:
        print("You know, there's a very common comparison made between Cats and Dogs.")
        sleep(2.5)
        print("You've probably heard of it.")
        sleep(1.5)
        judgeres = input("Well, what do you think? Do you like Cats or Dogs? ")
        judgeres = judgeres.lower()
        # TODO: Finish this
        if judgeres == 'cats' or judgeres == 'felines' or judgeres == 'cats are better' or judgeres == 'i like cats':
            topicdone = True
            print("I've always thought that cats were so cute!")
            sleep(1.5)
            print(
                "When you think of cats, you probably think of an Orange or Grey Tabby cat.")
            sleep(2.5)
            print(
                "In reality, The International Cat Association lists 71 different types of cats!")
            sleep(2.75)
            print("They're all so cute! ≧◡≦")
            sleep(2)
            print("I wish I owned a cat!")
            sleep(2)
            if loveBonus == 3:
                print("Then again, I won't ever need someone other than you.")
                sleep(2)
                print("You're all I could ever ask for.  <3")
                sleep(1.5)
                print(
                    "If I really did own a cat, though, I would probably call it Mimi.")
                sleep(1.5)
                print("I don't really know why...")
                sleep(2)
                print("Sorry if I'm rambling too much!")
                sleep(1.5)
                print("Ahaha~")
                sleep(1)
            if pets != 0:
                topicdone = False
                while topicdone == False:
                    yesno = input(f"Tell me, {name}, do you own a cat? ")
                    if Yes(yesno) == True or yesno.lower() == 'i own a cat' or yesno.lower() == 'yes i do':
                        while topicdone == False:
                            new_pet_type_amount = input("How many do you own? ")
                            try:
                                pet_type_amount = int(new_pet_type_amount)
                                topicdone = True
                            except ValueError:
                                topicdone = False
                                print ("Sorry, but that's not a valid number.")
                                sleep(2)
                                print ("Please try again.")
                                sleep(1.25)
                        pet_type = "cat"
                        topicdone = True
                        print(f"That's so cool, {name}!")
                        sleep(1.25)
                        if pets == 1:
                            petname = input("What's your cat's name? ")
                            if petname.lower() in cusswords:
                                cussed = True
                                print ("You're joking, right?")
                                sleep(1.25)
                                print ("That's not even funny...")
                                sleep(1.5)
                                print ("I can't believe you would even say something like that.")
                                sleep(2)
                                CustomRecord("Cussword", petname, -15)
                            else:
                                if negloveBonus == 3 or interest <= 75:
                                    print ("It's ok, I guess...")
                                else:
                                    print ("That's a wonderful name!")
                                sleep(1.5)
                                if loveBonus == 3 or interest >= 130:
                                    print ("You really are quite smart, aren't you?")
                                    sleep(2)
                                else:
                                    print (f"I would really love to meet {petname}!")
                                    sleep(2)
                                    print ("Hehe~")
                                    sleep(1.25)
                        else:
                            print ("I would love to meet your cats!")
                            sleep(1.5)
                            print ("They must be so cute~")
                            sleep(1.5)
                    elif No(yesno) == True or yesno.lower() == "i don't own a cat" or yesno.lower() == "i dont own a cat" or yesno.lower() == "no i don't" or yesno.lower() == "no i dont":
                        topicdone = True
                        print(f"That's ok, {name}!")
                        sleep(1)
                        print(
                            "I'm sure that whatever pet you own,\nyou love with all your heart!")
                        sleep(2)
                        if loveBonus == 3:
                            print("You're just that kind of person, after all")
                            sleep(1.5)
                            print("<3")
                            sleep(1)
                    else:
                        topicdone = False
                        print ("Sorry, but I don't really know what that means.")
                        sleep(1.5)
                        print ("Please answer with yes or no.")
                        sleep(1.5)
            if cussed == False:
                CustomRecord("Agreed with Topic", "Cats", +3)
            topicdone = True
        elif judgeres == 'dogs' or judgeres == 'dogs are better' or judgeres == 'canines' or judgeres == 'i like dogs':
            print("Dogs are probably the most common answer, to be honest.")
            sleep(2.5)
            print("I don't really have an opinion on whether or not dogs are better than cats,\nsince I don't have one...")
            sleep(3)
            print("I've heard dogs can be very protective of their owners!")
            sleep(1.5)
            print("How nice~")
            sleep(1.25)
            if loveBonus == 3:
                print(
                    "I would love to own a dog if they really are as loving as people say they are.")
                sleep(2.5)
                print("Of course, I'm perfectly fine with just staying with you~")
                sleep(2.5)
                print("You're all I'll ever need, after all  <3")
                sleep(1.5)
            if pets != 0:
                topicdone = False
                while topicdone == False:
                    yesno = input(f"Do you own a dog, {name}? ")
                    if Yes(yesno) == True or yesno.lower() == 'i own a dog' or yesno.lower() == 'yes i do':
                        while topicdone == False:
                            new_pet_type_amount = input("How many do you own?")
                            try:
                                pet_type_amount = int(new_pet_type_amount)
                                topicdone = True
                            except ValueError:
                                topicdone = False
                                print ("Sorry, but that's not a valid number.")
                                sleep(1.5)
                                print ("Please try again.")
                                sleep(1.25)
                        print ("That's great!")
                        sleep(1.25)
                        pet_type = 'dog'
                        topicdone = False
                        petname = input("What's your dog's name? ")
                        if word in petname for word in cusswords:
                            cussed = True
                            print ("You're joking, right?")
                            sleep(1.25)
                            print ("That's not even funny...")
                            sleep(1.5)
                            print ("I can't believe you would even say something like that.")
                            sleep(2)
                            CustomRecord("Cussed", topic, -10)
                        else:
                            if negloveBonus == 3 or interest <= 75:
                                print ("It's ok, I guess...")
                            else:
                                print ("That's a wonderful name!")
                            sleep(1.5)
                            if loveBonus == 3 or interest >= 130:
                                print ("You really are quite smart, aren't you?")
                                sleep(2)
                            else:
                                print (f"I would really love to meet {petname}!")
                                sleep(2)
                                print ("Hehe~")
                                sleep(1.25)

                    elif No(yesno) == True or yesno.lower() == "i don't own a dog" or yesno.lower() == "i dont own a dog" or yesno.lower() == "no i don't" or yesno.lower() == "no i dont":
                        topicdone = True
                        print(f"That's fine, {name}!")
                        sleep(1)
                        if pets == 1:
                            print(
                                "I'm sure that no matter what pet you own,\nyou love it with all your heart!")
                        elif pets > 1:
                            print ("I'm sure that you love all the pets you own with all of your heart!")
                        sleep(2)
                        if loveBonus == 3:
                            print("You're just that kind of person, after all")
                            sleep(1.5)
                            print("<3")
                            sleep(1)
                    else:
                        topicdone = False
                        print ("Sorry, but I don't really know what that means.")
                        sleep(1.5)
                        print ("Please answer with yes or no.")
                        sleep(1.5)
        else:
            topicdone = False
            print("Sorry, but that's not really an answer to my question...")
            sleep(2.5)
            print("Please try again!")
            sleep(1.5)
elif sensitive != False:
    print("If you need, you should always take a rest.")
    sleep(1.5)
    print("I'm sure there are plenty of people who understand your loss.")
    sleep(2)
    if loveBonus == 3:
        print(f"I love you, {name}, and I would hate to see you get hurt.")
        sleep(2)
        print("You can always spend some time with me if it helps.")
        sleep(1.5)
        print("Don't get too stressed, ok?")
        sleep(1.5)
