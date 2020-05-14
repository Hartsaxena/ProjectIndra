# This is executed the player asks Indra a Suggestion through the subject "I don't know" or "I don't care"
ignoreinteract = True

print("ok!")
sleep(1)
print("How about I give you a suggestion?")
sleep(1.5)
print("We should talk about...")
sleep(2)
# Refer to topic list above the supreme while loop
topicSuggestion = random.randint(0, len(topicsList) - 1)
print(topicsList[topicSuggestion] + "!")
sleep(1.5)
print("Next time I ask you about what you want to talk about, just type that in!")
sleep(3)
