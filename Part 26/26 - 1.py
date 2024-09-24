file = open("txt/players.txt", "w") 
x = 1
for i in range(4):
    print(f"Enter player {x}")
    name = input()
    file.write(name+"\n")
    x = x + 1
file.close() 
