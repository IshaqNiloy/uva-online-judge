import math

if __name__ == '__main__':
    primes = [True] * (10000000 + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(20 ** 0.5) + 1):
        if primes[i]:
            for j in range(i ** 2, 20 + 1, i):
                primes[j] = False


    print(primes[:100])