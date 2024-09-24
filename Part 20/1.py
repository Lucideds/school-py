import random
suits = ["♥", "♦", "♣", "♠"]
deck = []
for suit in suits:
    for card in range(1,14):
        if card == 1:
            deck.append("A"+suit)
        elif card == 11:
            deck.append("J"+suit)
        elif card == 12:
            deck.append("Q"+suit)
        elif card == 13:
            deck.append("K"+suit)
        else:
            deck.append(str(card)+suit)
random.shuffle(deck)
index = 26
player1 = deck [:index]
player2 = deck [index:]
print("player 1 is", player1)
print("player 2 is", player2)



