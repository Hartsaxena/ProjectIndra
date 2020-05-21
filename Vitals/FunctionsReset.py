# This Defines all Custom Functions
# This also makes my job easier


vitals = Path(HOME_PATH / "ProjectIndra/Vitals")


def restart():
    os.execl(sys.executable, sys.executable, * sys.argv)


def StartEdit():
    a = open(intlog, "a+")
    a.write("\n" + 'New Sitting: ' + name +
            "   Time: " + str(currentdate) + "\n")
    a.close()


def cleaner(a):
    return a.strip('\n')

# This finds the Days Since a date
# The Date should be given in the format: yyyy, mm, dd (Similar to a list)


def DaysSince(givendate):
    if type(givendate) == list:
        datenow = datetime.now()
        currentdateexact = list(datenow.timetuple())
        # Simplifies the list
        currentdate = date(
            currentdateexact[0], currentdateexact[1], currentdateexact[2])
        g = list(givendate)
        pastdate = date(g[0], g[1], g[2])
        # This should normally be a positive number
        result = (currentdate - pastdate).days
        return result
    else:
        print("Sorry, but the datatype you entered could not be turned into a date.")
        return "ValueError"


def NametoMonth(month_name):
    month_name = month_name.lower()
    monthlist = {
        "january": "jan",
        "february": "feb",
        "march": "mar",
        "april": "apr",
        "may": "may",
        "june": "jun",
        "july": "jul",
        "august": "aug",
        "september": "sep",
        "october": "oct",
        "november": "nov",
        "december": "dec"
    }
    if month_name in monthlist:
        month_name = monthlist[month_name]
    return strptime(month_name, "%b").tm_mon


# This finds the amount of lines in a file

def linesin(filepath):
    if os.path.exists(filepath) == True:
        file = open(filepath, 'r')
        lines = file.readlines()
        result = len(lines)
        file.close()
        return result
    else:
        print("FUNCTION ERROR")
        print("The filepath given doesn't exist.")
        print("Function: linesin")

# Notification function that doesn't really have a use yet. It just looked cool. Might find a use for this later


def notify(title = "Title", text = "Body text"):
    os.system("""
        osascript -e 'display notification "{}" with title "{}"'
        """.format(text, title))

# Functions that detects a bunch of different ways to say "Yes" or "No"


def Yes(function):
    lowercase_function = function.lower()
    if lowercase_function == 'yes' or lowercase_function == 'yep' or lowercase_function == 'definitely' or lowercase_function == 'y' or lowercase_function == 'of course' or lowercase_function == 'ok' or lowercase_function == 'k' or lowercase_function == 'yea' or lowercase_function == 'yeah' or lowercase_function == 'sure' or lowercase_function == 'certainly' or lowercase_function == 'with pleasure':
        return True
    else:
        return False


def No(function):
    lowercase_function = function.lower()
    if lowercase_function == 'no' or lowercase_function == 'nope' or lowercase_function == 'n' or lowercase_function == 'nah' or lowercase_function == 'definitely not' or lowercase_function == 'no way' or lowercase_function == 'not really' or 'sorry but no' in lowercase_function or lowercase_function == 'sorry, but no':
        return True
    else:
        return False


def Like(function, topic=""):
    function = function.lower()
    if f'i love {topic}' in function or function == 'i really like it' or function == 'i enjoy it' or 'i like' in function:
        return True
    else:
        return False


def Dislike(function, topic=""):
    function = function.lower()
    if "i don't like" in function or "i really don't like" in function or function == 'i hate it' or function == 'i hate them' or function == 'i really hate them' or function == f"i don't like {topic}":
        return True
    else:
        return False

# Topic Reactions


def TopicAgreed():
    global interest
    interest = (interest + 5) + loveBonus - negloveBonus
    a = open(intlog, "a")
    a.write("Agreed with subject: " + topic + " |  +5  |  " + str(loveBonus) + "  |    |  " +
            str(negloveBonus) + "  |  " + str(interest - 5 - loveBonus + negloveBonus) + " --> " + str(interest) + "\n")
    a.close()


def TopicDisagreed():
    global interest
    interest = (interest - 5) + loveBonus - negloveBonus
    a = open(intlog, 'a')
    a.write("Disagreed with subject: " + topic + " |  -5  |  " + str(loveBonus) + "  |    |  " +
            str(negloveBonus) + "  |  " + str(interest + 5 - loveBonus + negloveBonus) + " --> " + str(interest) + "\n")
    a.close()


# Video Game Reactions


