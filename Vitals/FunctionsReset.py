# This Defines all Custom Functions
# This also makes my job easier


def sleep(pause):
    time.sleep(pause)


def restart():
    os.execl(sys.executable, sys.executable, * sys.argv)


def StartEdit():
    a = open(intlog, "a+")
    a.write("\n"+'New Sitting: '+name+"   Time: "+ctime()+"\n")
    a.close()

def cleaner(a):
    return a.strip('\n')


# Topic Reactions

def TopicAgreed():
    a = open(intlog, "a")
    a.write("Agreed with subject: "+topic+" |  +5  |  "+str(loveBonus)+"  |  "+"  |  " +
            str(negloveBonus)+"  |  "+str(interest-5-loveBonus+negloveBonus)+" --> "+str(interest)+"\n")
    a.close()


def TopicDisagreed():
    a = open(intlog, 'a')
    a.write("Disagreed with subject: "+topic+" |  -5  |  "+str(loveBonus)+"  |  "+"  |  " +
            str(negloveBonus)+"  |  "+str(interest+5-loveBonus+negloveBonus)+" --> "+str(interest)+"\n")
    a.close()

# Indra Reactions


def IndraAgreed():
    a = open(intlog, 'a')
    a.write("Agreed With Subject: "+topic+" |  +10  |  "+str(loveBonus)+"  |  "+"  |  " +
            str(negloveBonus)+"  |  "+str(interest-10-loveBonus+negloveBonus)+" --> "+str(interest)+"\n")
    a.close()


def IndraDisagreed():
    a = open(intlog, 'a')
    a.write("Disagreed with subject: "+topic+" |  -10  |  "+str(loveBonus)+"  |  "+"  |  " +
            str(negloveBonus)+"  |  "+str(interest+10-loveBonus+negloveBonus)+" --> "+str(interest)+"\n")
    a.close()


# Love Reactions


def LoveAgreed():
    l = open(indrafolder/"Love_You.txt", 'w')
    l.write("I love you too, "+name +
            ". I hope we can love eachother for the rest of eternity.  c;\n")
    l.close()
    a = open(intlog, "a")
    a.write("Loved Indra  |  +20  | "+str(interest-20)+" --> "+str(interest)+"\n")
    a.close()


def LoveDisagreed():
    l = open(indrafolder/"Don't_Love_You.txt", 'w')
    l.write("I can't believe you would have the nerve to say something like that!\n")
    l.close()
    a = open(intlog, "a")
    a.write("Rejected by Indra  |  -20  | " +
            str(interest+20)+" --> "+str(interest)+"\n")
    a.close()


def LoveShrugged():
    l = open(indrafolder/"You're_ok.txt", 'w')
    l.write("Sorry, "+name+", but I really don't think we can get that far in our relationship. I think we should just stay as friends. You're a great person, but I don't think we know enough about eachother yet. Maybe after some time, we'll get to know each other more and I can make a decision.\n")
    l.close()
    a = open(intlog, "a")
    a.write("Friendzoned by Indra  |  +5  | " +
            str(interest-5+loveBonus)+" --> "+str(interest)+"\n")
    a.close()


# Over-Repeated


def OverRepeat():
    a = open(intlog, "a")
    a.write("Repeating subject  |  -10  | "+str(interest+10)+" --> "+str(interest)+"\n")
    a.close()


# Marriage Reactions


def CalmRejection():
    a = open(intlog, 'a')
    a.write("Calmly rejected: "+topic+" |  +1  |  "+str(loveBonus)+"  |  "+"  |  " +
            str(negloveBonus)+"  |  "+str(interest-1-loveBonus+negloveBonus)+" --> "+str(interest)+"\n")
    a.close()


def MiddleRejection():
    a = open(intlog, 'a')
    a.write("Raised Awkwardness: "+topic+" |  -1  |  "+str(loveBonus)+"  |  "+"  |  " +
            str(negloveBonus)+"  |  "+str(interest+1-loveBonus+negloveBonus)+" --> "+str(interest)+"\n")
    a.close()


def HardRejection():
    a = open(intlog, "a")
    a.write("Indra Terminated program\n")
    a.close()


def ChangeMind():
    a = open(intlog, "a")
    a.write("Indra changes her mind: "+topic+" |  -5  |  "+str(loveBonus)+"  |  "+"  |  " +
            str(negloveBonus)+"  |  "+str(interest+5-loveBonus+negloveBonus)+" --> "+str(interest)+"\n")
    a.close()

# Indra Editing


def IndraEdit():
    f = open(indrafolder/"Hello! I'm Indra!/Indra.txt", 'a')
    f.write("\nFun Fact:\n")
    f.write(indraFactsList[IndraFact]+"\n")
    f.close()


def IndraComment():
    f = open(imindra/"Indra.txt", "w")
    if loveBonus == 3:
        f.write("Love you, "+name+".   <3")
    elif negloveBonus == 3:
        f.write("I'm better than you.")
    else:
        f.write("Hello! It's me, Indra!\n")
    if name.lower() == 'james' or 'hartsaxena':
        f.write("\n Work hard!\n    (づ｡◕‿‿◕｡)づ\n")
    f.close()

# Terminate Program


def AbruptTerminate(message):
    sys.exit(message)


def RecordedTerminate(message):
    a = open(intlog, "a")
    a.write("User Terminated program\n")
    a.close()
    sys.exit(message)


def AbruptRestart():
    os.execl(sys.executable, sys.executable, * sys.argv)


def RecordedRestart():
    a = open(intlog, "a")
    a.write("User Restarted program\n")
    a.close()
    os.execl(sys.executable, sys.executable, * sys.argv)


# Record Player Status


def GenderChange():
    g = open(intlogs, 'a')
    g.write("User Changed Gender: "+gender+"\n")
    g.close()


def GenderSet():
    g = open(intlogs, 'a')
    g.write("User Recorded Gender: "+gender+"\n")
    g.close()


# Record Saves


def Save():
    s = open(saves/"save", 'w')
    try:
        s.write(str(name)+"\n"+str(interest)+"\n"+str(loveBonus)+"\n"+str(negloveBonus)+"\n"+str(firsttimeIndra)+"\n"+str(devbypass)+"\n")
    except NameError:
        exec(open(vitals/"NewGame.py"))
    s.close()


def Load():
    if os.path.exists(saves/"save") == False:
        Save()
    with open(saves/"save", 'r') as f:
        lines = [line.rstrip('\n') for line in f]
    global name
    global interest
    global loveBonus
    global negloveBonus
    global firsttimeIndra
    global devbypass
    name = str(lines[0])
    interest = int(str(lines[1]))
    loveBonus = int(str(lines[2]))
    negloveBonus = int(str(lines[3]))
    firsttimeIndra = bool(lines[4] == 'True')
    devbypass = bool(lines[5] == 'True')
    f.close()




# def execute(file):
#     exec(open(Path.home()/"Documents/ProjectIndra"/Path(file)))
