import utils

def pb1():
    result = 0
    for i in range(1000):
        if (i%3 == 0) or (i%5 == 0):
            result += i
    return result

def pb2():
    result = 0
    f = utils.fibonacci()
    curr = next(f)
    while curr < 4000000:
        if curr%2 == 0:
            result += curr
        curr = next(f)
    return result

def pb3():
    return utils.prime_factors(600851475143)[-1]

def pb4():
    res = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            candidate = i*j
            if candidate > res:
                if utils.is_palindrome(str(candidate)):
                    res = candidate
    return res
