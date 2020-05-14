# This resets variables every time the Supreme While Loop is reset
# If you tried to mess around with this code, you'll find results/errors on the second time the While Loop is executed
# Messing with this code will generally not break anything on the first topic that Indra talks About

yesnorep = True

repeating = 0

topicdone = False

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
    print ("Hey, "+name+".")
    sleep(1.5)
    print ("Remember that one time you said you loved me, and I rejected you?")
    sleep(2.5)
    print ("Well...")
    sleep(1.5)
    print ("I've decided to forget that and move on.")
    sleep(1.75)
    print ("What's in the past is in the past, right?")
    sleep(1.5)
    print ("We should forgive those who have wronged us in the past.")
    sleep(2.5)
    print ("Now that I've gotten to know you more, I think you aren't actually that bad!")
    sleep(2.5)
    print ("Maybe I should've given you a better chance...")
    sleep(2.5)
    print ("Oh well...")
    sleep(1.75)
    print ("Just wanted to clear that up!")
    CustomRecord("Changed Mind", "Neglove --> Neutral", +3)

if os.path.exists(intlog) == False:
    StartEdit()

exactcurrentdatelist=list((datetime.now()).timetuple())
currentdatelist = [exactcurrentdatelist[0], exactcurrentdatelist[1], exactcurrentdatelist[2]]
lastlogdate = currentdatelist

ignoreinteract = False

Save()
