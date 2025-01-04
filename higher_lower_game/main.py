from art import logo
from art import vs
from game_data import data
import os
import random
def is_right(choice, right_choice):
    if(choice == right_choice):
        return True
    return False
compare_A = random.choice(data)
counter = 0

print(logo)
while True:
    compare_B = random.choice(data)
    print(f"A: {compare_A['name']}, a {compare_A['description']}, from {compare_A['country']}")
    print(vs)
    print(f"B: {compare_B['name']}, a {compare_B['description']}, from {compare_B['country']}")

    inp = input("Who has more followers, 'A' or 'B': ").upper()
    winner = ''
    if compare_A['follower_count'] > compare_B['follower_count']:
        winner = 'A'
    else:
        winner = 'B'
    if is_right(inp, winner):
        counter+=1
        os.system('cls')
        print(f"You are right! Your current score: {counter}")
        compare_A = compare_B
        
    else:
        os.system('cls')
        print(f"Sorry, that's wrong. Final score: {counter}")
        break
        






