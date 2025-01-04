questions = [
    "How many bones are in the human body?",
    "what is the biggest planet in the solar system",
    "What is the boiling point of water at standard atmospheric pressure?",
    "How many continents are there in the world?",
    "what is the fastest animal?"
    
]

options = (
    ('A. 205', 'B. 206', 'C. 210', 'D. 215'),
    ('A. Earth', 'B. Mars', 'C. Jupiter', 'D. Saturn'),
    ('A. 90C', 'B. 100C', 'C. 110C', 'D. 120C'),
    ('A. 5', 'B. 6', 'C. 7', 'D. 8'),
    ('A. Lion', 'B. Cheetah', 'C. Leopard', 'D. Gazelle')
            )
answers = ['B', 'C', 'B', 'C', 'B']
guesses = []
print('-----------  Quiz  -----------')
score = 0
question_num = 0
for question in questions:
    print(question)
    for option in options[question_num]:
        print(option)
    answer = input("which one is corret? enter here : ")
    guesses.append(answer.upper())
    if answer.upper() == answers[question_num]:
        score += 1
    else:
        print(f"incorrect, the correct answer is {answers[question_num]}")
    question_num += 1
    print("-----------------------------------------")

print("------------------------------")
print("           RESULTS            ")
print("------------------------------")
print()
print("answers: ", end = "")
for answer in answers:
    print(answer, end = " ")
print()
print("guesses: ", end = "")
for guess in guesses:
    print(guess, end = " ")
print()
total = score / 5 * 100
print(f"you got {int(total)}%")
    