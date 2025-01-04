import random
print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
choice = int(input())
if choice > 2:
    print("You typed invalid input, you lose")
else:
    rock = """
        _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
    """

    # Paper
    paper = """
        _______
    ---'    ____)____
            ______)
            _______)
            _______)
    ---.__________)
    """

    # Scissors
    scissors = """
        _______
    ---'   ____)____
            ______)
        __________)
        (____)
    ---.__(___)
    """
    rpc = [rock, paper, scissors]
    print(rpc[choice])
    computer_choice = random.randint(0, 2)
    print("Coputer chose: ")
    print(rpc[computer_choice])
    if choice == 0:
        if(computer_choice == 0):
            print("Draw")
        elif computer_choice == 1:
            print("You lose")
        else:
            print("You win")
    elif choice == 1:
        if(computer_choice == 0):
            print("You win")
        elif computer_choice == 1:
            print("Draw")
        else:
            print("You lose")
    elif choice == 2:
        if(computer_choice == 0):
            print("You lose")
        elif computer_choice == 1:
            print("You win")
        else:
            print("Draw")
