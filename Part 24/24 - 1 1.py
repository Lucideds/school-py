encrypted = ""
print("What is the encryption key?")
key = int(input())
print("Enter your text to encrypt")
text = input()
for letter in text.upper():
    enc = ord(letter) + key
    if enc > 90:
        enc = enc - 26
    encrypted = encrypted + chr(enc)
print(encrypted)
