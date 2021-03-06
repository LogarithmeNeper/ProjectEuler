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

def collatz(n: int):
    """
    This fucntion uses a generator to get values of the Collatz sequence.
    n -> n/2 if even, n -> 3*n+1 if odd.
    General seed has to be given.
    """
    while n>1:
        n = n//2 if n%2==0 else 3*n+1
        yield n

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

# Sorting algorithms
def merge_sort(lst: list):
    """
    Implementation of the merge sort algorithm in O(n.log(n)) time complexity.
    Does not return anything but modifies the object.
    """ 
    if len(lst) > 1:
        # Splitting
        piv = len(lst) // 2
        left_list = lst[:piv]
        right_list = lst[piv:]

        # Sorting
        merge_sort(left_list)
        merge_sort(right_list)

        # Merging
        i = 0
        j = 0
        k = 0
        # Constructing for the basic elements
        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                lst[k] = left_list[i]
                i+=1
            else:
                lst[k] = right_list[j]
                j+=1
            k+=1
        # IF elements are left in either splited list
        while i < len(left_list):
            lst[k] = left_list[i]
            i+=1
            k+=1
        while j < len(right_list):
            lst[k] = right_list[j]
            j+=1
            k+=1   

# Other useful functions
def fact(n: int):
    """
    Computes the factorial of a number iteratively (so that we do not stack recursive calls)
    """
    res = 1
    for i in range(2, n+1):
        res*=i 
    return res