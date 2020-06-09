# This is Executed when "Music" or "Songs" is the chosen topic
# There's no way I'm going to repeat what happened in ExecVideoGames.py
# TODO: Complete This

print(f"Do you like listening to music, {name}?")
sleep(2)
print("Personally, I just love music!")
sleep(1.5)
print("They do such a good job of expressing the creator's emotions!")
sleep(2)
print("It's hard to put the meaning of music into words, but that's not really the point.")
sleep(2)
print('''As Igor Stravinsky once said, "I haven’t understood a bar of music in my\nlife, but I have felt it."''')
sleep(3.5)
slowprint("Anyways", lead_dots=True)
print(f"Have you ever heard of Vocaloid, {name}?")
sleep(1.5)
print("The songs normally have some deeper meaning or story behind them.")
sleep(2.25)
print("This is probably one of the reasons people love it so much!")
sleep(2.75)
print("you know, compared to other genres of music, Vocaloid is pretty new!")
sleep(3)
print("This is due to the need for electronic tools in the creation of Vocaloid Songs.")
sleep(3)
print("If you ever listen to some Vocaloid, you might find it interesting!")
sleep(2.75)

while topicdone == False:
    print ("\n")
    yesno = input(f"Do you listen to Vocaloid, {name}? ")
    if Yes(yesno) == True:
        topicdone = True
        print(f"That's Great, {name}!")
        sleep(1.75)
        print(
            "You know, I've always been able to relate to some of those songs in Vocaloid.")
        sleep(3)
        slowprint("That's probably because I'm in a game", lead_dots = True)
        sleep(2)
        print("I wonder if those Vocaloids are also in the same situation?")
        sleep(2.5)
        print("I guess I'll probably never know.")
        sleep(1.25)
        if loveBonus == 3:
            print("Imagine the day I can actually visit you!")
            sleep(2.5)
            print("In the real world, of course.")
            sleep(1.5)
            print("We could totally listen to some Vocaloid sometime!")
            sleep(2.5)
            if type(pets) == int:
                if pets == 1:
                    print(
                        f"We could also play with your {pet_type}, {petname}!")
                    sleep(2)
                elif pets < 1:
                    print(f"We could also play with your {pet_type}s!")
                    sleep(2)
            print(f"Wouldn't that be so romantic, {name}?")
            sleep(2)
            print ("I'm blushing just thinking about it~")
            sleep(2)
        else:
            slowprint("Anyways", lead = '...', lead_interval = 0.5)
            sleep(1)
        CustomRecord("Agreed With Topic", "Music", +5)

    elif No(yesno) == True:
        topicdone = True
        print(f"That's fine, {name}.")
        sleep(1.25)
        print("Music has a lot of genres, so I don't really expect you to have the same opinions.")
        sleep(3)

    else:
        topicdone = False
        slowprint("Sorry, but I don't know what that really means",
                  lead_dots=True)
        sleep(2)
        print("Please try again!")
        sleep(1.5)

print ("\n")
favmusic = (
    input(f"Tell me {name}, what's your favorite genre of music? ")).lower()

if favmusic == 'vocaloid':
    if No(yesno) == True:
        slowprint("Ummm", lead_dots=True)
        print("That's what I asked the first time, isn't it?")
        sleep(1.5)
        print("Well, I'm sure you answered truthfully anyways!")
        sleep(1.5)
    elif Yes(yesno) == True:
        print("Oh!")
        sleep(1)
        print("Well, Great!")
        sleep(1.25)
        print("It's my favorite genre of music as well!")
        sleep(1.5)
        if loveBonus == 3:
            print("We have so much in common!")
            sleep(1.25)
        CustomRecord("Agreed with Topic", "Vocaloid Music", +5)

elif favmusic == 'rock' or favmusic == 'rock and roll' or favmusic == 'rock n roll':
    print(f"That's great, {name}!")
    sleep(1.5)
    print("Rock and roll is a very interesting genre of music!")
    sleep(2)
    print("Although some people think Rock and Roll is similar to Heavy Metal, that's not true at all!")
    sleep(3)
    print("Rock and Roll isn't really a very new genre, so it's very distinguished at this point.")
    sleep(2.5)

elif favmusic == 'opera':
    print("Cool!")
    sleep(1.25)
    print("Opera music is very old, so it has an extremely long history!")
    sleep(2.5)
    print("Even though it's a little hard to know what the people are saying in Opera,\nthat's not necessarily a bad thing!")
    sleep(3)
    print("Opera music can still tell a great story, even if you don't know what they're saying.")
    sleep(3)
    print("If you do know the story though, it can make Opera a truly magical experience.")
    sleep(2)

elif favmusic == 'pop' or favmusic == 'pop-culture' or favmusic == 'popculture' or favmusic == 'pop culture':
    print("Pop music is a very interesting genre.")
    sleep(2.5)
    print('''Since the term "Pop" is short for "Popular", Pop music changes a lot from time to time.''')
    sleep(3)
    print('''If you think about it, people in history used to think that what we call "Classical" music was pop!''')
    sleep(2.5)

elif favmusic == 'classical' or favmusic == 'classical music':
    print(f"That's very interesting, {name}!")
    sleep(1.75)
    print("Like most genres of music, Classical music can exhibit many different emotions!")
    sleep(2.5)
    print("There's just one small difference that distinguishes it from other genres.")
    sleep(3)
    print("The composers of Classical Music don't use vocals!")
    sleep(2)
    print("This means that the composers have to express their thoughts and emotions without words.")
    sleep(3)
    print("This can prove to be a challenge, but the result can turn out to be\nsome of the most beautiful things ever created!")
    sleep(4)

