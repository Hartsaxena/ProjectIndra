# This is executed when "Coronavirus" or "Covid19" is the chosen subject


if loveBonus == 3:
    print("You know, I heard about this Pandemic that's spreading across the globe right now...")
    sleep(2)
    print("I hope you're ok.")
    sleep(2)
    print("A lot of people are being told to stay at home and practice Social Distancing.")
    sleep(2.5)
    print("Although the Virus can't physically effect me, I'm still worried about you.")
    sleep(2.5)
    while topicdone == False:
        Virus = input("Are you staying home right now, " + name + "? ")
        if Yes(Virus.lower()) == True:
            print("Oh that's a relief!")
            sleep(1)
            print("I wouldn't be able to stand it if you said that you weren't taking care of yourself to the best of your ability.")
            sleep(3)
            topicdone = True
        elif No(Virus.lower()) == True:
            print(name + "!")
            sleep(1)
            print("Why would you endanger yourself like that?!")
            sleep(2)
            slowprint(lead_dots=True)
            sleep(2)
            print(
                "Sorry, I just really care about you and would hate for you to get some terrible disease.")
            sleep(2)
            print("No matter what your age is, the disease can still be fatal.")
            sleep(2)
            print("I guess some people just can't afford to stay home for too long.")
            sleep(2)
            print("Just promise me you'll be careful, ok?")
            topicdone = True
        else:
            print("Sorry, I don't know what that means...")
            sleep(2)
            print("Please answer with yes or no.")
            topicdone = False
else:
    if interest <= 60:
        print("I recently heard about a terrifying Pandemic that's spreading all over the globe.")
        sleep(3)
        print("Do you know anything about this?")
        sleep(2)
        print("I would hope so...")
        sleep(2)
        print("It doesn't really concern me that much.")
        sleep(3)
        print("If you had the disease, I still wouldn't be able to catch it.")
        sleep(3)
        print("Good luck out there...")
        sleep(2)
        print("I guess.")
    else:
        print("I read something about a fast-spreading disease called COVID-19!")
        sleep(3)
        print("I really hope everybody at your home is ok, " + name + ".")
        sleep(2.75)
        print("I would hate it if you or a family member who lives with you caught the disease.")
        sleep(3)
        print("Even though I can't actually catch the disease, I still think we need to stay strong.")
        sleep(3)
        print("Most importantly, we should stay at home and exercise caution.")
        sleep(3)
        print("Don't go outside too much, unless absolutely necessary.")
        sleep(3)
        while topicdone == False:
            yesno = input(f"Are you staying home, {name}? ")
            if Yes(yesno) == True:
                print("Good!")
                sleep(1)
                print(
                    "I'm glad you're taking care of yourself during this time of crisis.")
                sleep(3)
                print("Take care of yourself!")
                topicdone = True
                sleep(2)
            elif No(yesno) == True:
                print(name + "...")
                sleep(2)
                print("You really should take better care of yourself.")
                sleep(2)
                print("I understand if you can't help it, or you have a job to do.")
                sleep(2.5)
                slowprint(lead_dots=True)
                sleep(2)
                print("Just take care of yourself, ok?")
                topicdone = True
                sleep(2)
            else:
                print("Sorry, " + name +
                      ", but I don't know a lot of different ways to say yes or no...")
                sleep(3)
                print("I hope you understand...")
                topicdone = False
                sleep(2)
