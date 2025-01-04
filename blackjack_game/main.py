import random
import os
from art import logo
def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card
game_restart = True
while game_restart == True:    
    user_cards = []
    computer_cards = []
    user_sum = 0
    computer_sum = 0
    def add_to_user():
        random_user_card = deal_card()
        user_cards.append(random_user_card)
        return random_user_card
    def add_to_computer():
        random_computer_card = deal_card()
        computer_cards.append(random_computer_card)
        return random_computer_card
    def dashboard(user_cards, computer_cards, user_sum, computer_sum):
        print(f"your cards: {user_cards}, current score: {user_sum}")
        print(f"computer card: {computer_cards}, score: {computer_sum}")
    for _ in range(2):
        computer_sum += add_to_computer()
        user_sum += add_to_user()
    print(f"your cards: {user_cards}, current score: {user_sum}")
    print(f"computer first card: {computer_cards[0]}")
    add_card = input("Type 'y' to get another card, type 'n' to pass:")
    went_over = False
    black_jack = False
    while add_card=='y':
        user_sum += add_to_user()
        if user_sum > 21:
            if 11 in user_cards:
                user_cards[user_cards.index(11)] = 1
                user_sum -= 10
            else:
                went_over = True
                break
        elif user_sum == 21:
            black_jack = True
            break
        os.system('cls')
        print(logo)
        print(f"your cards: {user_cards}, current score: {user_sum}")
        print(f"computer first card: {computer_cards[0]}")
        add_card = input("Type 'y' to get another card, type 'n' to pass:")    
    while computer_sum <= user_sum and computer_sum < 17 and went_over == False and black_jack == False:
        computer_sum +=add_to_computer()
        if computer_sum > 21:
            if 11 in computer_cards:
                computer_cards[computer_cards.index(11)] = 1
                computer_sum -= 10
            else:
                went_over = True
    dashboard(user_cards, computer_cards, user_sum, computer_sum)
    if black_jack:
        print("You win, with Black Jack😎")
    elif went_over == False:
        if user_sum > computer_sum:
            print("You Win😁")
        elif user_sum == computer_sum:
            print("Draw 🙃")
        else:
            print("You Lose 😥")
    else:
        if computer_sum > 21:
            print("computer went over: You win😁") 
        else:
            print("you went over: You lose 😥")
    another_game = input("enter 'y' if you want another game, enter 'n' if you want to end the game: ")
    if another_game == 'n':
        game_restart = False