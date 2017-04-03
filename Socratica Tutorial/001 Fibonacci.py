# FIBONACCI NUMBERS

""" First few Fibonacci numbers
1 , 1 , 2 , 3 , 5 , 8 , 13 , 21 , 34 , 55 , 89 ...
1 + 1 = 2
    1 + 2 = 3
        2 + 3 = 5
            3 + 5 = 8
                5 + 8 = 13
                    8 + 13 = 21
                        13 + 21 = 34
                             21 + 34 = 55
                                  34 + 55 = 89
                                       ...

Goal: Write function to return nth term of Fibonacci Sequence
    - Fast
    - Clearly written
    - Rock solid


old code
# function to return nth term
def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        # return the previous two terms
        return fibonacci(n - 1) + fibonacci(n - 2)

How this works:
fib(5) = fib(4) + fib(3) _________
          /    \        \         \
    = fib(3) + fib(2) + fib(2) + fib(1)
         / \
    = fib(2) + fib(1) + fib(2) + fib(2) + fib(1)
    = 1 + 1 + 1 + 1 + 1
    = 5


Memoization:
will cure the effectivenes probelm by caching values so future functions does
not need to repeat the work.

1st - explicitely - code below:

fibonacci_cache = {}

def fibonacci(n):
    # if value sis in cache, then return it
    if n in fibonacci_cache:
        return fibonacci_cache[n]

    # compute the nth term
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        # write the previous in the new variable
        value = fibonacci(n - 1) + fibonacci(n - 2)

    # cache the value and return it
    fibonacci_cache[n] = value
    return value

for n in range(1, 100000):
    print('{} : {}'.format(n, fibonacci(n)))

2nd - Python caching tool:
"""


# this will do import all needed for the cache
# Least Recently User Cache
from functools import lru_cache

# call the cache and enter maximum to cache
@lru_cache(maxsize = 100000)
# function to return nth term
def fibonacci(n):
    # check the input is a positive integer
    if type(n) != int:
        raise TypeError('n must be a positive int')
    if n < 1:
        raise ValueError('n must be a positive int')
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        # return the previous two terms
        return fibonacci(n - 1) + fibonacci(n - 2)

for n in range(1, 100000):
    fibonacci_ratio = fibonacci(n + 1) / fibonacci(n)
    print('{} : ratio {} : number {}'\
          .format(n, fibonacci_ratio, fibonacci(n)))

















