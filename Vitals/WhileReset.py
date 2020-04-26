# This resets variables every time the Supreme While Loop is reset
# If you tried to mess around with this code, you'll find results/errors on the second time the While Loop is executed
# Messing with this code will generally not break anything on the first topic that Indra talks About
Save()
yesnorep = True

repeating = 0

topicdone = False


if loveBonus == 3 and interest <= 40:
    print("Hey, "+name+".")
    sleep(1.5)
    print("Recently I can't help but feel that all my love and affection for you is being ignored")
    sleep(2)
    print("As if you didn't care about me.")
    sleep(1.5)
    loveBonus = 0
    interest = interest-5
    ChangeMind()
