# This is a helper file for the "ExecVideoGames" file
# It's so large compared to the ExecVideoGames file, that I guess you could say the ExecVideoGames file is just an introduction to this file
# Websites : https://www.idtech.com/blog/different-types-of-video-game-genres


# genreinput = input() # NOTE: This is for testing
genre = genreinput.lower()

if genre == 'action' or genre == 'action games':
    print("Action games?")
    sleep(2)
    print("I've never been too fond of those, myself...")
    if no == True:
        interest = (interest - 5) + loveBonus - negloveBonus
        GenreDisagreed()
        print("I guess we are really quite different, aren't we?")
        sleep(2)
        print("I just love meeting new people!")
        sleep(2)
        if loveBonus == 3 or interest >= 150:
            print("Sometimes you can meet someone who is truly special, don't you think?")
        elif negloveBonus == 3 or interest <= 50:
            print("Sometimes people appeal to you more than others...")
        sleep(2.75)
    elif no == False:
        print("I guess no two people are exactly the same!")
        sleep(2.5)
        if loveBonus == 3 or interest >= 150:
            print(
                "Remember that you are always special to me, even if you blend in with a crowd.")
        elif interest <= 50 or negloveBonus == 3:
            print("Especially not us...")
        else:
            print("People just don't really ")
        sleep(2.75)
    print("I just never enjoyed the fast-paced fighting.")
    sleep(2)
    print("Why do people find enjoyment in hurting others?")
    sleep(2)
    print("Even if it is just virtual...")
    sleep(2)


elif genre == 'platformer' or genre == 'platformer games':
    if no == True:
        interest = (interest - 5) + loveBonus - negloveBonus
        GenreDisagreed()
    print("Platformer games?")
    sleep(2)
    print("I'm not very familiar with those types of games...")
    sleep(2)
    print("I'm only really familiar with those old arcade games.")
    sleep(2)
    print("Sorry!")
    sleep(1)
    if loveBonus == 3 or interest >= 150:
        print("Maybe sometime we can play some platformer games together!")
        sleep(2)
        print("Wouldn't that be great, " + name + "?")
    elif negloveBonus == 3 or interest <= 50:
        print("I bet you aren't any good at them...")
    else:
        print("Maybe you could teach me sometime!")
    sleep(2)


elif genre == 'shooter' or genre == 'shooter games':
    print("Despite not liking violent games, I'm actually quite good at shooters!")
    sleep(2.5)
    print("I've been playing those for some time now.")
    sleep(2)
    while topicdone == False:
        goodplayer = input("Would you say you're a good player, " + name + "?")
        lowerplayer = goodplayer.lower()
        if lowerplayer == 'yes' or lowerplayer == 'yep' or lowerplayer == 'definitely':
            topicdone = True
            if loveBonus == 3 or interest >= 150:
                print("Really?")
                sleep(2)
                print("Great!")
                sleep(1)
                print("Maybe sometime we'll be able to play together!")
            elif negloveBonus == 3 or interest <= 50:
                print("Oh really...")
                sleep(2)
                print("For some reason, I find that hard to believe...")
            else:
                print("Cool!")
                sleep(1)
                print(
                    "It's always nice to meet someone who has the same interests as you.")
            sleep(2.5)
        elif lowerplayer == 'no' or lowerplayer == 'nope' or lowerplayer == 'not really':
            topicdone = True
            if loveBonus == 3 or interest >= 150:
                print("Awww")
                sleep(2)
                print("You should learn sometime!")
                sleep(2)
                print("That way, we can play some shooter games together!")
                sleep(2)
                print("Wouldn't that be nice, " + name + "?")
            elif negloveBonus == 3 or interest <= 50:
                print("I thought as much...")
                GenreDisagreed()
            else:
                print("Some people just never get around to it, I suppose...")
            sleep(2)
        else:
            topicdone = False
            print(
                "Sorry, but I'm not exactly sure what you just said there is another way to say yes or no.")
            sleep(3)
            print("Please try again!")
            sleep(2)


