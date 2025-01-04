word = input("enter the word you want to calculate: ")
digits = 0
letters = 0
for letter in word:
    if(letter >= 48 and letter <=57):
        digits = digits+1
    elif(letter >=97 and letter <= 122):
        letters = letters+1
print(digits)
print(letters)
