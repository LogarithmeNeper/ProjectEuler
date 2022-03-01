import math

# Various generators
def fibonacci(a=0, b=1):
    """
    This function uses a generator to get values of the Fibonacci sequence.
    f_{n+2} = f_{n+1} + f_n
    General seed (0,1) given as named parameter for the function.
    """
    while True:
        yield a
        a, b = b, a+b

# Primes
def prime_factors(n: int):
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

def prime_valuation(n: int):
    """
    This function is used to generate p-adic valuation of a number and to return them as a list with the associated prime.
    For example : 10 -> [(2, 1), (5, 1)]
    """
    factors = []
    # Getting 2^v_2(n)
    valuation = 0
    while n%2 == 0:
        n /= 2
        valuation+=1
    if valuation!=0:
        factors.append((2, valuation))
    # Getting odd primes. 
    for curr in range(3, math.floor(math.sqrt(n))+1):
        valuation = 0
        while n%curr == 0:
            n /= curr
            valuation +=1
        if valuation !=0:
            factors.append((curr, valuation))
    # At this point, means that n is prime.
    if n>2:
        factors.append((int(n), 1))
    return factors

def generate_primes(n: int):
    """
    We iterate until we found the right length by checking if remainders with current primes are !=0
    """
    res = [2]
    length = 1
    curr = 3
    while length < n:
        # Implicit int -> bool there + using the all function.
        if all([curr%e for e in res]):
            res.append(curr)
            length+=1
        curr+=2
    return res

def atkin_sieve(max_value: int):
    """
    We generate a list of primes below a certain threshold with a Atkin sieve (yassified Eratosthenes).
    """
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]
    class1 = [1, 13, 17, 29, 37, 41, 49, 53]
    class2 = [7, 19, 31, 43]
    class3 = [11, 23, 47, 59]
    # Generating sieve
    sieve = [False] * max_value
    x=1
    while x**2<max_value:
        y=1
        while y**2<max_value:
            # ^= is equal to = not
            # If we flip the tile an even number of time then we do not change a thing 
            
            # Class 1
            current = 4*x**2+y**2
            if (current < max_value) and (current%60 in class1):
                sieve[current] ^= True 
            # Class 2
            current = 3*x**2+y**2
            if (current < max_value) and (current%60 in class2):
                sieve[current] ^= True
            # Class 3
            current = 3*x**2-y**2
            if (current < max_value) and (x>y) and (current%60 in class3):
                sieve[current] ^= True
            y+=1
        x+=1
    nb = 7
    while nb**2<max_value:
        if sieve[nb]:
            for i in range(nb**2, max_value, nb**2):
                sieve[i]=False
        nb+=1
    for i in range(60, max_value):
        if sieve[i]:
            primes.append(i)
    return primes

# Methods for string manipulation
def is_palindrome(str: str):
    """
    Checks if a string is a palindrome with slicing.
    Params: str 
    """
    return str==str[::-1]

# Getting specific digits
def first_digits(n: int, d:int):
    """
    Get the nth first digits of d.
    """
    return n//10**(int(math.log(n, 10))-d+1)