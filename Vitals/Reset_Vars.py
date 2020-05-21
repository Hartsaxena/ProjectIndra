# This Script sets certain variable values at the very Beginning of the Game
# This doesn't set all variables.

os.makedirs(HOME_PATH / "ProjectIndra/Saves/", exist_ok=True)
os.makedirs(HOME_PATH / "ProjectIndra/Logs/", exist_ok=True)
os.makedirs(HOME_PATH / "ProjectIndra/Misc", exist_ok=True)
os.makedirs(HOME_PATH / "ProjectIndra/Images", exist_ok=True)
os.makedirs(
    HOME_PATH / "ProjectIndra/Executes/MainExecutes", exist_ok=True)
os.makedirs(Path.home(
) / "Documents/ProjectIndra/Executes/MiscellaneousExecutes", exist_ok=True)
os.makedirs(
    HOME_PATH / "ProjectIndra/Executes/SystemExecutes", exist_ok=True)

# These variables are used for detecting if the player hasn't gone through a topic before
# Not all used variables are listed here. Some variables are set elsewhere

firsttimeIndra = True  # Used for the "Indra" topic
firsttimeVideoGames = True  # Used for the "Video Games" topic

# Logs the amount of topics or "Loops" the game has gone through. This increasing everytime the WhileReset file is run.

age = None
# Doesn't make sense, but it's just a filler. This allows for the Save function to work
birthdate = date(1000, 1, 1)
# The Game treats date(1000, 1, 1) as Null basically

gender = None
pets = None
nextyear = None
interactions = 0
topicdone = False  # Detects if the Topic is finished
topicopinion = True  # True = Good Topic and False = Bad Topic
loveBonus = 0  # Bonus given when Indra is told I love you
negloveBonus = 0  # Bonus given when Indra rejects user
rep = 0  # Used for NoneType Detects
interest = 75  # The interest. This is a key variable
namereject = False  # Tells whether or not the game will Restart if you get certain NameEggs
devbypass = False  # If it's True, it gives the player permissions they normally wouldn't have. # This is for Devoloping and testing code
firstrun = False  # Detects whether or not this is the First Run in the game
ignoreinteract = False  # Some Topics don't need to be logged as interactions


# These are paths used to make my job easier

indrafolder = Path(HOME_PATH / "ProjectIndra")
logs = Path(indrafolder / "Logs")
intlog = Path(indrafolder / "Logs/Int_log.txt")
namelog = Path(indrafolder / "Logs/Name_log.txt") # NOTE: Unused
vitals = Path(indrafolder / "Vitals")
executes = Path(indrafolder / "Executes")
mainexecutes = Path(indrafolder / "Executes/MainExecutes")
miscexecutes = Path(indrafolder / "Executes/MiscellaneousExecutes")
sysexecutes = Path(indrafolder / "Executes/SystemExecutes")
imindra = Path(indrafolder / "Hello! I'm Indra!")
saves = Path(indrafolder / "Saves")
misc = Path(indrafolder / "Misc")
datafiles = Path(indrafolder / "Data_Files")


# This path is used for custom modding only and isn't used in the main game.

custom = Path(indrafolder / "Misc/custom")

# Dev Variables that don't fit anywhere else

currentdate = datetime.now()

no = "no" or "not really" or "nope" or "n" or "definitely not" or "of course not"

#################################################

cdatetemp = list(currentdate.timetuple())
currentdate = date(currentdate.year, currentdate.month, currentdate.day)

currentdatelist = [cdatetemp[0], cdatetemp[1], cdatetemp[2]]

# Helps detect if a word is a cussword
# Best if you don't look into that file...
f = open(datafiles / "cusswords", 'r')
cusswordsread = f.readlines()
f.close()
cusswords = []
for line in cusswordsread:
    cusswords.append(line.rstrip('\n'))

#################################################
