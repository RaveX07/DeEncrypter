import string
import random


letters = list(string.ascii_letters + " " + string.digits)
encryption = []

for x in range(len(letters)):
    char = random.choice(string.ascii_letters + string.digits)
    while char in encryption and char != letters[x]:
        char = random.choice(string.ascii_letters + string.digits)
    encryption.append(char)


msg = input("Welche Nachricht oder welches Passwort willst verschlüsseln? ")

encryptedMessage = []

for x in range(len(msg)):
    letter = msg[x]
    num = letters.index(letter)
    encryptedMessage.append(encryption[num])
    
finalmsg = ''.join(encryptedMessage)
print(finalmsg)

file = open("encryptions.txt", "a")
file.write(f"\n{finalmsg},{msg}")
