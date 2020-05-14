# This is executed then "Monika" is the chosen subject


print("You know, that name kind of rings a bell...")
sleep(2)


# This makes the "Monika" window appear
root = tk.Tk()
root.title("Just Monika")
os.makedirs(indrafolder / "Monika's_Room", exist_ok=True)
f = open(indrafolder / "Monika's_Room/monika.chr", 'w')
f.close()
shutil.copy2(indrafolder / "Images/monika.png",
             indrafolder / "Monika's_Room/monika.chr")
monika = tk.Label(root, text="Successfully recovered monika.chr")
monika.pack()
monika = tk.Label(root, text="_J̷̩̍u̶͇͂s̵͚̽t̸͈̕ M̷̪̃ŏ̷͖n̸͕̂i̷̦͝k̵͍̕a̵̛̱_")
monika.pack()

print("Probably nothing!")
