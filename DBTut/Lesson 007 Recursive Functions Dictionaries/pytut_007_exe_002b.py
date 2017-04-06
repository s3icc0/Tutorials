# FIBONACCI NUMBERS

# print a sequence of n Fibonacci numbers

# Fn = Fn-0 + Fn-2
# Where F0 = 0 and F1 = 1


""" print(fib(9))
0 1 1 2 3 5 8 13 21


1st : result = fib(2) + fib(1) : 2 + 1
2nd : result = (fib(1) + fib(0)) + fib(0) : 1 + 0 = 1
"""


fibolist = []

max = 10


def fibo(n):
    global fibolist
    global max



for i in fibolist:
    print(i, end=', ')




def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:

        result = fib(n - 1) + fib(n - 2)
        return result