def GenreDisagreed():
    a = open(intlog, 'a')
    a.write("Disagreed with subject: " + genreinput + " |  -5  |  " + str(loveBonus) + "  |    |  " +
            str(negloveBonus) + "  |  " + str(interest + 5 - loveBonus + negloveBonus) + " --> " + str(interest) + "\n")
    a.close()


def CustomRecord(message, var, change):
    global interest
    interest = interest + int(change)
    a = open(intlog, 'a+')
    a.write(str(message) + ": " + str(var) + " |  " + str(change) + "  |  " + str(loveBonus) + "  |    |  " +
            str(negloveBonus) + "  |  " + (str(interest + int(change - (2 * change)))) + " --> " + str(interest) + '\n')
    a.close()


# Indra Reactions


def IndraAgreed():
    global interest
    interest = (interest + 10) + loveBonus - negloveBonus
    a = open(intlog, 'a')
    a.write("Agreed With Subject: " + topic + " |  +10  |  " + str(loveBonus) + "  |    |  " +
            str(negloveBonus) + "  |  " + str(interest - 10 - loveBonus + negloveBonus) + " --> " + str(interest) + "\n")
    a.close()


def IndraDisagreed():
    global interest
    interest = (interest - 20) + loveBonus - negloveBonus
    a = open(intlog, 'a')
    a.write("Disagreed with subject: " + topic + " |  -10  |  " + str(loveBonus) + "  |    |  " +
            str(negloveBonus) + "  |  " + str(interest + 10 - loveBonus + negloveBonus) + " --> " + str(interest) + "\n")
    a.close()


# Love Reactions


def LoveAgreed():
    global interest
    global loveBonus
    global negloveBonus
    interest = (interest + 20) + loveBonus - negloveBonus
    l = open(indrafolder / "Love_You.txt", 'w')
    l.write("I love you too, " + name +
            ". I hope we can love eachother for the rest of eternity.  c;\n")
    l.close()
    a = open(intlog, "a")
    a.write("Loved Indra  |  +20  | " + str(interest - 20) +
            " --> " + str(interest) + "\n")
    a.close()
    loveBonus = 3
    negloveBonus = 0


def LoveDisagreed():
    global interest
    global loveBonus
    global negloveBonus

    difference = interest - (interest - 50)
    interest = 50

    l = open(indrafolder / "Don't_Love_You.txt", 'w')
    l.write("I can't believe you would have the nerve to say something like that!\n")
    l.close()
    a = open(intlog, "a")
    a.write("Rejected by Indra  |  SET 50 (-" + str(difference) + ")  | " +
            str(interest + difference) + " --> " + str(interest) + "\n")
    a.close()
    negloveBonus = 3
    loveBonus = 0


def LoveShrugged():
    global interest
    interest = (interest + 5) + loveBonus - negloveBonus
    l = open(indrafolder / "You're_ok.txt", 'w')
    l.write("Sorry, " + name + ", but I really don't think we can get that far in our relationship. I think we should just stay as friends. You're a great person, but I don't think we know enough about eachother yet. Maybe after some time, we'll get to know each other more and I can make a decision.\n")
    l.close()
    a = open(intlog, "a")
    a.write("Friendzoned by Indra  |  +5  | " +
            str(interest - 5 + loveBonus) + " --> " + str(interest) + "\n")
    a.close()


# Over-Repeated


def OverRepeat():
    a = open(intlog, "a")
    a.write("Repeating subject  |  -10  | " +
            str(interest + 10) + " --> " + str(interest) + "\n")
    a.close()


# Marriage Reactions


def CalmRejection():
    a = open(intlog, 'a')
    a.write("Calmly rejected: " + topic + " |  +1  |  " + str(loveBonus) + "  |    |  " +
            str(negloveBonus) + "  |  " + str(interest - 1 - loveBonus + negloveBonus) + " --> " + str(interest) + "\n")
    a.close()


def MiddleRejection():
    a = open(intlog, 'a')
    a.write("Raised Awkwardness: " + topic + " |  -1  |  " + str(loveBonus) + "  |    |  " +
            str(negloveBonus) + "  |  " + str(interest + 1 - loveBonus + negloveBonus) + " --> " + str(interest) + "\n")
    a.close()


def GenreRejection():
    a = open(intlog, 'a')
    a.write("Raised Awkwardness: " + genreinput + " |  -1  |  " + str(loveBonus) + "  |    |  " +
            str(negloveBonus) + "  |  " + str(interest + 1 - loveBonus + negloveBonus) + " --> " + str(interest) + "\n")
    a.close()


def HardRejection():
    a = open(intlog, "a")
    a.write("Indra Terminated program\n")
    a.close()


