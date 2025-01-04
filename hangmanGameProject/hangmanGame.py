import random
import os
import hangmanArt
import wordDatabase
print(hangmanArt.logo)
random_word = random.choice(wordDatabase.word_list)
length = len(random_word)
result = ['_' for _ in range(length)]
counter = 0
index = 6
while result != list(random_word):
    guess = input("Guess a letter: ").lower()
    os.system('cls')
    if guess not in random_word:
        counter +=1
        index = 6 - counter
        print(f"the letter {guess} is not exist in th word, try another one")
    elif guess in result:
        print(f"the letter {guess} you already guessed, try another one")
    for n in range(length):
        if random_word[n] == guess:
            result[n] = guess
        print(result[n], end = " ")
    print()
    print(hangmanArt.stages[index])
    if counter == 6:
        print("you lose, cuz you tried 6 times to solve word")
        print(f"the word is: {random_word}")
        break
if result == list(random_word):
    print('congratulations you won the game')
    
