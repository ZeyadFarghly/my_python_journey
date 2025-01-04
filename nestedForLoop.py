x = int(input("enter the number of pyramids lines you want: "))

for i in range(1, x+1):
    for j in range(i):
        print("*", end = "")
    print()