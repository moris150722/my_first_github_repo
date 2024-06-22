import random

ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

def create_deck():
    deck = [(rank, suit) for rank in ranks for suit in suits]
    random.shuffle(deck)
    return deck

def deal_cards(deck):
    return [deck.pop() for _ in range(2)]

def calculate_hand_value(hand):
    value = sum(values[card[0]] for card in hand)
    num_aces = sum(1 for card in hand if card[0] == 'A')
    while value > 21 and num_aces:
        value -= 10
        num_aces -= 1
    return value

def player_turn(deck, player_hand):
    while True:
        action = input("Do you want to [H]it or [S]tand? ").lower()
        if action == 'h':
            player_hand.append(deck.pop())
            if calculate_hand_value(player_hand) > 21:
                print("Player busts! Dealer wins.")
                return False
        elif action == 's':
            return True
        else:
            print("Invalid input! Please enter 'H' or 'S'.")

def dealer_turn(deck, dealer_hand):
    while calculate_hand_value(dealer_hand) < 17:
        dealer_hand.append(deck.pop())
    print("\nDealer's Hand:", dealer_hand, "| Total Value:", calculate_hand_value(dealer_hand))

def determine_winner(player_hand, dealer_hand):
    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)
    if player_value > 21:
        print("Player busts! Dealer wins.")
    elif dealer_value > 21:
        print("Dealer busts! Player wins.")
    elif player_value == dealer_value:
        print("It's a tie!")
    elif player_value > dealer_value:
        print("Player wins!")
    else:
        print("Dealer wins!")

def play_blackjack():
    deck = create_deck()
    player_hand = deal_cards(deck)
    dealer_hand = deal_cards(deck)

    print("Welcome to Blackjack!")

    if player_turn(deck, player_hand):
        dealer_turn(deck, dealer_hand)
        determine_winner(player_hand, dealer_hand)

play_blackjack()
