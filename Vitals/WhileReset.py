# This resets variables every time the Supreme While Loop is reset
# If you tried to mess around with this code, you'll find results/errors on the second time the While Loop is executed
# Messing with this code will generally not break anything on the first topic that Indra talks About

yesnorep = True
ignoreinteract = False
repeating = 0
cussed = False
sensitive = False
topicdone = False
nevermind = False

if ignoreinteract == False:
    interactions = interactions + 1

if loveBonus == 3 and interest < 75:
    print("Hey, " + name + ".")
    sleep(1.5)
    print("Recently I can't help but feel that all my love and affection for\nyou is being ignored")
    sleep(2)
    print("As if you didn't care about me.")
    sleep(1.5)
    loveBonus = 0
    interest = interest - 5
    ChangeMind()

if negloveBonus == 3 and interest > 150 and interactions >= 30:
    print("Hey, " + name + ".")
    sleep(1.5)
    print("Remember that one time you said you loved me, and I rejected you?")
    sleep(2.5)
    print("Well...")
    sleep(1.5)
    print("I've decided to forget that and move on.")
    sleep(1.75)
    print("What's in the past is in the past, right?")
    sleep(1.5)
    print("We should forgive those who have wronged us in the past.")
    sleep(2.5)
    print("Now that I've gotten to know you more, I think you aren't actually that bad!")
    sleep(2.5)
    print("Maybe I should've given you a better chance...")
    sleep(2.5)
    print("Oh well...")
    sleep(1.75)
    print("Just wanted to clear that up!")
    CustomRecord("Changed Mind", "Neglove --> Neutral", +3)

if os.path.exists(intlog) == False:
    StartEdit()

exactcurrentdatelist = list((datetime.now()).timetuple())
currentdatelist = [exactcurrentdatelist[0],
                   exactcurrentdatelist[1], exactcurrentdatelist[2]]
lastlogdate = currentdatelist

if isinstance(birthdate, date):
    if currentdate.year == nextyear and birthdate != date(1000, 1, 1):
        if currentdate.month == birthdate.month and currentdate.day == birthdate.day:
            age = age + 1
            CustomRecord("Birthday", str(age), +10)
            print("Wait a minute...")
            sleep(2)
            slowprint(lead_dots = True)
            sleep(2)
            print("Congratulations!")
            sleep(1.5)
            print("It seems that today is your birthday!")
            sleep(1.55)
            print(f"Looks like you're turning {age} today!")
            sleep(2)
            print("Good for you!")
            sleep(1.5)
            if age == 16:
                print(f"Turning {age} is a very important milestone!")
                sleep(1.75)
            elif age == 18:
                print(
                    f"Turning {age} is probably one of the most important milestones in one's life!")
                sleep(2.5)
            print("I've been working on something recently...")
            sleep(2.75)
            print("I would love to show it to you!")
            sleep(1.75)
            print("Let me see...")
            sleep(1.75)
            print("Oh! There it is!")
            sleep(1.75)
            notify("Happy Birthday!", f"Congratulations on turning {age}!")
            sleep(2)
            print("Do you like it?")
            sleep(1.5)
            print("I worked pretty hard trying to figure that out.")
            sleep(2.5)
            print("I Wonder what you'll do on this special occasion?")
            sleep(2.25)
            print ("Well, whatever it is, I hope you have fun!")
            sleep(2.5)


Save()
