file = open("csv/names.csv", "r")
data = []
for line in file:
    line = line.strip()
    data.append(line)
file.close()
letter = input("Enter the first letter of the name: ")
for name in data:
    if letter.upper() == name[0]:
        print(name)
