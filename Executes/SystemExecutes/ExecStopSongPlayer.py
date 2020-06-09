# This stops any music if it is playing

if mixer.music.get_busy() == 1:  # Detects if mixer.music is playing
    mixer.music.stop()
    print("The music has stopped!")
    sleep(1.5)
    print("Tell me if you want to play some music again, ok?")
    sleep(2)
    if loveBonus == 3 or interest >= 100:
        print("I would love to listen to some more music with you!")
        sleep(2.5)
    elif negloveBonus == 3 or interest <= 50:
        print("It was ok, I guess.")
        sleep(1.5)

else:
    print("Sorry, but I don't think any music is currently playing.")
    sleep(2.5)
    print("I can't control if you hear music from anything other than me.")
    sleep(2.5)
    print("Are you sure you aren't hearing music from another computer?")
    sleep(2)