def ChangeMind():
    a = open(intlog, "a")
    a.write("Indra changes her mind: " + topic + " |  -5  |  " + str(loveBonus) + "  |    |  " +
            str(negloveBonus) + "  |  " + str(interest + 5 - loveBonus + negloveBonus) + " --> " + str(interest) + "\n")
    a.close()


# Indra Editing


def IndraEdit():
    f = open(indrafolder / "Hello! I'm Indra!/Indra.txt", 'a')
    f.write("\nFun Fact:\n")
    f.write(indraFactsList[IndraFact] + "\n")
    f.close()


def IndraComment():
    f = open(imindra / "Indra.txt", "w")
    elsetrig = False
    if loveBonus == 3:
        f.write("Love you, " + name + ".   <3")
    elif negloveBonus == 3:
        f.write("I'm better than you.")
    else:
        f.write("Hello! It's me, Indra!\n")
        elsetrig = True
    if elsetrig == False:
        if name.lower() == 'james' or 'hartsaxena':
            f.write("\nWork hard!\n    \n(づ｡◕‿‿◕｡)づ\n")
    f.close()


# Terminate Program


def AbruptTerminate(message):
    sys.exit(message)


def RecordedTerminate(message):
    a = open(intlog, "a")
    a.write("User Terminated program\n")
    a.close()
    sys.exit(message)


def IndraTerminate(message):
    a = open(intlog, "a")
    a.write("Indra Terminated program\n")
    a.close()
    sys.exit(message)


def AbruptRestart():
    os.execl(sys.executable, sys.executable, * sys.argv)


def RecordedRestart():
    a = open(intlog, "a")
    a.write("User Restarted program\n")
    a.close()
    os.execl(sys.executable, sys.executable, * sys.argv)


def slowprint(message = '', interval = 0, lead = "", lead_interval = 0.5, lead_dots = False, newline = "\n"):
    '''Prints a string slowly, letter by letter.'''

    for letter in message:
        sys.stdout.write(letter)
        sys.stdout.flush()
        sleep(interval)
    if lead_dots == True:
        for i in range(1, 4):
            sleep(0.75)
            sys.stdout.write(".")
            sys.stdout.flush()
        sleep(0.75)
    elif lead != "":
        sleep(lead_interval/2)
        for letter in lead:
            sys.stdout.write(letter)
            sys.stdout.flush()
            sleep(lead_interval)
    print(newline)


# Record Player Status


def GenderChange():
    g = open(intlogs, 'a')
    g.write("User Changed Gender: " + gender + "\n")
    g.close()


def GenderSet():
    g = open(intlogs, 'a')
    g.write("User Recorded Gender: " + gender + "\n")
    g.close()


# Recording through text files.
# Moved to a sub-file to reduce clutter.

exec(open(vitals / "FunctionsReset_Save_Load.py").read())

# Older versions of the Save and Load function, if needed:
#
# def Save():
#     s = open(saves / "save", 'w')
#     try:
#         s.write(str(name) + "\n" + str(interest) + "\n" + str(loveBonus) + "\n" + str(negloveBonus) +
#                 "\n" + str(firsttimeIndra) + "\n" + str(devbypass) + "\n" + str(firsttimeVideoGames) + "\n" + str(lastlogdate[0]) + "\n" + str(lastlogdate[1]) + "\n" + str(lastlogdate[2]) + "\n")
#     except NameError:
#         exec(open(vitals / "NewGame.py").read())
#     s.close()
#
# def Load():
#     if os.path.exists(saves / "save") == False:
#         Save()
#     with open(saves / "save", 'r') as f:
#         lines = [line.rstrip('\n') for line in f]
#     global name
#     global interest
#     global loveBonus
#     global negloveBonus
#     global firsttimeIndra
#     global firsttimeVideoGames
#     global devbypass
#     global lastlogdate
#     name = str(lines[0])
#     interest = int(str(lines[1]))
#     loveBonus = int(str(lines[2]))
#     negloveBonus = int(str(lines[3]))
#     firsttimeIndra = bool(lines[4] == 'True')
#     devbypass = bool(lines[5] == 'True')
#     firsttimeVideoGames = bool(lines[6] == 'True')
#     lastlogdateyear = int(lines[7])
#     lastlogdatemonth = int(lines[8])
#     lastlogdateday = int(lines[9])
#     lastlogdate = [lastlogdateyear, lastlogdatemonth, lastlogdateday]
#     log = open(intlog, 'a')
#     log.write("LOAD  |  " + str(currentdate) + "\n")
#     log.close()
#     f.close()
#


def execute(file_path):
    exec(open(file_path).read())


# Download Modules in case the player doesn't already have them installed

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


def uninstall(package):
    subprocess.check_call([sys.executable, '-m', 'pip', 'uninstall', package])
