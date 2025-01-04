import string
import art
def caeser(text, shift, letters, dir):
    result = ''
    for i in range(len(text)):
        if text[i] in letters:
            index = letters.index(text[i])
            text = list(text)
            letters = list(letters)
            if dir == 'encode':
                text[i] = letters[(index+shift) % 26]
            else:
                text[i] = letters[(index-shift) % 26] 
            result += text[i]
        else:
            result += text[i]
    return result
letters = string.ascii_lowercase
print(art.logo)
repeat = "yes"
while repeat == 'yes':
    direction = input("type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("type your message:\n").lower()
    shift = int(input("type the shift number:\n"))
    print(caeser(text, shift, letters, direction))
    repeat = input("Type 'yes' if you want to go again. Otherwise type 'no'.")
    

