file = open("encryptions.txt", "r")

encs = []
msgs = []

for x in file.readlines():
    komma = int(x.find(","))
    komma1 = komma + 1
    
    encs.append(x[:komma])
    msgs.append(x[komma1:])

enc = input("Welche Nachricht willst du entschlüsseln? ")
num = encs.index(enc)

msg = msgs[num]

print(msg)
