import random
import string

# Define character sets
letters = string.ascii_letters
symbols = string.punctuation
numbers = string.digits

# Welcome and user input
print("Welcome to the PyPassword Generator!")
lettersSize = int(input("How many letters would you like in your password? "))
symbolsSize = int(input("How many symbols would you like? "))
numbersSize = int(input("How many numbers would you like? "))

# Generate random characters
passLetters = [random.choice(letters) for _ in range(lettersSize)]
passSymbols = [random.choice(symbols) for _ in range()]
passNumbers = [random.choice(numbers) for _ in range(numbersSize)]

# Combine all characters and shuffle
password = passLetters + passSymbols + passNumbers
random.shuffle(password)  # Shuffle in place

# Convert to string
result = ''.join(password)
print(f"Here is your password: {result}")
