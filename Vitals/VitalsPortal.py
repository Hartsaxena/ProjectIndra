# This is a Portal Program that opens other Programs!
# This is mainly to reduce the clutter of "exec(open()) code in the Main Program"

exec(open("ProjectIndra/Vitals/FunctionsReset.py").read())
exec(open("ProjectIndra/Vitals/Imports.py").read())
exec(open("ProjectIndra/Vitals/Reset_Vars.py").read())
exec(open("ProjectIndra/Vitals/Topics_List.py").read())

print("\n")  # Should make 2 empty lines

exec(open("ProjectIndra/Vitals/NewGame.py").read())