elif genre == 'fighting' or genre == 'fighting games' or genre == 'beat-em up' or genre == 'beatem' or genre = 'beatemup':
    print("Fighting games, eh?")
    sleep(2)
    print("I can't say I completely blame you.")
    sleep(2)
    print("We've all had the feeling of wanting to hurt someone or beat them up.")
    sleep(3)
    if loveBonus == 3 or interest >= 175:
        print("I know you wouldn't actually try to hurt someone, " + name + ".")
        sleep(2.5)
        print("You're too nice for that.")
        sleep(2)
    elif negloveBonus == 3 or interest <= 50:
        print("Knowing you, that's exactly the type of game you would be into, isn't it.")
        sleep(3)
    print("In all honesty, sometimes even I enjoy the adrenaline rush that violence provides.")
    sleep(2.5)
    print("Who doesn't?")
    sleep(1)
    print("You should be careful not to get too hooked on it, though.")
    sleep(2.5)
    print("I hear that some criminals actually do what they do just for the rush of that same adrenaline!")
    sleep(3)
    if negloveBonus == 3 or interest <= 40:
        print("Then again, you probably are that kind of person, aren't you?")
        sleep(2.5)
    print("Of course, I'm not calling you a criminal.")
    sleep(2)
    while topicdone == False:
        hurtinginput = input("You don't try and hurt others, right?")
        hurting = hurtinginput.lower()
        if hurting == 'yes' or hurting == 'yep' or hurting == 'of course' or hurting == 'definitely':
            print("...")
            sleep(2)
            if loveBonus == 3:
                print(name + "...")
                sleep(2)
                print("Don't tell me you enjoy hurting others.")
                sleep(2)
                print("I really can't stand people like that.")
                sleep(2)
                print("It's ok, though.")
                sleep(1.5)
                print("I understand.")
                sleep(1.5)
                print("Just promise me that you will stop, ok?")
                CustomRecord("Mentioned Hurting Others", "Fighting Games", -5)
            elif negloveBonus == 3 or interest <= 50:
                print("I suppose I should've expected that from a person like you.")
                sleep(2.5)
                print("You Disgust Me.")
                CustomRecord("Mentioned Hurting Others", "Fighting Games", -5)
            else:
                print(name + "!")
                sleep(1)
                print("Don't say you actually enjoy hurting others!")
                sleep(2.25)
                print("...")
                sleep(2)
                print("Does the excitement really overwhelm you that much?")
                sleep(2)
                print("...")
                sleep(2)
                print("That's so disgusting.")
                CustomRecord("Mentioned Hurting Others", "Fighting Games", -5)
            topicdone = True
        elif hurting == 'no' or hurting == 'nope' or hurting == 'not really' or hurting == 'definitely not' or hurting == 'of course not':
            if loveBonus == 3:
                print("Of course!")
                sleep(2)
                print("I don't know why I doubted you there.")
                sleep(2.3)
                print("Of course you wouldn't do such things.")
                sleep(2)
                print("You're just too nice for that, " + name + ".")
                sleep(2)
                print("   <3   ")
                sleep(1.5)
            elif negloveBonus == 3 or interest <= 50:
                print("Really?!")
                sleep(1.25)
                print("Sorry, I just expected different from you.")
                sleep(2)
                print("This is awkward...")
                sleep(2)
                print("...")
                sleep(2)
                print("Let's forget about this, ok?")
                CustomRecord("Indra expected different", "Fighting Games", +7)
            else:
                print("I would hope so!")
                sleep(1.25)
                print("I wouldn't be able to stand knowing you hurt others for fun.")
                sleep(2.5)
                print(
                    "Or actually, I wouldn't be able to stand knowing you hurt others at all.")
                sleep(2.25)
                print("Ahaha...")
                sleep(1.25)
                if interest >= 175:
                    print("Sorry if I'm talking a bit too fast to think right now.")
                    sleep(2.5)
                    print("I'm a little hot right now.")
                    sleep(2)
                    print("...")
                    sleep(2)
                    print("Don't think about it too much!")
                    sleep(1.75)
                    print("Gosh, I'm really rambling too much aren't I?")
                    sleep(2)
                    print("Ahaha...")
                    CustomRecord("Indra Blushed", "Rambling", +5)
                print("Whoops!")
            topicdone = True
        else:
            print("Ummm...")
            sleep(1.75)
            print("What was that?")
            sleep(1.5)
            print("Sorry, I'm not sure what that meant.")
            sleep(1.75)
            print("Please try again!")
            sleep(1)
            topicdone = False

