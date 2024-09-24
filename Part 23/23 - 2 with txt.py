add_users = True  # make while loop go on forever unless changed
users = [ # pre define a user array as sample data
    {"username": "Lucideds", "password": "GoobIsBetter", "score": 69420}, # not anyones actual password btw 
    {"username": "Raxlair", "password": "ZeldaIsGood", "score": -1},
    {"username": "SmallBrainRat", "password": "Hampter", "score": 34710}
]

while add_users:
    username = input("Input username: ")
    password = input("Input password: ") # i dont know why the sheets want to make me do it the most inefficient way possible but i prefer this
    score = input("Input score: ")
    user = {"username": username, "password": password, "score": score}
    users.append(user)
    print("Would you like to add another player? Y/N")
    answer = input()
    if answer.lower() == "n":
        break
    else:
        pass

# Writing users data to a TXT file
with open("users.txt", "w") as file:
    for user in users:
        file.write(str(users))

print("Data stored successfully in 'users.txt' file.")
