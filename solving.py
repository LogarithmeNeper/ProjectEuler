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
    with open('./resources/input_pb8.txt', 'r') as f:
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

def pb10():
    """
    Problem 10 : Summation of primes
    See utils.atkin_sieve about how we create a quicker way to get primes.
    """
    lst_of_primes = utils.atkin_sieve(2000000)
    # Casually writing some primes to be reused at some point (way better than pb7)
    with open('./resources/primes.txt', 'w') as f:
        for prime in lst_of_primes:
            f.write(str(prime)+'\n')
    return sum(lst_of_primes)

def pb11():
    """
    Problem 11 : Largest product in a grid.
    Just an iterative version. We work with a 1D-array.
    """
    grid = []
    with open('./resources/input_pb11.txt', 'r') as f:
        for i in range(20):
            lst = list(map(int, f.readline().split()))
            grid+=lst
    res = 1
    for i in range(len(grid)):
        tile_products = []
        if i < 17*20: # vertical (goes below)
            tile_products.append(grid[i]*grid[i+20]*grid[i+2*20]+grid[i+3*20])
        if i%20<17: # horizontal (goes right)
            tile_products.append(grid[i]*grid[i+1]*grid[i+2]*grid[i+3])
        # diagonals
        if i%20<17 and i<17*20:
            tile_products.append(grid[i]*grid[i+20+1]*grid[i+2*20+2]*grid[i+3*20+3])
        if i%20>3 and i<17*20:
            tile_products.append(grid[i]*grid[i+20-1]*grid[i+2*20-2]*grid[i+3*20-3])
        m = max(tile_products) if tile_products != [] else 0
        if res<m:
            res = m
    return res

def pb12():
    """
    Problem 12 : Highly divisible triangular number
    See utils.prime_valuation on how we create a list of valuation.
    For this problem, we use the valuation for each prime factor and say that d(n) = \prod_{i} v_{p_i}+1.
    """
    snd = lambda x: x[1]
    step = 0
    triangular_number = 0
    while True:
        step += 1
        triangular_number += step
        nb_divisors = 1
        pval = utils.prime_valuation(triangular_number)
        # There may be a better way of doing it with a lambda function (typically because Haskell is more simple there)
        for j in range(len(pval)):
            nb_divisors *= snd(pval[j])+1
        if nb_divisors > 500:
            break
    return triangular_number

def pb13():
    """
    Problem 13: Large sum
    Nothing to say there
    """
    import math
    sum = 0
    with open('./resources/input_pb13.txt', 'r') as f:
        for i in range(100):
            sum += int(f.readline().strip())
    res = utils.first_digits(sum, 10)
    return res

def pb14():
    """
    Problem 14 : Longest Collatz Sequence
    See utils.collatz for the generator.
    We use a generator for each number. 
    
    Clearly suboptimal, as a better computing idea would be to memoize the expression in an array.
    """
    length_sequence = -1
    res = 0
    for i in range(1000000):
        sequence = list(utils.collatz(i))
        if  len(sequence) > length_sequence:
            length_sequence = len(sequence)
            res = i
    return res

def pb15():
    """
    Problem 15 : Lattice paths
    One could prove that the number of such paths are Catalan Numbers i.e. (2n)!/(n!)^2 or (2n n).
    See utils.fact for implementation of the factorial function.
    """
    res = utils.fact(40) // (utils.fact(20) ** 2)
    return res

def pb16():
    """
    Problem 16 : Power digit sum
    Dumb solution.
    """
    n = 2**1000
    return sum(list(map(int, list(str(n)))))