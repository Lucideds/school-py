import random
suits = ["♥", "♦", "♣", "♠"]
face = ["A", "2", "3","4","5","6","7","8","9","10", "J", "Q", "K"]
deck = []
for suit in suits:
    for card in range(0,12):
        deck.append(face[card] + suit)
        
random.shuffle(deck)
index = 26
player1 = deck [:index]
player2 = deck [index:]
print("player 1 is", player1)
print("player 2 is", player2)
