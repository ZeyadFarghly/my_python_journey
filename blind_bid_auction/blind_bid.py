import os
import art
end_of_auction = True
print(art.logo)
print('welcome to the blind auction program')
bidders = {}
while(end_of_auction):
    name = input("whats your name: ")
    bid = int(input("whats your bid: $"))
    bidders[name] = bid
    print("are there any other bidders type 'yes' or 'no'")
    option = input()
    if option == 'no':
        end_of_auction = False
        os.system("cls")
    elif option == 'yes':
        os.system("cls")
        continue
    else:
        while option != 'yes' and option != 'no':
            print("are there any other bidders type 'yes' or 'no'")
            option = input()
max_bid = 0
max_bidder = ''
for key in bidders:
    bid = bidders[key]
    if max_bid < bid:
        max_bid = bid
        max_bidder = key
print(f"the winner is {max_bidder} with a bid of a ${max_bid}")
        
    



