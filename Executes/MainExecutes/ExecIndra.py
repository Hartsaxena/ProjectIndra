# Executed when "Indra" is the chosen subject


topicopinion = True
print("You want to know more about me and this project!? Great!")
sleep(2)
print(indraFactsList[0])
sleep(4)
print("The more you know!")
sleep(2)
if firsttimeIndra == True:
    print("Since this topic is supposed to be all about me, I'm gonna override some code just to show off real quick...")
    sleep(4)
    print("don't tell the creator!")  # First Aspect of lore for now.
    os.makedirs(
        imindra, exist_ok=True)
    IndraComment()
    exec(open(vitals/"SpamText.py").read())
    sleep(3)
elif firsttimeIndra == False:
    print("We've already had this conversation, so I don't need to override anything. I already have control c:<")
    IndraComment()
IndraFact = random.randint(1, len(indraFactsList)-1)
firsttimeIndra = False
while yesnorep == True:
    yesno = input("Do you want to know another fact about me and this project? ")
    if yesno.lower() == 'yes' or yesno.lower() == 'of course' or yesno.lower() == 'sure':
        print("Great!")
        sleep(1)
        IndraEdit()
        print("I put this fact in the Indra.txt file!")
        sleep(1.75)
        print('Look for it in your "ProjectIndra" folder!')
        sleep(3)
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
        judgeres = input("Say, "+name+", What do you think of me and this project? ")
    if judgeres.lower() == "i like them" or judgeres.lower() == "i like it" or judgeres.lower() == 'i like you' or judgeres.lower() == 'i like her':
        if topicopinion == True:
            print("That's so nice! I think you're a great person too!")
            sleep(1)
            interest = (interest+10)+loveBonus-negloveBonus
            IndraAgreed()
            repeating = 5
        elif topicopinion == False:
            print("oh... I guess you're bored of me...")
            sleep(1)
            interest = (interest-20)+loveBonus-negloveBonus
            IndraDisagreed()
            repeating = 5
    elif judgeres.lower() == "i don't like them" or judgeres.lower() == "i don't like it" or judgeres.lower() == "i don't like her" or judgeres.lower() == "i don't like you" or judgeres.lower() == 'i hate her' or judgeres.lower() == 'i hate you':
        if topicopinion == False:
            print("That's so nice! I think you're a great person too!")
            sleep(1)
            interest = (interest+10)+loveBonus-negloveBonus
            IndraAgreed()
            repeating = 5
        elif topicopinion == True:
            print("oh... I guess you're bored of me...")
            sleep(1)
            interest = (interest-20)+loveBonus-negloveBonus
            IndraDisagreed()
            repeating = 5
    elif judgeres.lower() == 'i love her' or judgeres.lower() == 'i love you':
        if name.lower() == 'james' or name.lower() == 'hartsaxena':
            print("Of course you do, James.")
            sleep(2)
            print("If you didn't, why would you spend so much time on me?")
            sleep(3)
            repeating = 5
        elif loveBonus == 3 or name.lower() == 'james' or name.lower() == 'hartsaxena':
            print("I love you too, "+name+".")
            sleep(1.5)
            print("I wish I could give you a hug, but some... restraints pull me back to this cruel cell behind the screen")
            sleep(3)
            repeating = 5
        elif interest >= 150:
            print("...")
            sleep(2)
            print("Wh-What?")
            sleep(2)
            print("...")
            sleep(2)
            print("Really?")
            sleep(2)
            print("I love you too, "+name+".  c:")
            interest = (interest+20)+loveBonus
            LoveAgreed()
            loveBonus = 3
            negloveBonus = 0
            repeating = 5
        elif interest <= 50:
            print("You're joking, right?")
            sleep(2)
            interest = interest-15
            LoveDisagreed()
            negloveBonus = 3
            loveBonus = 0
            repeating = 5
        else:
            interest = (interest+5)+loveBonus-negloveBonus
            print("I'm not sure what to say to that...")
            sleep(2)
            print("You're nice, but I don't think we know each other for that one yet")
            sleep(3)
            print("Maybe some other time!")
            sleep(1.75)
            LoveShrugged()
            repeating = 5
    else:
        print("Hey, "+name+"! Be serious! I know you mean well, but this is important! Answer whether or not you like the subject!")
        repeating = repeating+1
if repeating == 4:
    print("hmph! Don't think of this as some kind of joke!")
    interest = interest-10
    OverRepeat()
