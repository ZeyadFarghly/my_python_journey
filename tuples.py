myList = [(1,2,3), (4,5,6), (7,8,9)]
newList = []
for tuple in myList:
    newList.append(tuple[:-1] + (100,))
print(newList)
