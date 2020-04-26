# This detects if a previous state exists and recovers the save if it exists.


if os.path.exists(indrafolder/".Saves/.save.txt") == True:


if os.path.exists(indrafolder/".Saves/.save.txt") == False:
    os.makedirs(indrafolder/".Saves")
    save = open(indrafolder/".Saves/.saves.txt", 'w')
    save.write("")
