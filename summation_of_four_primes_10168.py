import math
from sys import stdin
def is_prime(max_input):
    #sieve of eratosthenes algorithm
    primes_bool = [True] * (max_input + 1)
    primes_bool[0] = primes_bool[1] = False

    for i in range(2, int(math.sqrt(max_input))):
        if primes_bool[i]:
            for j in range(i ** 2, max_input + 1, i):
                primes_bool[j] = False

    return [i for i in range(2, max_input + 1) if primes_bool], primes_bool

if __name__ == '__main__':
    second_last_num = 0
    last_num = 0
    max_input = 10000000
    prime_numbers, prime_numbers_bool = is_prime(max_input)

    while True:
        user_input = input()
        try:
            if user_input == '':
                break
            value = int(user_input)
            if value < 8:
                print("Impossible")
            else:
                if value % 2 == 0:
                    value = value - 4
                    second_last_num = last_num = 2
                else:
                    value = value - 5
                    second_last_num = 2
                    last_num = 3

                for prime in prime_numbers:
                    after_sub = value - prime
                    if prime_numbers_bool[after_sub]:
                        print('{} = {} + {} + {} + {}'.format(user_input, prime, after_sub, second_last_num, last_num))
                        break
        except EOFError:
            break
