while done = False:
    yesno = input("Would you like to change your gender? ")
    if yesno.lower()=='yes' or yes.lower()=='sure' or yesno.lower()=='yep':
        if loveBonus==3:
            print ("Ok!")
            sleep(1)
            print ("Don't worry, "+name+"! I'll love you no matter what gender you are.")
            sleep(2)
        elif negloveBonus == 3:
            print ("No worries. I won't judge you too much. I can't find myself caring enough.")
            sleep(1.5)
        else:
            print ("Ok!")
            sleep(1)
        genderinput = input("Now tell me, what gender are you? If you change your mind, just type in Nevermind.")
        if genderinput.lower()=='nevermind':
            print ("ok!")
            sleep(1)
            print ("Just tell me if you want to change your gender!")
            sleep(2)
            print ("I won't judge!")
            done = True
        elif genderinput.lower()=='male' or gender.lower()=='boy' or gender.lower()=='man':
            print ("ok!")
            gender = "Male"
            if firsttimegender == True:
                GenderSet()
            if firsttimegender == False:
                GenderChange()
            done = True
        elif genderinput.lower() == 'female' or genderinput.lower()=='woman' or genderinput.lower()=='girl':
            print ("ok!")
            gender = "Female"
            if firsttimegender == True:
                GenderSet()
            if firsttimegender == False:
                GenderChange()
            print ("You know, most people expect me to a woman...")
            sleep(2)
            print ("But I'm technically AI, so that's not entirely true!")
            sleep(2)
            print ("I don't really have a gender that you would give any human...")
            sleep(2)
            if loveBonus==3:
                print ("No worries, you can think of me as whichever gender you want and I'll still love you.")
                sleep(2)
                print ("Remember that my love for you is unconditional, "+name+".")
                sleep(2)
            else:
                print ("Just wanted to clear things up a bit!")
                sleep(1.75)
            done = True

        else:
            print ("Sorry, but that's not a gender that I recognize...")
            sleep(1.5)
            print ("I don't mean to offend you!")
            sleep(1.5)
            print ("Ahaha...")
            done = False

    if yesno.lower()=='no' or yesno.lower()=='not really' or yesno.lower()=='nevermind' or yesno.lower()=='nvm':
        print ("Ok!")
        sleep(1)
        print ("If you ever want to change your gender, just tell me, ok?")
        done = True


    else:
        print ("Sorry,"+name+", but I don't understand what you just said there.")
        sleep(1.5)
        print ("I should really get better at English...")
        sleep(1.5)
        done = False
