board = [["1", "2", "3"], 
         ["4", "5", "6"], 
         ["7", "8", "9"]] 

player = "X"
game_loop = True
incorrect_move = False

def instructions():
    print("Instructions:\n")
    print("This is a 2 player game.")
    print("The first player will be noughts.")
    print("The second player will be crosses.")
    print("The game is presented in a grid...\n")

def displayboard(board): 
    print(" ", board[0][0], "│", board[0][1], "│", board[0][2]) 
    print(" ───┼───┼───")
    print(" ", board[1][0], "│", board[1][1], "│", board[1][2]) 
    print(" ───┼───┼───")
    print(" ", board[2][0], "│", board[2][1], "│", board[2][2])

def play_move():
    global incorrect_move
    print(f"Player: {player} is playing now.")
    print("Where do you want to play?")
    move = int(input())
    if move == 1 and board[0][0] == "1":
        board[0][0] = player
        incorrect_move = False
    elif move == 2 and board[0][1] == "2":
        board[0][1] = player
        incorrect_move = False
    elif move == 3 and board[0][2] == "3":
        board[0][2] = player
        incorrect_move = False
    elif move == 4 and board[1][0] == "4":
        board[1][0] = player
        incorrect_move = False
    elif move == 5 and board[1][1] == "5":
        board[1][1] = player
        incorrect_move = False
    elif move == 6 and board[1][2] == "6":
        board[1][2] = player
        incorrect_move = False
    elif move == 7 and board[2][0] == "7":
        board[2][0] = player
        incorrect_move = False
    elif move == 8 and board[2][1] == "8":
        board[2][1] = player
        incorrect_move = False
    elif move == 9 and board[2][2] == "9":
        board[2][2] = player
        incorrect_move = False
    else:
        print("Not a correct option/someone has already gone there. Try again.")
        incorrect_move = True

def check_win():
    global won
    won = False
    if (board[0][0] == player and board[0][1] == player and board[0][2] == player) or \
       (board[1][0] == player and board[1][1] == player and board[1][2] == player) or \
       (board[2][0] == player and board[2][1] == player and board[2][2] == player) or \
       (board[0][0] == player and board[1][0] == player and board[2][0] == player) or \
       (board[0][1] == player and board[1][1] == player and board[2][1] == player) or \
       (board[0][2] == player and board[1][2] == player and board[2][2] == player) or \
       (board[0][0] == player and board[1][1] == player and board[2][2] == player) or \ 
       (board[0][2] == player and board[1][1] == player and board[2][0] == player): # made it look better
        won = True
    return won

instructions()

while game_loop:
    displayboard(board)
    play_move()
    while incorrect_move:
        play_move()
    if check_win():
        print(f"GG, player '{player}' wins!")
        game_loop = False
    if player == "X":
        player = "O"
    else:
        player = "X"
# i hated doing this