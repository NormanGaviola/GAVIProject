from random import *


#Function Definitions
def deal_from_deck(deck):
    if len(deck)<1:
         create_deck(deck)
         shuffle_deck(deck)
         deal_cards()

def deal_cards(deck):
    return deck.pop(0)

def define_cards(n): #All cards contained in the deck
    rank_string = ("ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen","king")
    suit_string = ("clubs", "diamonds", "hearts", "spades")
    cards = []

    for suit in range(4):
        for rank in range(13):
            card_string = rank_string[rank] + " of " + suit_string[suit]
            cards.append(card_string)
    return cards[n]

def create_deck(deck):
    for i in range(52):
        deck.append(i)
    return

def shuffle_deck(deck):
    shuffle(deck)
    return

def card_value(n):
    vals = (11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10)
    card_vals = []

    for s in range(4):
        for r in range(13):
            card_vals.append(vals[r])
    return card_vals[n]

def card_display(n):
    name = define_cards(n)
    val = card_value(n)
    print (name + " : " + str(val))

def show_cards(hand):
    for card in hand:
        card_display(card)

def hand_val(hand):
    list = []
    for card in hand:
        list.append(card_value(card))
    if sum(list) > 21:
        for i in range(len(list)):
            if list[i] == 11:
                list[i] = 1
    return sum(list)

# Initializing
drawn_hands = 0
player_wins = 0
dealer_win = 0
deck = []
player_hand = []
dealer_hand = []
playing = True


#Processing
create_deck(deck)
shuffle_deck(deck)

for i in range(2):
    card = deal_cards(deck)
    card2 = deal_cards(deck)
    player_hand.append(card)
    dealer_hand.append(card2)


# put in a loop for player hand

print("\nDealer shows: ")
card_display(dealer_hand[0])


while playing == True:
    player_val = hand_val(player_hand)


    print("\nYour current hand is...")
    show_cards(player_hand)
    print(hand_val(player_hand))


    if player_val < 22:
        H_or_S = input("Would you like to Hit or Stand?\n")
        if H_or_S == "hit":
            player_hand.append(deal_cards(deck))
        elif H_or_S == "stand":
            playing = False
    else:
        playing = False
        print("busted")
        print("Thanks for playing")
        exit()

# check if it is higher than 21, if yes then end program, dealer hand wins
show_cards(dealer_hand)

playing = True
while playing == True:
    if hand_val(dealer_hand) < 17:
        dealer_hand.append(deal_cards(deck))
    else:
        playing = False


print("Dealer has:")
print(show_cards(dealer_hand))



if hand_val(dealer_hand) > 21:
    print("The dealer busted")
    show_cards(dealer_hand)
    print("You win!")
    exit()
elif hand_val(dealer_hand) > hand_val(player_hand):
    print("Dealer wins, You lose")
    show_cards(dealer_hand)
    exit()
elif hand_val(player_hand) > hand_val(dealer_hand):
    print("You win!")
    show_cards(player_hand)
    exit()
else:
    print("It's a Tie")
    exit()