file = open("csv/weatherdata.csv", "r")
data = []
max_rainfall = 0

next(file)
for line in file:
    fields = line.strip().split(",")
    rainfall = float(fields[-1])
    if rainfall > max_rainfall:
        max_rainfall = rainfall
file.close()
print(f"Highest rainfall amount: {max_rainfall}")
