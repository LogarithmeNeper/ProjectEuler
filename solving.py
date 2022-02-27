from functools import reduce
import utils

def pb1():
    """
    Problem 1 : Multiples of 3 or 5
    Simple iteration and adding when necessary.
    """
    result = 0
    for i in range(1000):
        if (i%3 == 0) or (i%5 == 0):
            result += i
    return result

def pb2():
    """
    Problem 2 : Even Fibonacci numbers
    See utils.fibonacci for generating numbers.
    Simple iteration on the generator and adding when ncessary.
    """
    result = 0
    f = utils.fibonacci()
    curr = next(f)
    while curr < 4000000:
        if curr%2 == 0:
            result += curr
        curr = next(f)
    return result

def pb3():
    """
    Problem 3 : Largest prime factor
    See utils.prime_factors for having the list of prime numbers.
    Generates the list of prime factors and takes the last element.
    """
    return utils.prime_factors(600851475143)[-1]

def pb4():
    """
    Problem 4 : Largest palindrome product
    See utils.is_palindrome for checking if a string is a palindrome.
    Iterates over {100, ... , 999}^2 and discards if less than current result.
    Otherwise, checks and updates.
    """
    res = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            candidate = i*j
            if candidate > res:
                if utils.is_palindrome(str(candidate)):
                    res = candidate
    return res

def pb5():
    """
    Problem 5 : Smallest multiple
    By hand using max valuation for each prime in range.
    """
    res = 2**4 * 3**2 * 5 * 7 * 11 * 13 * 17 * 19 # 16 * 9 * 5 * 7 * 11 * 13 * 17 * 19 
    return res

def pb6():
    """
    Problem 6 : Sum square difference
    By hand using sum([1..n])=n*(n+1)/2 and sum([1**2..n**2])=n*(n+1)*(2*n+1)/6
    """
    n = 100
    sum_of_squares = int(n*(n+1)*(2*n+1)/6)
    square_of_sum = int((n*(n+1)/2)**2)
    return square_of_sum-sum_of_squares

def pb7():
    """
    Problem 7 : 10001st prime
    See utils.generate_primes for prime generation.
    We then (apart from writing the list on a file) get the last element of the list.
    """
    n = 10001
    lst_of_primes = utils.generate_primes(n)
    # Casually writing some primes to be reused at some point
    with open('./resources/primes.txt', 'w') as f:
        for prime in lst_of_primes:
            f.write(str(prime)+'\n')
    return lst_of_primes[-1]

def pb8():
    """
    Problem 8 : Largest product in a series
    We first open and convert data as a list of integers (string -> list[char] -> list[int]).
    Then we use \l x,y-> xy and reduce to a single value iterating on the sliced list, and then updates if necessary.
    """
    with open('./resources/input_pb8.txt') as f:
        lst = list(map(int, list(f.readline())))
    res = 1
    for i in range(len(lst)-13):
        current_slice = lst[i:i+13]
        product = reduce((lambda x, y: x*y), current_slice)
        if product > res:
            res = product
    return res

def pb9():
    """
    Problem 9 : Special Pythagorician Triplet
    Dumb algorithm.
    """
    for i in range(1, 1000):
        for j in range(1, 1000):
            k = 1000-i-j
            if (i*i+j*j)==k*k:
                return i*j*k