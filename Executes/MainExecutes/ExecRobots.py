topicopinion = True
print("Great! I'm an expert on those!")
sleep(2)
print(robotFactsList[0])
sleep(5)
print("isn't that a fun fact?")
sleep(3)
while yesnorep == True:
    yesno = input('wanna hear another fun fact about Robots? ')
    if yesno.lower() == "yes" or yesno.lower() == "sure" or yesno.lower() == "of course":
        print("Great! What About this:")
        sleep(1)
        robotfact = random.randint(1, len(robotFactsList)-1)
        print(robotFactsList[robotfact])
        sleep(5)
        print("isn't that interesting?")
        yesnorep = False
    elif yesno.lower() == "no" or yesno.lower() == 'nope' or yesno.lower() == 'not really':
        print('ok')
        yesnorep = False
    else:
        print(name+"! Please answer with yes or no. Thanks!")
        yesnorep = True
sleep(2)
judgeres = input("Say, "+name+", what do you think of "+topic+"? ")
while repeating < 4:
    if repeating != 0:
        judgeres = input("Say, "+name+", What do you think of "+topic+"? ")
    if judgeres.lower() == "i like them" or judgeres.lower() == "i like it" or judgeres.lower() == 'i love it' or judgeres.lower() == 'i love them':
        if topicopinion == True:
            print("Me too! It's nice to know we have some common opinions!")
            sleep(1)
            interest = (interest+5)+loveBonus-negloveBonus
            TopicAgreed()
            repeating = 5
        elif topicopinion == False:
            print("oh... That's ok. I suppose everyone's different, even AIs")
            sleep(1)
            interest = (interest-5)+loveBonus
            TopicDisagreed()
            repeating = 5
    elif judgeres.lower() == "i don't like them" or judgeres.lower() == "i don't like it" or judgeres.lower() == 'i hate them' or judgeres.lower() == 'i hate it':
        if topicopinion == False:
            print("me too! It's nice to know that we have some common opinions!")
            sleep(1)
            interest = (interest+5)+loveBonus-negloveBonus
            TopicAgreed()
            repeating = 5
        elif topicopinion == True:
            print("oh... That's ok. I suppose everyone's different, even AIs")
            sleep(1)
            interest = (interest-5)+loveBonus
            TopicDisagreed()
            repeating = 5
    else:
        print("Hey, "+name+"! Be serious! I know you mean well, but this is important! Answer whether  or not you like the subject! ")
        repeating = repeating+1
if repeating == 4:
    print("hmph! Don't think of this as some kind of joke!")
    interest = interest-10
    OverRepeat()
