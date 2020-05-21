# This is a Portal Program that opens other Programs!
# This is mainly to reduce the clutter of "exec(open()) code in the Main Program"

HOME_PATH = Path(__file__).parent.absolute()

exec(open(HOME_PATH / "ProjectIndra/Vitals/FunctionsReset.py").read())
exec(open(HOME_PATH / "ProjectIndra/Vitals/Imports.py").read())
exec(open(HOME_PATH / "ProjectIndra/Vitals/Reset_Vars.py").read())
exec(open(HOME_PATH / "ProjectIndra/Vitals/Topics_List.py").read())

print("\n")  # Should make 2 empty lines

exec(open(HOME_PATH / "ProjectIndra/Vitals/NewGame.py").read())
