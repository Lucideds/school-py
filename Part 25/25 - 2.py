file = open("txt/numbers.txt","r")
x = 0
for line in file:
    x = x + int(line)
print(f"The total sum of the number is: {x}")
