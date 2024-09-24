def load_words():
    with open('words.txt') as word_file:
        valid_words = set(word_file.read().split())
    return valid_words

if __name__ == '__main__':
    english_words = load_words()

print("Input encrypted string")
encrypted = input()
decrypted = False

while decrypted == False:
    print("while loop")
    if encrypted in english_words:
        print("Compared")
        print(encrypted)
        print(f"'{encrypted}' was found as a word, does it look correct?")
        ans = input("Y/N: ")
        if ans.lower() == 'y':
            print(f"Your decrypted sting is '{encrypted}'")
            decrypted = True
            break
    else:
        encrypted = ""
        print("else statement")
        for letter in encrypted:
            print("for loop")
            enc = ord(letter) + 1
            print(enc)
            if enc > 122:
                print("if loop")
                enc = enc - 26
            print("out of if loop")
            encrypted = encrypted + chr(enc)
            print(encrypted)
