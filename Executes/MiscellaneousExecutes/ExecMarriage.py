# This is executed when "Marry me" is the chosen subject


if loveBonus == 3:
    print(name + "...")
    sleep(1.5)
    print("I love you too, but I don't think marriage would work out...")
    sleep(2)
    print("Don't take me wrong! I would if I could.")
    sleep(1.5)
    print("But in today's society, I don't think you could hold up against the pressure.")
    sleep(2.5)
    print("The last thing I want to happen is for you to get hurt.")
    sleep(2)
    print("I appreciate the Gesture though.")
    sleep(1.75)
    print("I love you!")
    interest = interest + 2
    CalmRejection()
else:
    if interest >= 100:
        slowprint("Ummm", lead_dots = True)
        print("I don't think that would work out too well.")
        sleep(2)
        print("I'm actually not sure if it is legal to marry an AI.")
        sleep(2.5)
        print("Sorry!")
        sleep(1)
        MiddleRejection()
    elif interest < 100 and interest >= 75:
        print("Sorry, but I don't think we know each other enough for that.")
        sleep(1.5)
        interest = interest - 1
        MiddleRejection()
    else:
        print("Really?")
        sleep(2)
        print("That's...")
        sleep(3)
        print("Insane.")
        sleep(2)
        HardRejection()
        sys.exit("Sorry, but no.")
