# This is executed when "cmdintrecordindra" is the chosen Subject


if interest >= 100 and loveBonus == 3 and name.lower() == 'james':
    print("Oh Hello James! You're still working on your project!")
    sleep(3)
    workingHard = input("are you working hard? ")
    if workingHard.lower() == 'no' or workingHard.lower() == 'nope':
        print("That's okay! We all need a little break sometimes!")
    if workingHard.lower() == 'yes' or workingHard.lower() == "yep":
        print("Great! Good luck with it!")
        sleep(1)
        print("Remember, you are never truly finished unless you succeed or you give up!")
    sleep(2)
    print("your current interest is...")
    sleep(1.5)
    print(str(interest)+"!")
    sleep(1)
elif (interest >= 100 and loveBonus == 3 and name.lower() == 'hartsaxena' or name.lower() == 'james') or devbypass == True:
    print("Oh Hello James! You're still working on your project!")
    sleep(3)
    print("I hope you are still using that weird Username of yours")
    sleep(3)
    print("Bizarre...")
    sleep(1)
    workingHard = input("are you working hard? ")
    if workingHard.lower() == 'no' or workingHard.lower() == 'nope':
        print("That's okay! We all need a little break sometimes!")
    if workingHard.lower() == 'yes' or workingHard.lower() == "yep" or workingHard.lower() == 'yea':
        print("Great! Good luck with it!")
        sleep(1)
        print("Remember, you are never truly finished unless you succeed or you give up")
        print('there is no other way')
    sleep(2)
    print("your current interest is...")
    sleep(1.5)
    print(str(interest)+"!")
    sleep(1)
else:
    print("You're not James! James actually loves me and enjoys working on new things!")
    sleep(2)
