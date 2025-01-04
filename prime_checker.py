def prime_checker(num):
    n = 2
    while n * n <=num:
        if num % n == 0:
            return False
        n += 1
    return True


n = int(input())
if prime_checker(n):
    print("It's a prime number")
else:
    print("It's not a prime number")