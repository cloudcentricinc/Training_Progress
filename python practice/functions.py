import math


# 1
def spam():
    # print eggs
    print("Eggs!")


spam()


# 4
def power(base, exponent):
    result = base ** exponent
    print("%d to the power of %d is %d." % (base, exponent, result))


power(37, 4)


# 6
def cube(number):
    return number ** 3


def by_three(number):
    if number % 3 == 0:
        return cube(number)
    else:
        return False


# 8
# import math
print(math.sqrt(25))

# 9
from math import sqrt

print(sqrt(25))

# 10
from math import *

print(sqrt(25))


# 19


def distance_from_zero(n):
    if type(n) == int or type(n) == float:
        return abs(n)
    else:
        return "Nope"


distance_from_zero("-asdas")
