# LIST OF PRIME NUMBERS

# A prime can only be divided by 1 and itself


def isprime(num1):
    for i in range(2, num1):
        if (num1 % i) == 0:
            return False
    return True


def getprimes(max_number):
    list_of_primes = []
    for i in range(2, max_number):
        if isprime(i):
            list_of_primes.append(i)
    return list_of_primes


def main():
    max_num_to_check = int(input('Enter the max limit: '))
    list_of_primes = getprimes(max_num_to_check)

    for i in list_of_primes:
        print(i)


main()
