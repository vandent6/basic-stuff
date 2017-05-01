import math

'''
v1 get_primes

def get_primes(input_list):
    result_list = list()
    for element in input_list:
        if is_prime(element):
            result_list.append(element)

    return result_list
'''

def get_primes(number):
    while True:
        if is_prime(number):
            yield number
        number += 1

def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0:
                return False
        return True
    return False

def solve_number_10():
    total = 2
    for next_prime in get_primes(3):
        if next_prime < 200000:
            total += next_prime
        else:
            print(total)
            return


        