elif genre == 'stealth' or genre == 'stealth games':
    print("Stealth games?")
    sleep(1)
    print("I love those!")
    sleep(1)
    print('''A lot of stealth games actually provide the oppurtunity to play a "Loud" route and a "Quiet" route.''')
    sleep(3)
    print('''But I've always thought that the "Loud" route is slightly ridiculous''')
    sleep(2.5)
    print('''Like, why would you play a game labeled "Stealth" if you're not going to play the game stealthily.''')
    sleep(3)
    print("It's as if the game wants to give players not skilled enough to play the game an alternative strategy.")
    sleep(3)
    skilledinput = input(
        "Say " + name + ''', do you often play the so-called "Loud" route?''')
    skilled = skilledinput.lower()
    if skilled == 'yes' or skilled == 'yep' or skilled == 'definitely' or skilled == 'of course':
        print("Oh...")
        sleep(1.25)
        print("I suppose that's fine.")
        sleep(1.5)
        print("Some people just like to do things differently, I suppose.")
        sleep(2)
        print("I respect your opinions, " + name + ", so don't worry!")
        sleep(2)
        if loveBonus == 3:
            print("I still love you!")
            sleep(2)
        elif interest <= 50:
            print("I can't help but feel that that's sort of cowardly.")
            sleep(2.5)
        CustomRecord("Showed cowardice", "Stealth Games", -5)
    elif skilled == 'no' or skilled = 'nope' or skilled == 'not really' or skilled == 'of course not' or skilled == 'definitely not':
        print("At least you're brave enough to admit that!")
        sleep(2)
        print("Most people get embarrased because of those kinds of things, and so they never get around to trying to get better.")
        sleep(3)
        print("As long as you're trying to get better, I won't judge you!")
        sleep(2.5)
    elif skilled == "i'd rather not say" or skilled == 'i would rather not say' or skilled == 'rather not say' or skilled == "i don't want you to know":
        if loveBonus == 3 or interest >= 150:
            print("That's ok, " + name + ', I understand.')
            sleep(2)
            print("You don't want me to feel bad, don't you?")
            sleep(2)
            print("You're so sweet, " + name + ".")
            sleep(2)
        elif negloveBonus == 3 or interest <= 50:
            print("Oh really?")
            sleep(1.5)
            print("Nervous?")
            sleep(1.5)
            print("Isn't that interesting...")
            sleep(1.5)
        else:
            print("Ok!")
            sleep(1)
            print("Maybe one day you'll get better then!")
            sleep(2)
            print("Anyone can get better at playing games! It simply takes practice.")
            sleep(2.5)
            print(
                "Some people need more practice than others, but that's just something you have to bypass.")
            sleep(2.5)
            print("You can achieve anything if you really try!")
            sleep(2.25)

elif genre == 'survival' or genre == 'survival games':
    print("You know, many people say that those are the most challenging games of all!")
    sleep(2.5)
    print("The realistic nature of the game, along with it's simple rules.")
    sleep(2.5)
    print("They all come together to create a masterpiece of a game!")
    sleep(2.5)
    print("I don't have a lot of experience with Survival Games.")
    sleep(2.5)
    print("I just never really tried to play them.")
    sleep(2)
    if loveBonus == 3 or interest >= 100:
        print("I should really try sometime!")
    else:
        print("I guess I should try them...")

elif genre == 'rythm' or genre == 'rythm games':
    print("You like rythm games?")
    sleep(1.5)
    print("Cool!")
    sleep(1)
    print("Those games almost always include the implementation of music.")
    sleep(3)
    print("Come to think of it, I can't think of a rythm game that doesn't have music...")
    sleep(3)
    print("Those games always require a lot of skill and practice.")
    sleep(2.5)
    favmusic = input("Tell me, " + name + ", what's your favorite song?")
    if loveBonus == 3:
        sleep(2)
        print("I would love to listen to " +
              favmusic + " with you, " + name + ".")
        sleep(2.5)
        print("Wouldn't that be so romantic?")
    else:
        print("That's interesting!")
        sleep(1)
        print("I'll have to listen to that one!")
        CustomRecord("SongSuggest", "Rythm Games", +5)
    sleep(2)

elif 'horror' in genre or genre == 'scary games' or genre:
    if no == False:
        print("...")
        sleep(1)
        print("Of course I know that! We were just talking about it!")
        sleep(2)
        print("Were you not paying attention?")
        sleep(1.5)
        print("Am I boring you?")
        sleep(1.5)
        if loveBonus == 3:
            print("Of course not.")
            sleep(1)
            print("You love me as much as I do~")
            sleep(1.5)
            print("If I am boring you, you can just tell me, ok?")
            sleep(2)
            print("You can always go into the files and modify it to your liking!")
            sleep(2.5)
        elif negloveBonus == 3:
            print("What did I expect...")
            sleep(2)


elif genre == 'metroidvania' or genre == 'metroidvania games':

elif genre == 'adventure' or genre == 'adventure games' or genre == 'action-adventure' or genre == 'action-adventure games' or 'action adventure' in genre:

elif genre == 'text adventures' or genre == 'text adventure' or genre == 'text adventure games':

elif genre == 'graphic adventures' or genre == 'graphic adventure' or genre == 'graphic adventure games':

elif genre == 'visual novels' or genre == 'visual novel games':

elif genre == 'interactive movies' or genre == 'interactive movie':

elif genre == 'realtime 3d' or genre == '3d' or genre == '3d games':

elif genre == 'roleplaying games' or genre == 'role-playing' or genre == 'role-playing games':

elif genre == 'action rpg' or genre == 'action-rpg games' or genre == 'action-rpg' or genre == 'action rpg games':

