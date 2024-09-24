word = "sandwich"
user_guess = ""
not_guessed = word != user_guess
guesses = 0

while not_guessed and guesses < 5:
    if guesses == 1:
        firstletter = word[0]
        print(f"The first letter of the word is {firstletter}")
    elif guesses == 3:
        lastletter = word[-1]
        print(f"The last letter of the word is {lastletter}")
    print("Guess the word:")
    user_guess = input()
    guesses = guesses + 1

    not_guessed = word != user_guess
if word == user_guess:
    print("Correct, you win!")
else:
    print("Incorrect, you lose!")
