import math
from sys import stdin

if __name__ == '__main__':
    is_prime = 1
    prime_numbers = []
    starting_point = 2
    # inputs = [378, 306, 370, 52, 80, 106, 176, 154, 36, 222, 122, 254, 442, 320, 14, 384, 172, 120, 484, 188, 328, 486,
    #           492, 424, 134, 304, 104, 396, 88, 230, 268, 144, 66, 270, 234, 128, 360, 200, 502, 224, 334, 162, 462, 278,
    #           388, 452, 160, 114, 28, 488, 266, 312, 512, 420, 40, 402, 290, 448]
    while 1:
        input = int(stdin.readline())
        if input == 0:
            break
        for i in range(starting_point, input):
            for j in range(2, int(math.ceil(math.sqrt(i)))+2):
                if i % j == 0:
                    is_prime = 0
                    break
            if is_prime == 1:
                prime_numbers.append(i)
            else:
                is_prime = 1
        starting_point = input + 1

        for prime_number in prime_numbers:
            if input - prime_number in prime_numbers:
                print(str(input) + ' = ' + str(prime_number) + ' + '
                      + str(prime_numbers[prime_numbers.index(input - prime_number)]))
                break
