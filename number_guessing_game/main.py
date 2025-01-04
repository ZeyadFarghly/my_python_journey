from art import logo
import random
print(logo)
print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 to 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
attempts = 0
if difficulty == 'hard':
    attempts = 5
else:
    attempts = 10
def game(attempts):
    number = random.randint(1, 100)
    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number")
        guess = int(input("Make a guess: "))
        attempts-=1
        if guess == number:
            print(f"you got it! The answer is {number}")
            return 0
        elif guess < number:
            print("Too low.")
        else:
            print("Too high.")
        print("Guess again")
    if attempts == 0:
        print(f"you have ran out of guesses, the answer was {number}, try again")
game(attempts)

