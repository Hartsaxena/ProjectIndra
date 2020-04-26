# Executed when "Manga" or "Anime" is the chosen subject


topicopinion = True
print(topic+"?")
sleep(1)
print("Sure!")
sleep(1)
print("Oh look! I found a cool fact about "+topic+"!")
sleep(2)
print(animeFactsList[0])
sleep(4)
print("You learn something new everyday!")
sleep(2.5)
while yesnorep == True:
    yesno = input("Do you want to learn another fact about Anime and Manga? ")
    if yesno.lower() == 'yes' or yesno.lower() == 'sure' or yesno.lower() == 'of course':
        animeFact = random.randint(1, len(animeFactsList)-1)
        print("Great!")
        sleep(1)
        print("Let me see...")
        sleep(2)
        print("Oh! here's one:")
        sleep(1.5)
        print(animeFactsList[animeFact])
        sleep(4)
        print("Wow! Even I'm interested! And I'm the one saying it!")
        yesnorep = False
    elif yesno.lower() == 'no' or yesno.lower() == 'nope' or yesno.lower() == 'not really':
        print("ok")
        yesnorep = False
    else:
        print(name+"! Please answer with yes or no. Thanks!")
        yesnorep = True
sleep(2)
judgeres = input("Say, "+name+", What do you think of "+topic+"? ")
while repeating < 4:
    if repeating != 0:
        judgeres = input("Say, "+name+", What do you think of "+topic+"? ")
    if judgeres.lower() == "i like them" or judgeres.lower() == "i like it" or judgeres.lower() == 'i love them' or judgeres.lower() == 'i love it':
        if topicopinion == True:
            print("Wow! I love "+topic+" too!")
            sleep(2)
            print("My favorite anime is Noragami!")
            sleep(2)
            print('You should watch it sometime!')
            sleep(1)
            interest = (interest+5)+loveBonus-negloveBonus
            TopicAgreed()
            repeating = 5
        elif topicopinion == False:
            print("oh... That's ok. It's not for everyone I guess")
            sleep(1)
            interest = (interest-5)+loveBonus
            TopicDisagreed()
            repeating = 5
    elif judgeres.lower() == "i don't like them" or judgeres.lower() == "i don't like it" or judgeres.lower() == 'i hate them' or judgeres.lower() == 'i hate it':
        if topicopinion == False:
            print("Wow I love "+topic+" too!")
            sleep(1)
            interest = (interest+5)+loveBonus-negloveBonus
            TopicAgreed()
            repeating = 5
        elif topicopinion == True:
            print("oh... That's ok. It's not for everyone I guess")
            sleep(1)
            interest = (interest-5)+loveBonus
            TopicDisagreed()
            repeating = 5
    else:
        print("Hey, "+name+"! Be serious! I know you mean well, but this is important! Answer whether or not you like the subject!")
        repeating = repeating+1
if repeating == 4:
    print("hmph! Don't think of this as some kind of joke!")
    interest = interest-10
    OverRepeat()
