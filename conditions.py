value = input("enter a color to check: ")
count = 0
myList = [('red', 'white', 'blue'), ('green', 'pink', 'purble'), ('orange', 'yellow', 'lime')]
for tuple in myList:
    if(tuple.count(value)):
        print("true")
    else:
        print("false")


