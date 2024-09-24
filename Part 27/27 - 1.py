file = open("csv/scores.csv", "r")
data = []
for line in file:
    line = line.strip()
    data.append(line)
file.close()
data.remove("Scores")
data = [int(i) for i in data]
print(data)
high = max(data)
print(f"The highest number is: {high}")
