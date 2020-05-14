# This Script sets certain variable values at the very Beginning of the Game
# This doesn't set all variables.

os.makedirs(Path.home() / "Documents/ProjectIndra/Saves/", exist_ok=True)
os.makedirs(Path.home() / "Documents/ProjectIndra/Logs/", exist_ok=True)
os.makedirs(Path.home() / "Documents/ProjectIndra/Misc", exist_ok=True)
os.makedirs(Path.home() / "Documents/ProjectIndra/Images", exist_ok=True)
os.makedirs(
    Path.home() / "Documents/ProjectIndra/Executes/MainExecutes", exist_ok=True)
os.makedirs(Path.home(
) / "Documents/ProjectIndra/Executes/MiscellaneousExecutes", exist_ok=True)
os.makedirs(
    Path.home() / "Documents/ProjectIndra/Executes/SystemExecutes", exist_ok=True)

# These variables are used for detecting if the player hasn't gone through a topic before
# Not all used variables are listed here. Some variables are set elsewhere

firsttimeIndra = True  # Used for the "Indra" topic
firsttimeVideoGames = True  # Used for the "Video Games" topic


# Logs the amount of topics or "Loops" the game has gone through. This increasing everytime the WhileReset file is run.
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

indrafolder = Path(Path.home() / "Documents/ProjectIndra")
logs = Path(Path.home() / "Documents/ProjectIndra/Logs")
intlog = Path(Path.home() / "Documents/ProjectIndra/Logs/Int_log.txt")
# NOTE: Unused
namelog = Path(Path.home() / "Documents/ProjectIndra/Logs/Name_log.txt")
vitals = Path(Path.home() / "Documents/ProjectIndra/Vitals")
executes = Path(Path.home() / "Documents/ProjectIndra/Executes")
mainexecutes = Path(
    Path.home() / "Documents/ProjectIndra/Executes/MainExecutes")
miscexecutes = Path(
    Path.home() / "Documents/ProjectIndra/Executes/MiscellaneousExecutes")
sysexecutes = Path(
    Path.home() / "Documents/ProjectIndra/Executes/SystemExecutes")
imindra = Path(Path.home() / "Documents/ProjectIndra/Hello! I'm Indra!")
saves = Path(Path.home() / "Documents/ProjectIndra/Saves")
misc = Path(Path.home() / "Documents/ProjectIndra/Misc")


# This path is used for custom modding only and isn't used in the main game.

custom = Path(Path.home() / "Documents/ProjectIndra/Misc/custom")

# Dev Variables that don't fit anywhere else

currentdate = datetime.now()

no = "no"  or "not really" or "nope" or "n" or "definitely not" or "of course not"

#################################################

cdatetemp = list(currentdate.timetuple())

currentdatelist = [cdatetemp[0], cdatetemp[1], cdatetemp[2]]

#################################################
