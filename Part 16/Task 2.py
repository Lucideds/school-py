word = "sheep"
count = 0

print("Enter a character:")
character = input()

for letter in word:
    if letter == character:
        count = count + 1

print(f"The letter {character} appears {count} times")
