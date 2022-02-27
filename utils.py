import math

def fibonacci(a=0, b=1):
    """
    This function uses a generator to get values of the Fibonacci sequence.
    f_{n+2} = f_{n+1} + f_n
    General seed (0,1) given as named parameter for the function.
    """
    while True:
        yield a
        a, b = b, a+b

def prime_factors(n):
    """
    This function is used to generate prime factors of a number and to return them as a list.
    """
    factors = []
    # Getting 2^v_2(n)
    while n%2 == 0:
        factors.append(2)
        n /= 2
    # Getting odd primes. 
    for curr in range(3, math.floor(math.sqrt(n))+1):
        while n%curr == 0:
            factors.append(curr)
            n /= curr
    # At this point, means that n is prime.
    if n>2:
        factors.append(n)
    return factors

def is_palindrome(str):
    """
    Checks if a string is a palindrome with slicing.
    """
    return str==str[::-1]
