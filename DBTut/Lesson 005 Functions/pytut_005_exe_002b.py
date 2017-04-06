# LIST OF PRIME NUMBERS
# efficiency improved by starting at number next after the last in the list
# TODO further improve by skipping modulo of already checked multiples of
# TODO after num1 % 2 is checked checking with 4, 6, 8 ... is not needed ... etc

# a prime can only be divided by 1 and itself


def isprime(num1):
    for i in range(2, num1):
        if (num1 % i) == 0:
            return False
    return True


def getprimes(max_number):
    global list_of_primes

    if not list_of_primes:
        last = 2
    else:
        last = int(list_of_primes[-1]) + 1

    for i in range(last, max_number):
        if isprime(i):
            list_of_primes.append(i)
    return list_of_primes


list_of_primes = []


def main():

    max_num_to_check = int(input('Enter the max limit: '))
    list_of_primes = getprimes(max_num_to_check)

    for i in list_of_primes:
        print(i)


main()
