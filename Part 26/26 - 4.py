file = open("txt/romerojuliet.txt","r+")
stuff = file.read()
letter = input("what do u wanna look for: ")
count = stuff.count(letter)

file.write("\n\nLetter: "+letter+"\nOccurrences: "+str(count))
file.close()
