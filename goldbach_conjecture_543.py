import math
from sys import stdin
import bisect

def is_prime(max_input):
    prime_numbers_bool = [True] * (max_input + 1)
    prime_numbers_bool[0] = prime_numbers_bool[1] = False

    for i in range(2, int(math.sqrt(max_input)) + 1):
        if prime_numbers_bool[i]:
            for j in range(i ** 2, max_input + 1, i):
                prime_numbers_bool[j] = False

    return [i for i in range(2, max_input + 1) if prime_numbers_bool[i]], prime_numbers_bool

if __name__ == '__main__':
    max_value = 1000005
    prime_numbers, isPrime = is_prime(max_value)
    while True:
        value = input()
        value = int(value)
        if value == 0:
            break
        for prime in prime_numbers:
            after_sub = value - prime

            if isPrime[after_sub]:
                print("{} = {} + {}".format(value, prime, after_sub))
                break




    # for input in inputs:
    #     for prime_number in prime_numbers:
    #         if input - prime_number in prime_numbers:
    #             print('{} = {} + {}'.format(input, prime_number, prime_numbers[prime_numbers.index(input - prime_number)]))
    #             break


