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