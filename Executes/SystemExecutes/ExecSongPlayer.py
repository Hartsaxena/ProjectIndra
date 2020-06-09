# This plays some custom music
#
# to add your own custom music, follow these steps:
#
# 1. Create a folder in the game directory called "custom_music"
#
# 2. Put your songs (as mp3 files) into the custom_music folder
#
# 3. When Indra asks you what topic you want to talk about, type in "Play a song"
#
# 4. Pick which song you want to play
#
# 5. Done!
#
#         - Indra
#

ignoreinteract = True
custom_music_path = Path(indrafolder / "custom_music")


def custom_musicInstructions():  # Simple function that prevents too much repitition
    os.makedirs(custom_music_path, exist_ok=True)
    print("First, create a folder in the game directory called \"custom_music\" if\nit doesn't already exist.")
    sleep(3)
    print("I've already created one for you automatically!")
    sleep(2.5)
    print("Then, put your mp3 songs into the custom_music folder.")
    sleep(2.5)
    print("Finally, ask me to play a song again!")
    sleep(2.5)
    print("Simple, isn't it?")
    sleep(2)


# Finds if the custom_music folder exists
if os.path.exists(custom_music_path) == False:
    print("Sorry, but you haven't added a custom_music folder in the game directory yet.")
    sleep(2.5)
    if Music.firsttime == False:
        while topicdone == False:
            yesno = input(f"Do you still remember how to add custom music, {name}?")
            if Yes(yesno) == True:
                topicdone = True
                print("Good!")
                sleep(1)
                print(
                    "Then follow the instructions I told you and ask me to play a song again, ok?")
                sleep(3)
                if loveBonus == 3 or interest >= 130:
                    print("I can't wait to listen to your favorite music together.")
                    sleep(2)
            elif No(yesno) == True:
                topicdone = True
                print("Ok then!")
                sleep(1.25)
                print("I suppose I'll just tell you again then!")
                sleep(2)
                custom_musicInstructions()
                if loveBonus == 3 or interest >= 130:
                    print("I can't wait to listen to your favorite songs together!")
                    sleep(2.5)
                elif negloveBonus == 3 or interest <= 50:
                    print("The songs better be good.")
                    sleep(2)
            else:
                print("Sorry, but I don't understand what you just said.")
                sleep(2)
                print("Please try again!")
                sleep(1.25)
    else:
        print("Don't worry!")
        sleep(1.25)
        print("Doing so is pretty easy!")
        sleep(1.25)
        custom_musicInstructions()
        print("I'll be waiting to listen to some music then!")
        sleep(2)

else:  # Checks the custom_music folder for new music
    print("Checking for music...", end="\n\n")
    sleep(1.5)
    raw_music_files = os.listdir(custom_music_path)
    valid_music = []
    nonvalid_music = []
    for song in raw_music_files:
        if song.endswith(".mp3"):
            # Checks if the song is a folder (if for some reason it is)
            if os.path.isdir(custom_music_path / song):
                nonvalid_music.append(song)
            else:
                valid_music.append(song.rstrip('.mp3'))
        else:
            nonvalid_music.append(song)
    if len(nonvalid_music) > 0:  # Checks if their are non-mp3 files
        print("Sorry, but the following files couldn't be loaded in:")
        for song in nonvalid_music:
            print(song)
        print(end="\n\n")

    if len(valid_music) == 0:
        print("Sorry, but I couldn't find any songs in the custom_music folder.")
        sleep(2.5)
        print("Please make sure you followed all instructions correctly.")
        sleep(2)
        print("I'll be waiting!")
        sleep(1.25)

    else:
        print("Valid Songs:")
        numofsong = 1
        for song in valid_music:
            print(f"{numofsong}. {song}")
            numofsong = numofsong + 1
        topicdone = False
        while topicdone == False:
            print()
            print("Which song would you like to play?\n(answer with the number on the left of the song).")
            print("Type \"nevermind\" if you change your mind!")
            whichsong = (input()).lower()

            if whichsong[len(whichsong) - 1] == '.':
                whichsong = whichsong.rstrip(".")

            if whichsong == 'nevermind':
                topicdone = True
                print("Ok!")
                sleep(1)
                print("If you ever want to play some music, just ask me, ok?")
                sleep(2)

            else:
                try:
                    whichsong = int(whichsong)
                except ValueError:
                    print("Sorry, but that's not a valid integer.")
                    sleep(1.5)
                    print("Please try again!")
                    sleep(1.5)
                else:
                    try:
                        mixer.music.stop()
                        mixer.music.load(str(custom_music_path) + "/" + str(valid_music[whichsong - 1]) + ".mp3")
                        mixer.music.play()
                    except IndexError:
                        print("Sorry, but that's not a number that's listed.")
                        sleep(2)
                        print("Please try again!")
                        sleep(1.25)
                    else:
                        topicdone = True
                        print("Currently playing music!")
