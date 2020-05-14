# These are technically supposed to be part of the FunctionsReset.py file, but since the more variables that are added to the game, the longer these two functions will get, I decided to move these to a seperate file


def Save():
    ''' Saves the game everytime the WhileReset file is run. '''

    global lastlogdate
    if firstrun == True:
        lastlogdate = currentdatelist
    savefile = open(saves / "save.json", 'w')
    savedict = {
        "name": name,
        "interest": interest,
        "interactions": interactions,
        "loveBonus": loveBonus,
        "negloveBonus": negloveBonus,
        "devbypass": devbypass,
        "lastlogdatevars": {
            "lastlogdate": lastlogdate,
            "lastlogdateyear": lastlogdate[0],
            "lastlogdatemonth": lastlogdate[1],
            "lastlogdateday": lastlogdate[2],
        },
        "firsttimes": {
            "firsttimeIndra": firsttimeIndra,
            "firsttimeVideoGames": firsttimeVideoGames,
        },
    }
    json.dump(savedict, savefile, indent=1)
    savefile.close()


def Load():
    ''' Loads the Savefile at the beginning of each game session. '''

    ''' These simply allow me to change the variables from the function.
    I know they're not recommended, but I decided "Screw that!" and went along with it anyways'''

    global name
    global interest
    global loveBonus
    global negloveBonus
    global firsttimeIndra
    global firsttimeVideoGames
    global devbypass
    global lastlogdate
    global lastlogdateyear
    global lastlogdatemonth
    global lastlogdateday
    global interactions

    savefilepath = saves / "save.json"
    with open(savefilepath, 'r') as j:
        sdict = json.loads(j.read())
    j.close()
    name = sdict["name"]
    interest = sdict["interest"]
    interactions = sdict["interactions"]
    loveBonus = sdict["loveBonus"]
    negloveBonus = sdict["negloveBonus"]
    devbypass = sdict["devbypass"]
    lastlogdateyear = sdict["lastlogdatevars"]["lastlogdateyear"]
    lastlogdatemonth = sdict["lastlogdatevars"]["lastlogdatemonth"]
    lastlogdateday = sdict["lastlogdatevars"]["lastlogdateday"]
    lastlogdate = sdict["lastlogdatevars"]["lastlogdate"]
    firsttimeIndra = sdict["firsttimes"]["firsttimeIndra"]
    firsttimeVideoGames = sdict["firsttimes"]["firsttimeVideoGames"]
