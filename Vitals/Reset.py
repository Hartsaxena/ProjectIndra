# This Script sets certain variable values at the very Beginning of the Game
# This doesn't set all variables.

os.makedirs(Path.home()/"Documents/ProjectIndra/Saves/", exist_ok=True)
os.makedirs(Path.home()/"Documents/ProjectIndra/Logs/", exist_ok=True)
os.makedirs(Path.home()/"Documents/ProjectIndra/Misc", exist_ok=True)
os.makedirs(Path.home()/"Documents/ProjectIndra/Images", exist_ok=True)
os.makedirs(Path.home()/"Documents/ProjectIndra/Executes/MainExecutes", exist_ok=True)
os.makedirs(Path.home()/"Documents/ProjectIndra/Executes/MiscellaneousExecutes", exist_ok=True)
os.makedirs(Path.home()/"Documents/ProjectIndra/Executes/SystemExecutes", exist_ok=True)


firsttimeIndra = True  # Used for the "Indra" topic
topicdone = False  # Detects if the Topic is finished
topicopinion = True  # True = Good Topic and False = Bad Topic
loveBonus = 0  # Bonus given when Indra is told I love you
negloveBonus = 0  # Bonus given when Indra rejects user
rep = 0 # Used for NoneType Detects
interest = 75  # The interest. This is a key variable
namereject = False  # Tells whether or not the game will Restart if you get certain NameEggs
devbypass = False  # If it's True, it gives the player permissions they normally wouldn't have. # This is for Devoloping and testing code
firstrun = False  # Detects whether or not this is the First Run in the game


# These are paths used to make my job easier

indrafolder = Path(Path.home()/"Documents/ProjectIndra")
logs = Path(Path.home()/"Documents/ProjectIndra/Logs")
intlog = Path(Path.home()/"Documents/ProjectIndra/Logs/Int_log.txt")
namelog = Path(Path.home()/"Documents/ProjectIndra/Logs/Name_log.txt") # NOTE: Unused
vitals = Path(Path.home()/"Documents/ProjectIndra/Vitals")
executes = Path(Path.home()/"Documents/ProjectIndra/Executes")
mainexecutes = Path(Path.home()/"Documents/ProjectIndra/Executes/MainExecutes")
miscexecutes = Path(Path.home()/"Documents/ProjectIndra/Executes/MiscellaneousExecutes")
sysexecutes = Path(Path.home()/"Documents/ProjectIndra/Executes/SystemExecutes")
imindra = Path(Path.home()/"Documents/ProjectIndra/Hello! I'm Indra!")
saves = Path(Path.home()/"Documents/ProjectIndra/Saves")
misc = Path(Path.home()/"Documents/ProjectIndra/Misc")
