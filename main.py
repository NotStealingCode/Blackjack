import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
computer_cards = []
player_cards = []
running = True

def starting_hands():
    for give_p_cards in range(2):
        assign_p_cards = random.choice(cards)
        player_cards.append(assign_p_cards)

        assign_c_cards = random.choice(cards)
        computer_cards.append(assign_c_cards)

def player_sum():
    player_score = 0
    for acquire_p_sum in player_cards:
        player_score += acquire_p_sum
        if player_score > 21 and 11 in player_cards:
            ace_p_conversion = player_cards.index(11)
            player_cards[ace_p_conversion] = 1
            player_score -= 10
    return(player_score)

def computer_final_sum():
    computer_score = 0
    for acquire_c_sum in computer_cards:
        computer_score += acquire_c_sum
    while computer_score < 17:
        add_c_cards = random.choice(cards)
        computer_cards.append(add_c_cards)
        computer_score += add_c_cards
        if computer_score > 21 and 11 in computer_cards:
            ace_c_conversion = computer_cards.index(11)
            computer_cards[ace_c_conversion] = 1
            computer_score -= 10
    return(computer_score)

def deal_cards():
    deal_another_card = random.choice(cards)
    player_cards.append(deal_another_card)
    
def black_jack():
    print(f"\nYour cards: {player_cards}, current score: {player_beginning_score}")
    print(f"\nComputer's final hand: {computer_cards}, current score: {computer_beginning_score}")
    if computer_cards[0] + computer_cards[1] == 21:
        print("\nThe computer has Blackjack. You have lost!")
    elif player_cards[0] + player_cards[1] == 21:
        print("\nYou have Blackjack. You have won")

def win_condition():
    p_score = player_sum()
    c_score = computer_final_sum()
    print(f"\nYour final hand: {player_cards}, final score: {p_score}")
    print(f"\nComputer's final hand: {computer_cards}, final score: {c_score}")
    if p_score > 21:
        print("\nYou went over 21. You have lost!")
    elif c_score > 21 and p_score < 21:
        print("\nDealer went over. You win!")
    elif p_score > c_score:
        print("\nYou have won!")
    elif c_score > p_score:
        print("\nYou have lost!")
    elif c_score == p_score:
        print("\nIt's a draw!")

def reset_game():
    player_cards.clear()
    computer_cards.clear()

while running == True:
    replay_game = input("Do you wish to play a game of Blackjack. Type 'y' for yes or 'n' for no: ")
    if replay_game == 'y':
        reset_game()
        print(logo)
        starting_hands()
        
        player_beginning_score = player_sum()
        computer_beginning_score = computer_final_sum()
        
        print(f"\nYour cards: {player_cards}, current score: {player_beginning_score}")
        print(f"\nComputer's first card: {computer_cards[0]}")
        if player_beginning_score == 21 or computer_beginning_score == 21:
            black_jack()
            running = False
        else:
            deal_pass = True
            while deal_pass == True:
                deal_more_cards = input("\nType 'y' to get another card, type 'n' to pass: ")
                if deal_more_cards == 'y':
                    deal_cards()
                    new_sum = player_sum()
                    print(f"\nYour cards: {player_cards}, current score: {new_sum}")
                    print(f"\nComputer's first card: {computer_cards[0]}")
                    if new_sum > 21:
                        win_condition()
                        deal_pass = False
                else:
                    deal_pass = False
            final_p_sum = player_sum()
            print(f"\nYour final hand: {player_cards}, final score: {final_p_sum}")
            print(f"\nComputer's final hand: {computer_cards}, final score: {computer_beginning_score}")
            win_condition()
    else:
        running = False
    reset_game()