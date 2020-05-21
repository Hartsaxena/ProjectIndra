# This is executed when the Player wants to change their newage
# This is very ugly looking code

nevermind = False
changevars = False
while topicdone == False:
    if age is None or birthdate == date(1000, 1, 1):
        age = None
        birthdate = date(1000, 1, 1)
        print("Know that you mention it, I just realized that you've never really\ntold me how old you are!")
        sleep(2.5)
        print("I would love to know!")
        sleep(1.75)
        # This triggers if Yes(yesno) == True:
        yesno = 'yes'
    else:
        while topicdone == False:
            yesno = input("Would you like to change your age? ")
            if Yes(yesno) == True:
                topicdone = True
                print("Ok!")
                sleep(1)
            elif No(yesno) == True:
                print("That's fine.")
                sleep(1)
            else:
                print("Please answer with yes or no.")
                sleep(1.5)
                print(
                    "I'm still learning about different ways to say yes or no, so please be patient!")
                sleep(3)
                print("Sorry!")
                sleep(1.5)

    if Yes(yesno) == True:
        topicdone = False
        while topicdone == False:
            print("")
            birthtopicdone = False
            while birthtopicdone == False:
                birthyearinput = input("Tell me, what year were you born? ")
                if birthyearinput.lower() == 'nevermind':
                    topicdone = True
                    birthtopicdone = True
                    nevermind = True
                else:
                    try:
                        try:
                            birthyearinput = int(birthyearinput)
                        except ValueError:
                            birthyearinput = w2n.word_to_num(birthyearinput)
                        if birthyearinput < 1895:
                            print("Sorry, but that's not a valid year.")
                            sleep(1.5)
                            print("there's no way you're really that old!")
                            sleep(2)
                            print("Please be serious.")
                            sleep(1.5)
                        else:
                            birthtopicdone = True
                    except ValueError:
                        print(f"Sorry, but {birthyear} isn't a valid year.")
                        sleep(1.75)
                        print("Please try again!")
                        sleep(1)
            birthtopicdone = False
            if nevermind == True:
                topicdone = True
                birthtopicdone = True
            while birthtopicdone == False:
                birthmonthinput = input("What month were you born? ")
                if birthmonthinput.lower() == 'nevermind':
                    topicdone = True
                    birthtopicdone = True
                    nevermind = True
                else:
                    try:
                        try:
                            birthmonthinput = int(birthmonthinput)
                        except ValueError:
                            birthmonthinput = NametoMonth(birthmonthinput)
                        if birthmonthinput > 12 or birthyearinput < 1:
                            print("Sorry, but that month isn't a valid month.")
                            sleep(2)
                            print("Are you sure you typed the month in correctly?")
                            sleep(1.75)
                            print("Please try again.")
                            sleep(1)
                        else:
                            birthtopicdone = True
                    except ValueError:
                        print("Sorry, but that's not a valid number.")
                        sleep(1.25)
                        print("Please try again.")
                        sleep(1.25)
            birthtopicdone = False
            if nevermind == True:
                birthtopicdone = True
                topicdone = True
            while birthtopicdone == False:
                birthdayinput = input("What day were you born? ")
                if birthdayinput.lower() == 'nevermind':
                    topicdone = True
                    birthtopicdone = True
                    nevermind = True
                else:
                    try:
                        birthdayinput = int(birthdayinput)
                    except ValueError:
                        try:
                            birthdayinput = w2n.word_to_num(birthdayinput)
                        except ValueError:
                            birthdayinput = 999  # Triggers the if statement below
                    if birthdayinput > 31 or birthdayinput < 1:
                        print("Sorry, but that's not a valid day.")
                        sleep(1.5)
                        print("Please try again!")
                        sleep(1.25)
                    else:
                        birthtopicdone = True
            birthtopicdone = False
            if nevermind == True:
                birthtopicdone = True
                topicdone = True
                print ("Ok!")
                sleep(1)
                print ("If you ever want to change your age, just tell me, ok?")
                sleep(2)
            else:
                birthdateinput = date(
                    birthyearinput, birthmonthinput, birthdayinput)
                newage = (currentdate - birthdateinput).days
                # There are technically 365.25 days in a year, not 365 (this explains leap years, doesn't it?)
                newage = int(newage / 365.25)
                if newage <= 0:
                    topicdone = False
                    slowprint("Ummm", lead_dots = True)
                    sleep(2)
                    print(f"That doesn't make a lot of sense, {name}.")
                    sleep(2)
                    print("Apparently, you were born in the future?")
                    sleep(1.75)
                    slowprint("Ahaha", lead_dots = True)
                    sleep(1.5)
                    if negloveBonus == 3 or interest <= 75:
                        print(f"Please be serious, {name}.")
                        sleep(1.5)
                    elif loveBonus == 3:
                        print(f"You're so funny, {name}.")
                        sleep(1.5)
                        print("I love you~")
                        sleep(1.25)
                        CustomRecord("Joke", topic, +5)
                    else:
                        print(f"I really enjoy your company, {name}.")
                        sleep(1.5)
                        print("You have a lovely sense of humor.")
                        sleep(1.5)
                        CustomRecord("Joke", topic, +5)
                elif birthdateinput == currentdate:
                    print("So you were born today?")
                    sleep(1.5)
                    if loveBonus == 3 or interest >= 175:
                        CustomRecord("Joke", "Age", +3)
                        print("Ahaha~")
                        sleep(1)
                        print(f"You're so funny, {name}.")
                        sleep(1.5)
                        print("I really love your company.")
                        sleep(1.5)
                        print("You're all I could ever ask for.")
                        sleep(1.75)
                    elif negloveBonus == 3 or interest <= 50:
                        print(f"Please be serious, {name}.")
                        sleep(1.25)
                    else:
                        CustomRecord("Joke", "Age", +3)
                        print("Hehehe~")
                        sleep(1)
                        if interactions >= 15:
                            print("You're really entertaining, you know that?")
                            sleep(2.5)
                            print("I'm glad I met someone like you.")
                            sleep(1.75)
                        else:
                            print(f"That's pretty funny, {name}")
                            sleep(2)
                            print(
                                "It gets kind of lonely in here sometimes, so I appreciate you trying to entertain me.")
                            sleep(3)
                            if interest > 150:
                                CustomRecord("Blushed", "IBID[Joke]", +5)
                else:
                    if newage <= 6 and newage > 0:
                        slowprint("Ummm", lead_dots = True)
                        sleep(2)
                        print("You're joking, right?")
                        sleep(1.75)
                        topicdone = False  # topicdone is already False but this is too remind me in the future
                        # I don't want to add too many "done" variables, so I'm gonna just try to do this for now.
                        # TODO: Think of an alternative method for "Done" vars
                        while topicdone == False:
                            if newage == 6:
                                yesno = input("You're actually only 6 years old? ")
                            elif newage < 6:
                                yesno = input("You're not even 6 years old? ")
                            if Yes(yesno) == True or yesno.lower() == 'maybe' or yesno.lower() == 'maybe...':
                                topicdone = True
                                changevars = True
                                print(f"That's a little bizarre, {name}.")
                                sleep(1.5)
                                if interactions >= 30:
                                    print(
                                        "Now that I think about it, I guess I should've seen\nsomething like this coming...")
                                    sleep(3.5)
                                else:
                                    print("I never could've saw this coming!")
                                    sleep(2)
                                if negloveBonus == 3 or interest <= 60:
                                    print(
                                        "I guess you were never that mature either...")
                                    sleep(3)
                                    print("Meh.")
                                    CustomRecord("age", "6", -5)
                            elif No(yesno) == True:
                                topicdone = True
                                if loveBonus == 3:
                                    print("Ahaha~")
                                    sleep(1)
                                    print(f"You really are funny, {name}.")
                                    sleep(1.5)
                                    print(
                                        "For a second, I really thought you were 6 years old!")
                                    sleep(2.5)
                                    print(
                                        "Now that I think about it, that would be kind of ridiculous.")
                                    sleep(2.5)
                                    print(
                                        "How would a 6 year old even find this game in the first place?!")
                                    sleep(3)
                                    print(f"I really enjoy your company, {name}.")
                                    sleep(2)
                                    print("You always make my day!")
                                    sleep(1.5)
                                    print("<3")
                                    sleep(1)
                                else:
                                    print("Ah.")
                                    sleep(1)
                                    print(
                                        "You just wanted to see what happens, didn't you?")
                                    sleep(2)
                                    print("Well, I can't blame you for being curious.")
                                    sleep(2)
                                    print("I'm pretty curious myself.")
                                    sleep(2)
                                    print("Please try again, though!")
                                    sleep(1.75)
                            else:
                                print(
                                    "Sorry, but that's not really an answer to my question.")
                                sleep(2.5)
                                print(f"Don't be shy, {name}")
                                sleep(1)
                                print("I won't judge you.")
                                sleep(1.5)
                        topicdone = False
                    elif newage >= 60:
                        topicdone = False
                        changevars = True
                        print("You're older than 60?")
                        sleep(1.5)
                        slowprint(lead_dots = True)
                        sleep(2)
                        print("Cool!")
                        sleep(1)
                        print(
                            "I've always thought that older people are always the most mature.")
                        sleep(2.5)
                        print(
                            "All the ones I know have learned so much during their lifetime!")
                        sleep(2.5)
                    else:
                        topicdone = False
                        while topicdone == False:
                            newageconfirm = input(
                                f"So your age is {newage}, correct? ")
                            if Yes(newageconfirm) == True:
                                topicdone = True
                                changevars = True
                                print("Ok!")
                                sleep(1)
                                print(
                                    f"From know on, I'll remember that your birthday is on {birthmonthinput}-{birthdayinput}-{birthyearinput}.")
                                sleep(2.5)
                                print(
                                    f"Thanks for taking your time to tell me, {name}.")
                                sleep(2.5)
                                print("I really appreciate it.")
                                sleep(1.5)
                            elif No(newageconfirm) == True:
                                print("Oh.")
                                sleep(1)
                                print(
                                    "Well then, I guess we'll try again some other time, ok?")
                                sleep(1.5)
                                topicdone = True
                            else:
                                print(
                                    "Sorry, but I don't quite understand what you just said.")
                                sleep(1.5)
                                print("Please try again.")
                                sleep(1.25)

    elif No(yesno) == True:
        if age is None or birthdate == date(1000, 1, 1):
            print("Oh.")
            sleep(1)
            print("That's fine.")
            sleep(1.25)
            print("Promise me you'll tell me soon, ok?")
            sleep(2)
            if loveBonus == 3:
                print("As your lover, I think I have the right, ok?")
                sleep(2.25)
                print("I know you'll tell me eventually.")
                sleep(2)
                print("Love you!")
            elif interest >= 200 and interactions >= 30:
                print("As your lover, I think-")
                sleep(1)
                for i in range(1, 20):
                    print("")
                slowprint("Ummm", lead_dots = True)
                sleep(1)
                print("Let's just forget I said anything, ok?")
                sleep(1)
                print("Sorry if I'm talking a little fast.")
                sleep(1)
                print("I'm kind of nervous.")
                sleep(1)
                print("About nothing.")
                sleep(1)
                print("Let's just forget about this, ok?")
                sleep(1.5)
                slowprint("Ahaha", lead_dots = True)
                sleep(1.25)
                CustomRecord("Indra Blushed", "Rambling", +10)
            elif negloveBonus == 3 or interest <= 50:
                print("Not that I really care that much.")
                sleep(2)
            else:
                print(f"I would love to know more about you, {name}!")
                sleep(2)
        else:
            print("Ok!")
            sleep(1)
            print(
                "If you ever want to change your age (in this game, obviously),\njust tell me, ok?")
            sleep(2.5)

    else:
        print("Sorry, but I don't know what that means.")
        sleep(1.75)
        print("Please try again!")
        sleep(1.25)

if changevars == True:
    age = newage
    birthdate = birthdateinput
    if birthdate.month > currentdate.month or (birthdate.month == currentdate.month and birthdate.day > currentdate.day):
        nextyear = currentdate.year
    else:
        nextyear = ((currentdate.year) + 1)
