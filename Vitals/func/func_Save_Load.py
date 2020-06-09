# These are technically supposed to be part of the FunctionsReset.py file, but since the more variables that are added to the game, the longer these two functions will get, I decided to move these to a seperate file



##############################
# SAVE
##############################


def Save(message = False):
    ''' Saves the game everytime the WhileReset file is run. '''

    global lastlogdate
    if firstrun == True:
        lastlogdate = currentdatelist
    savefile = open(saves / "save.json", 'w')
    savedict = {
        "name": name,
        "profile": {
            "gender": gender,
            "agevars": {
                "age": age,
                "birthdate": {
                    "year": birthdate.year,
                    "month": birthdate.month,
                    "day": birthdate.day
                },
                "nextyear": nextyear
            },
            "petsprofile": {
                "pets": pets,
                "pet_type": pet_type,
                "petname": petname,
                "pet_type_amount": pet_type_amount,
            },
            "instrument": instrument,
        },
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
            "Indra.firsttime": Indra.firsttime,
            "VideoGames.firsttime": VideoGames.firsttime,
            "Music.firsttime": Music.firsttime,
        },
    }
    json.dump(savedict, savefile, indent=1)
    savefile.close()
    if message == True:
        print ("The game has been Saved!") # Unused
        sleep(1.5)

##############################
# LOAD
##############################

def Load(message = False):
    ''' Loads the Savefile at the beginning of each game session. '''

    ''' These simply allow me to change the variables from the function.
    I know global variables are not recommended, but I decided "Screw that!" and went along with it anyways'''

    # I'm pretty sure class variables (like Indra.firsttime) are global...
    global age
    global birthdate
    global devbypass
    global gender
    global interactions
    global instrument
    global petname
    global interest
    global lastlogdate
    global lastlogdateday
    global lastlogdatemonth
    global lastlogdateyear
    global loveBonus
    global name
    global negloveBonus
    global nextyear
    global pet_type
    global pet_type_amount
    global pets

    savefilepath = saves / "save.json"
    with open(savefilepath, 'r') as j:
        sdict = json.loads(j.read())
    j.close()

    profile = sdict["profile"]

    name = sdict["name"]
    gender = profile["gender"]
    age = profile["agevars"]["age"]
    birthdate = date(profile['agevars']['birthdate']["year"], profile["agevars"]["birthdate"]["month"], profile["agevars"]["birthdate"]["day"])
    instrument = profile["instrument"]

    nextyear = profile["agevars"]["nextyear"]
    pets = profile["petsprofile"]["pets"]
    pet_type = profile['petsprofile']['pet_type']
    pet_type_amount = profile['petsprofile']['pet_type_amount']
    petname = profile['petsprofile']['petname']

    interest = sdict["interest"]
    interactions = sdict["interactions"]
    loveBonus = sdict["loveBonus"]
    negloveBonus = sdict["negloveBonus"]
    devbypass = sdict["devbypass"]

    lastlogdatevars = sdict["lastlogdatevars"]
    lastlogdateyear = lastlogdatevars["lastlogdateyear"]
    lastlogdatemonth = lastlogdatevars["lastlogdatemonth"]
    lastlogdateday = lastlogdatevars["lastlogdateday"]
    lastlogdate = lastlogdatevars["lastlogdate"]

    # firsttimes
    # There will be a lot of these coming up
    firsttimes = sdict['firsttimes']

    Indra.firsttime = firsttimes["Indra.firsttime"]
    VideoGames.firsttime = firsttimes["VideoGames.firsttime"]
    Music.firsttime = firsttimes["Music.firsttime"]

    if message == True:
        print ("Game successfully loaded!")