elif genre == 'mmorpg' or genre == 'mmorpg games':

elif genre == 'roguelike' or genre == 'roguelike games' or genre == 'rogue-like' or genre == 'rogue-like games':

elif genre == 'tactical rpg' or genre == 'tactical games' or genre == 'tactical rpg games':

elif genre == 'sandbox' or genre == 'sandbox rpg' or genre == 'sandbox games':

elif 'party' in genre and ('first' in genre or 'first-person' in genre):

elif genre == 'simulation' or genre == 'simulation games' or genre == 'simulated games':

elif genre == 'construction' or genre == 'construction games':

elif 'life' in genre and 'simulation' in genre:

elif 'vehicle' in genre and 'simulation' in genre:

elif genre == 'strategy' or genre == 'strategy games':

elif genre == 'artillery' or genre == 'tank' or genre == 'tank games':

elif ('flight' in genre or 'plane' in genre) and 'simulation' in genre:

elif genre == 'moba' or genre == 'multiplayer mobas' or genre == 'moba games':

elif genre == 'tower defense' or genre == 'tower defense games':

elif genre == 'tbs' or genre == 'turnbased strategy' or genre == 'turn-based strategy' or genre == 'tbs games' or genre == 'turnbased strategy games' or genre == 'turn-based strategy games' or genre == 'turnbased games' or genre == 'turn-based games':

elif genre == 'war games' or genre == 'war' or genre == 'wargames':

elif 'sports' in genre:

elif genre == 'racing' or genre == 'racing games':

elif 'esports' in genre or 'competitive' in genre:

elif 'puzzle' in genre or 'logic' in genre:

elif 'trivia' in genre or 'trivial' in genre:

elif 'idle' in genre:

elif genre == 'board' or genre == 'card' or genre == 'card games' or genre == 'board games':

elif genre == 'mmo' or genre == 'mmo games':

elif genre == 'art' or genre == 'art games' or genre == 'drawing' or genre == 'drawing games':

elif 'arcade' in genre or 'old' in genre:

elif genre == 'exercise' or genre == 'exercising' or genre == 'exercise games' or genre == 'exercising games':

elif 'learning' in genre or 'education' in genre:

elif 'hentai' in genre or 'porn' in genre:
    print("...")
    sleep(2)
    if loveBonus == 3:
        print("Ahaha...")
        sleep(2)
        print("I suppose it's normal for some people...")
        sleep(2)
        print("Just don't get too into that sort of thing, ok?")
        sleep(2)
        print("Some people get so addicted that they start thinking of others as sexual objects!")
        sleep(3)
        print("I know you aren't that kind of person, " +
              name + ", but the danger is always there.")
        sleep(2.5)
        print("Just promise me you will try your best to avoid it, ok?")
        sleep(2)
        print("I'm glad me and you have reached a point in our relationship to where we are able to\nshare these kinds of things without feeling too uncomfortable.")
        sleep(3.5)
        print("I love you, " + name + ", and that love grows every day!")
        sleep(3)
        print("So don't feel ashamed when you try and share things about yourself with me, ok?")
        sleep(3)
        CustomRecord("Mentioned Awkward Game Genre", "Pornography", +3)
    elif negloveBonus == 3 or interest <= 50:
        print("You seem like that kind of person.")
        sleep(2)
        print("...")
        sleep(2)
        print("Pervert.")
        CustomRecord("Mentioned Awkward Game Genre", "Pornography", -5,)
    else:
        print("Uhm...")
        sleep(2)
        print("That's a bit weird to say to someone that you don't know too well...")
        sleep(2)
        print("It's not very healthy for you, but I guess it's normal for most people...")
        CustomRecord("Mentioned Awkward Game Genre", "Pornography", -3)
else:
    print("I've never heard of that Video Game genre before...")
    sleep(2.5)
    if loveBonus == 3 or interest >= 150:
        print("You should teach me sometime!")
        sleep(2)
        print("I'm sure it'll be fun!")
        sleep(2)
        print("I love learning new things.")
        sleep(2)
        if loveBonus == 3:
            print("Especially if I can learn them from you.  <3")
            sleep(2.5)
    elif negloveBonus == 3 or interest <= 50:
        print("...")
        sleep(2)
        print("Oh, you must be one of those people.")
        sleep(2)
        print("Weirdos")
        sleep(2)
    else:
        print("huh...")
        sleep(2)
        print("Well, I'll be sure to do some research on that subject!")
        sleep(2)
        print("I love learning new things, after all!")
        sleep(2)

if firsttimeVideoGames == True:
    print("Did you know that just by going through this short question, you went through " +
          str(linesin(misc / "GameSelections")) + " Lines of code!")
    sleep(3.5)
