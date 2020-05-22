# These are technically supposed to be part of the FunctionsReset.py file, but since the more variables that are added to the game, the longer these two functions will get, I decided to move these to a seperate file


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
            "petsprofile":{
                "pets": pets,
                "pet_type": pet_type,
                "petname": petname,
                "pet_type_amount": pet_type_amount,
            },
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
            "firsttimeIndra": firsttimeIndra,
            "firsttimeVideoGames": firsttimeVideoGames,
        },
    }
    json.dump(savedict, savefile, indent=1)
    savefile.close()
    if message == True:
        print ("The game has been Saved!") # Unused
        sleep(1.5)


def Load():
    ''' Loads the Savefile at the beginning of each game session. '''

    ''' These simply allow me to change the variables from the function.
    I know global variables are not recommended, but I decided "Screw that!" and went along with it anyways'''

    global age
    global birthdate
    global devbypass
    global firsttimeIndra
    global firsttimeVideoGames
    global gender
    global interactions
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

    name = sdict["name"]
    gender = sdict["profile"]["gender"]
    age = sdict["profile"]["agevars"]["age"]
    birthdate = date(
        sdict['profile']['agevars']['birthdate']["year"], sdict["profile"]["agevars"]["birthdate"]["month"], sdict["profile"]["agevars"]["birthdate"]["day"]
        )

    nextyear = sdict["profile"]["agevars"]["nextyear"]
    pets = sdict["profile"]["petsprofile"]["pets"]
    pet_type = sdict['profile']['petsprofile']['pet_type']
    pet_type_amount = sdict['profile']['petsprofile']['pet_type_amount']
    petname  = sdict['profile']['petsprofile']['petname']

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
