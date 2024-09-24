import datetime
currenttime = datetime.datetime.now()
timestamp = currenttime.strftime("%d-%m-%Y %H:%M:%S")
file = open("txt/scores.txt","w")
print("Enter your latest score: ")
score = input()
file.write(score+" recorded at "+timestamp)
file.close()
