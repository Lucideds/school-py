users = [ # pre define a user array as sample data
    {"username": "Lucideds", "password": "GoobIsBetter", "score": 69420}, # not anyones actual password btw 
    {"username": "Raxlair", "password": "ZeldaIsGood", "score": -1},
    {"username": "SmallBrainRat", "password": "Hampter", "score": 34710}
]

add_users = True # make while loop go on forever unless changed

while add_users:
    username = input("Input username: ")
    password = input("Input password: ") # i dont know why the sheets want to make me do it the most inefficient way possible but i prefer this
    score = input("Input score: ")
    user = {"username": username, "password": password, "score": score} # make everything together
    users.append(user) # add to list
    print("Would you like to add another player? Y/N")
    answer = input()
    if answer.lower() == "n":
        break # break loop? for some reason making it false doesnt even do anything
        # add_users = False
    else:
        pass # i feel like this is unnecessary but why not

print(users) # print full list
# have made one that stores data to a txt file