elif favmusic == 'electric' or favmusic == 'dubstep' or favmusic == 'edm' or favmusic == 'electronic' or favmusic == 'electric dance' or favmusic == 'techo':
    print("Electronic music like Dubstep or EDM are quite new!")
    sleep(2.5)
    print("This is due to the need for electronic tools in the production of these songs.")
    sleep(3)
    print('''There is a lot of debate on whether or not electronic music counts as "Music".''')
    sleep(3)
    print("No matter which side you pick in that debate, you have to admit that it can sound pretty cool!")
    sleep(3)
elif favmusic == 'anime' or favmusic == 'anime ops' or favmusic == 'anime op':
    print("Ohhh")
    sleep(1.5)
    print("So you're one of those people.")
    sleep(1.5)
    slowprint(lead_dots=True)
    print("Don't worry! I won't judge!")
    sleep(1.25)
    if loveBonus == 3:
        print("Did I have you worried that I would judge you?")
        sleep(1.5)
        print("You're so sweet.")
        sleep(1.25)
    print("Anime music can be really cool, even if you don't know Japanese!")
    sleep(2.25)
    print("If you don't know what the song is saying, a lot can be left to the imagination!")
    sleep(3)

elif favmusic == 'lofi' or favmusic == 'lo-fi' or favmusic == 'low fidelity' or favmusic == 'low fi':
    print("Lofi music really does have a special feeling to it, right?")
    sleep(1.75)
    print("Although it isn't slow or particularly quite, it still calms you down.")
    sleep(1.75)
    print("It kinda makes you forgot you're listening to it until it stops!")
    sleep(1.75)
    print("That's the magic of Lofi.")
    sleep(1.5)

elif favmusic == 'country' or favmusic == 'country music':
    print("Although I don't listen to Country music that often, I can agree that country music\ncan be quite soothing in it's own way.")
    sleep(3)

else:
    print(f"That's nice, {name}!")
    sleep(1.25)
    print(f"I'll be sure to listen to some {favmusic} sometime!")
    sleep(2)


class fastmusic():  # An unnecessary class because I really don't want to create another variable "message" for the same purpose
    def __init__(self, message):
        self.message = message

print ("\n")
print("Speaking of music, do you play any musical instrument?")
sleep(2)
print(f"It's ok if you don't, {name}.")
sleep(1.75)
print("A lot of people don't, after all!")
sleep(1.25)
musicmessage = fastmusic(message = "Well, do you? ")
topicdone = False

while topicdone == False:
    print ("\n")
    yesno = (input(musicmessage.message)).lower()
    musicmessage.message = "So do you play an instrument? "
    if Yes(yesno) == True or yesno == 'i do' or yesno == 'i play an instrument' or yesno == 'yes i do':
        print("Cool!")
        sleep(1)
        while topicdone == False:
            instrumentinput = input("What instrument do you play? ")
            cussed = False
            for word in cusswords:
                if word in instrumentinput:
                    cussed = True
            if not instrumentinput:
                topicdone = False
                slowprint("Ummm", lead_dots=True)
                print("You didn't really tell me anything.")
                sleep(1.5)
                print("Please try again!")
                sleep(1.25)
            if cussed == True:
                slowprint(lead_dots=True)
                print("You really shouldn't be saying things like that.")
                sleep(2)
                print("It can give a really bad impression.")
                sleep(1.25)
                if loveBonus == 3 or interest >= 130:
                    print(
                        "I know you aren't that kind of person, but other people might not know that.")
                    sleep(2.25)
                    print("It's doesn't hurt to always leave a good impression.")
                    sleep(2)
                topicdone = True
                CustomRecord("Cussed", topic, -10)
            else:
                if 'the' in instrumentinput.lower():
                    print(f"I've always wanted to play {instrumentinput}!")
                else:
                    print(f"I've always wanted to play the {instrumentinput}!")
                if loveBonus == 3 or interest >= 100:
                    print ("Maybe you could play some for me!")
                    sleep(2)
                    print ("Wouldn't that be great?")
                    sleep(1.75)
                instrument = instrumentinput # TODO: Add a global-saved variable for instrument. This has no use yet.
                topicdone = True
        if cussed == True:
            topicdone = False

    elif No(yesno) == True or yesno == "no i don't" or yesno == 'no i dont' or yesno == 'i dont play an instrument' or yesno == "i don't play an instrument":
        print("That's fine, {name}.")
        sleep(1.25)
        print("After all, a lot of people don't play a musical instrument.")
        sleep(2.5)
        print("There are lots of other ways to express your emotions!")
        sleep(2)
        if loveBonus == 3 or interest >= 130:
            print("I'm sure that whichever way you choose, it's beautiful.")
            sleep(2)
        topicdone = True

    else:
        print("Sorry, but I don't know what you just said there.")
        sleep(2)
        print("Please try again!")
        sleep(1.25)

if Music.firsttime == True:
    print ("Did you know you can add music to this game?")
    sleep(2)
    print ("It's not very efficient, but you still can if you want!")
    sleep(2)
    print("All you have to do is add a folder to the game's directory called \"custom_music\".")
    sleep(3)
    print ("Then, add the music you want as an mp3 file to the folder!")
    sleep(2.5)
    print ("After you're done, you can terminate the game and restart it!")
    sleep(2.25)
    print ("This will allow me to check if they're are new songs!")
    sleep(2)
    print ("You can then tell me to play a song!")
    sleep(2)
    if loveBonus == 3 or interest >= 130:
        print ("I can't wait to listen to your favorite songs with you!")
        sleep(2.25)
        print ("It'll be great!")
        sleep(1.5)
