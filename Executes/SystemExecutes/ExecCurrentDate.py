# This is executed when the player wants to know the current time!
ignoreinteract = True

cdate = datetime.now()
datelisttemp = list(cdate.timetuple())
datelist = date(datelisttemp[0], datelisttemp[1], datelisttemp[2])
year = str(datelisttemp[0])
month = str(calendar.month_name[datelisttemp[1]])
day = str(datelisttemp[2])

if negloveBonus==3 or interest<=100:
    print ("Are you really too lazy to just check a clock?")
    sleep(2.5)
    print ("You're probably playing on some kind of device that has a clock, after all...")
    CustomRecord("Showed Laziness", "Time", -2)
    sleep(2.5)

else:
    print ("The Current time is...")
    sleep(1.5)
    print (month+" "+day+", "+year+"!")
    sleep(2)
    if negloveBonus==3 or interest<=50:
        print ("Just another day, I suppose.")
    elif loveBonus==3:
        print ("Everyday is better with you, my love.")
    else:
        print ("A new day always brings new oppurtunities!")
    sleep(2)
