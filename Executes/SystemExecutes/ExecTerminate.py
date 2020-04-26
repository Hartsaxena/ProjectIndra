# This is executed when the Player tells Indra to terminate the Program through "terminate" as the chosen subject.


if interest >= 60:
    if loveBonus == 3:
        if name.lower() == 'james' or name.lower() == 'hartsaxena':
            RecordedTerminate("Until next time, "+name+"!")
        else:
            RecordedTerminate("Love you, "+name+'!  c;')
    else:
        if name.lower() == 'james' or name.lower() == 'hartsaxena':
            RecordedTerminate("Until next time, "+name+"!")
        else:
            RecordedTerminate("OK! See you next time, "+name+"!")
if interest < 40:
    if name.lower() == 'james' or name.lower() == 'hartsaxena':
        RecordedTerminate("Until next time, "+name+"!")
    else:
        RecordedTerminate("Whatever.")
