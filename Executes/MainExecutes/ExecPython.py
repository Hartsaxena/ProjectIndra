# Executed when "Python" is the chosen subject


topicopinion = True
print("Wow! What a coincidence! Did you know that this program is written with Python?")
sleep(3)
print("let me try to find a fun fact...")
sleep(1.5)
print("Oh look! Here's one:")
sleep(2)
print(pythonFactsList[0])
sleep(4)
print("You should try it sometime! You won't regret it!")
sleep(2)
while yesnorep == True:
    yesno = input("Would you like to hear another fact about Python? ")
    if Yes(yesno.lower()) == True:
        PythonFact = random.randint(1, len(pythonFactsList) - 1)
        print("Great! What about this:")
        sleep(1)
        print(pythonFactsList[PythonFact])
        sleep(4)
        print("Isn't that interesting?")
        sleep(3)
        yesnorep = False
    elif No(yesno.lower()) == True:
        print('ok!')
        sleep(0.5)
        yesnorep = False
    else:
        print(name + "! Please answer with yes or no. Thanks!")
        yesnorep = True
judgeres = input("Say, " + name + ", What do you think of " + topic + "? ")
while repeating < 4:
    if repeating != 0:
        judgeres = input("Say, " + name +
                         ", What do you think of " + topic + "? ")
    if judgeres.lower() == "i like them" or judgeres.lower() == "i like it" or judgeres.lower() == 'i love it' or judgeres.lower() == 'i love them':
        if topicopinion == True:
            print("Me too! It's nice to know we have some common opinions!")
            sleep(1)
            TopicAgreed()
            repeating = 5
        elif topicopinion == False:
            print("oh... That's ok. I suppose everyone's different, even AIs")
            sleep(1)
            TopicDisagreed()
            repeating = 5
    elif judgeres.lower() == "i don't like them" or judgeres.lower() == "i don't like it" or judgeres.lower() == 'i hate them' or judgeres.lower() == 'i hate it':
        if topicopinion == False:
            print("me too! It's nice to know that we have some common opinions!")
            sleep(1)
            TopicAgreed()
            repeating = 5
        elif topicopinion == True:
            print("oh... That's ok. I suppose everyone's different, even AIs")
            sleep(1)
            TopicDisagreed()
            repeating = 5
    else:
        print("Hey, " + name + "! Be serious! I know you mean well, but this is important! Answer whether or not you like the subject!")
        repeating = repeating + 1
if repeating == 4:
    print("hmph! Don't think of this as some kind of joke!")
    interest = interest - 10
    OverRepeat()
