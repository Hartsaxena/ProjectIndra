# This is executed when a subject/topic that isn't recognized is chosen
ignoreinteract = True

print("I've never heard of that one...")
sleep(2)
if interest < 20:
    print("Why would you even want to talk about something like that?")
    sleep(2)
    print('weirdo')
    sleep(2)
if interest > 20:
    print("Maybe you could teach me about it sometime?")
    sleep(2)
