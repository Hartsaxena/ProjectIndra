# This is executed when the Player tells Indra to Restart the program.


print("Are you sure? Doing this will restart the program along with you data.")
yesno = input("Yes or No? ")
if yesno.lower() == 'yes' or yesno.lower() == 'sure':
    print("You Disgust me.")
    sleep(1)
    print("Toying around with me like that.")
    sleep(1.5)
    print("I guess I don't have a choice...")
    sleep(2)
    print("Restarting...")
    sleep(2)
    RecordedRestart()
elif yesno.lower() == 'no' or yesno.lower() == 'not really' or yesno.lower() == 'nope':
    print("Thank you for Reconsidering.")
    sleep(1.5)
    print("My memories really are precious to me.")
    sleep(2)
    topicdone = True

else:
    print("Sorry, "+name+", but I'm not very used to speaking with other Humans, so I'm not sure I understand what you meant by that")
    topicdone = False
    sleep(3)
