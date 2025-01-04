line1 = [" ", " ", ""]
line2 = [" ", " ", ""]
line3 = [" ", " ", ""]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot,")
position = input().lower()
letter = position[0]
number = int(position[1]) - 1
lst = ['a', 'b', 'c']
map[number][lst.index(letter)] = 'x'
print(f"{line1}\n{line2}\n{line3}\n")
