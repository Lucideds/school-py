x = 0
fulltranscript = []
trans1 = open("txt/transcript1.txt","r")
trans2 = open("txt/transcript2.txt","r")
tran1 = trans1.readlines()
tran2 = trans2.readlines()

for line1, line2 in zip(tran1, tran2):
    fulltranscript.append(line1)
    fulltranscript.append(line2)

print(' '.join(fulltranscript))

