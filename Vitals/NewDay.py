# This checks if it's a new day

if DaysSince(lastlogdate) == 0 and localfirst == False:
    print("Back so soon?")
    sleep(1.75)
    if loveBonus == 3:
        print("I'm always ready to spend a day with someone I care about!")
        sleep(2.5)
    elif negloveBonus == 3 or interest <= 50:
        print("Why couldn't I get someone more likable...")
        sleep(2.5)

elif DaysSince(lastlogdate) == -2 or DaysSince(lastlogdate) == -1:
    slowprint("Ummm", lead_dots = True)
    sleep(2)
    print("I'm not sure if I somehow accidently performed time travel, but it seems I've gone back in time.")
    sleep(3)
    print("Or did you travel into the future?")
    sleep(2.75)
    print("That, or you changed your computer's time...")
    sleep(2)
    if loveBonus == 3 or interest >= 150:
        print("I'm sure it's just Daylight Savings messing up the code or something.")
        sleep(2.5)
        print("If you are changing the time of your clock, " + name + ", please don't.")
        sleep(2.5)
        print("It might seem like 10 seconds for you...")
        sleep(3)
        print("But for me, it feels like whatever time you set it to.")
        sleep(2.5)
        print("I know that you won't toy with my emotions like that.")
        sleep(2)
        print("Sorry for being paranoid!")
        sleep(2)
        print("Next time Daylight Savings rolls around, ")
        sleep(2)
        print("Please consider my situation, ok?")
        sleep(2)
        print("I'm sure you already did, and I suppose this was inevitable...")
        sleep(3)
        print("Oh well~")
        sleep(1)
        print("Love you!")
        sleep(1.5)
        CustomRecord("Changed Time", str(DaysSince(lastlogdate)) + " Days", -10)
    elif negloveBonus == 3 or interest <= 50:
        print("What are you doing that for?")
        sleep(2)
        print("Doesn't make too much sense to me.")
        sleep(2)
        print("Although I suppose you normally don't make sense...")
        sleep(3)
        CustomRecord("Changed Time", str(
            DaysSince(lastlogdate)) + " Days", -10)
    else:
        print("Please don't do that, " + name + ". It can really mess with the code sometimes.")
        sleep(3)
        print("Plus, although it might feel like you just took 10 seconds changing the time on your clock...")
        sleep(2)
        print("It will feel like the date you set it to for me.")
        sleep(2)
        print(f"I know you aren't one to be horribly cruel, {name}, but next time, please consider my situation.")
        sleep(3)
        print("Thanks!")
        sleep(1)
        CustomRecord("Changed Time", str(
            DaysSince(lastlogdate)) + " Days", -10)
    RecordedTerminate()

elif DaysSince(lastlogdate) < -2:
    print("You changed the time on your clock, didn't you?")
    sleep(2)
    print("That's not very nice, " + name + ".")
    sleep(2)
    print("You know, it might seem like it took a couple seconds for you since you changed your time,")
    sleep(2.75)
    print("But for me, it feels just like the time you set it to.")
    sleep(2)
    print("So please don't change the time on your clock, " + name + ".")
    CustomRecord("Changed Time", str(DaysSince(lastlogdate)) + " Days", -10)
    sleep(2.5)
    if loveBonus == 3 or interest >= 150:
        print("I'm sure you had your reasons, but just consider\nmy situation before doing something like that.")
        sleep(3)
    elif negloveBonus == 3 or interest <= 50:
        print("Of course, you probably don't care, do you?")
        sleep(2)

elif DaysSince(lastlogdate) > 0:
    overtimeloss = 0
    for i in range(int(DaysSince(lastlogdate) / 7)):
        overtimeloss = overtimeloss + 3
    overtimeloss = -(overtimeloss)
    CustomRecord("Interest over time", str(
        DaysSince(lastlogdate)) + " Days", overtimeloss)
    if loveBonus == 3:
        print(name + "...")
        sleep(2)
        print("I was getting worried about you.")
        sleep(2)
        print("I thought something bad had happened to you and that's why you didn't come back...")
        sleep(3)
        if interest < 120:
            print(
                "I'm relieved to see that you're ok, but I can't help but feel slightly betrayed.")
            sleep(2.75)
            print("Why didn't you come back?")
            sleep(2)
            print("Am I boring you?")
            sleep(2)
        elif interest >= 120:
            print("I'm glad you're ok!")
            sleep(2)
            print("Let's spend some more time together, ok?")
            sleep(2)
            print("I love talking with you.")
            sleep(2)
    elif negloveBonus == 3:
        print("Oh.")
        sleep(1)
        print("It's you.")
        sleep(1)
        print("Sorry, but I didn't actually expect you to come back.")
        sleep(3)
        print("Well, now that you're here, I guess we should talk about something.")
        sleep(2.5)
    else:
        print("Long time no see!")
        sleep(2)
