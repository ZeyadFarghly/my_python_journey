#Caclulator

#Add
def add(n1, n2):
    return n1 + n2
#Subtract
def sub(n1, n2):
    return n1 - n2
#Multiply
def multiply(n1, n2):
    return n1 * n2
#divide
def divide(n1, n2):
    return n1 / n2

operations = {
    '+' : add,
    '-' : sub,
    '*' : multiply,
    '/' : divide,
}
sum = 0
should_continue = True
option = 'again'
while should_continue == True:
    if option == 'again':
        num1 = int(input("what's the first number: "))
    else:
        num1 = sum
    num2 = int(input("what is the second number: "))
    for symbol in operations:
        print(symbol)
    operation_symbol = input("pick an operatoin from the 4 operations above: ")
    function = operations[operation_symbol]
    sum = function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {sum}")
    option = input("if you want to continue and make operation with the last result type 'yes' if not type 'no' if you want to make to start the program from the beginning type 'again': ")
    if  option == 'yes':
        should_continue = True
    elif option == 'again':
        should_continue = True
        sum = 0
    else:
        should_continue = False

