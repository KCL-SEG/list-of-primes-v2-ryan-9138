"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def isprime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True


def primes(number_of_primes):
    list = []
    if number_of_primes <= 0:
        raise ValueError(f"{number_of_primes} must be a positive number")
    i = 0 #number of prime numbers in the list
    x = 2 #first prime number
    while i < number_of_primes:
        if isprime(x):
            list.append(x)
            i +=1
        x += 1
    return list
