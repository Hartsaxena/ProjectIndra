from pathlib import Path
import time
import random
alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
         'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ',', '.', '/', '[', ']', '{', '}', '-', '=', '_', '+', '`', '~', '\n', '|']
print("Creating firstrun...")
f = open(Path.home()/"Documents/ProjectIndra/firstrun", 'w')
for x in range(5):
    for i in range(1000000):
        character = random.randint(1, len(alpha)-1)
        f.write(alpha[character])
    print(str(x)+"/5")
f.close()
time.sleep(2)
print("Done!")
