import random

word = ""

word = word + input("First word: ")
word = word + input("Second word: ")
word = word + input("Third word: ")

new_word = ""

for letter in word: 
    print(letter)
    if letter == "a": 
        new_word = new_word + chr(random.randint(33, 37))
    elif letter == "e":
        new_word = new_word + chr(random.randint(38, 42))
    elif letter == "i":
        new_word = new_word + chr(random.randint(43, 47))
    elif letter == "o":
        new_word = new_word + chr(random.randint(58, 61))
    elif letter == "u":
        new_word = new_word + chr(random.randint(91, 94))
    else: 
        new_word = new_word + letter 
    print(new_word)
print(new_word)  
