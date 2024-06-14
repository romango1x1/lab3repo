def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_even(number):
    return number % 2 == 0
