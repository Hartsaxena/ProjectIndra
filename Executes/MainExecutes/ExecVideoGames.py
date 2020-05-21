# This is executed when "Video Games" is the chosen subject
# This is a rather passive topic, meaning it doesn't change a lot of variables


print("Video Games?")
sleep(2)
print("Sorry, but I don't really have a lot of experience with Video Games...")
sleep(3)
print("I've played a few, though!")
sleep(2)
print("I'm really interested in the Horror genre!")
sleep(2)
print("I don't really like those cliche Horror games that rely on cheap scares,\nbut there are some really unique ones out there!")
sleep(3)
yesno = input(f"Do you like playing Horror games, {name}?")
if Yes(yesno.lower()) == True or Like(yesno) == True:
    no = False
    print("Me too!")
    sleep(1)
    print("I used to be really scared of them, but after some time, I kinda just got numb.")
    sleep(3)
    nomessage = "Even if you enjoy Horror games, you must enjoy other genres as well!"
if No(yesno.lower()) == True or Dislike(yesno) == True:
    no = True
    if loveBonus == 3:
        print("That's ok.")
        sleep(2)
        print("It's not for everyone, I suppose")
    elif negloveBonus == 3 or interest <= 50:
        print("It's ok to be scared, " + name + ".")
        sleep(2)
        print("Not everyone takes it too well.")
    else:
        print("No worries.")
        sleep(2)
        print("We're all different when it comes to these things.")
    sleep(2.5)
    nomessage = "I'm sure you're into different types of video games, though!"
print(nomessage)
sleep(2.75)
genreinput = input("What genre of Video Games do you prefer? ")
exec(open(indrafolder / "Misc/GameSelections.py").read())
