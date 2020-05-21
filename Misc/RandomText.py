# Creates a bunch of nonsense text in the firstrun files
# "I wonder if the firstrun file contains encoded secrets?"
# Well now you know the answer - It's literally randomly generated text
# Bummer, isn't it?
#                - Indra

alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
         'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ',', '.', '/', '[', ']', '{', '}', '-', '=', '_', '+', '`', '~', '\n', '|']
print("Creating firstrun...")
f = open(indrafolder / "firstrun", 'w')
for i in range(1000000):
    character = random.randint(1, len(alpha) - 1)
    f.write(alpha[character])
f.close()
sleep(2)
