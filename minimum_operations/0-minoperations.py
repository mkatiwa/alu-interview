#!/usr/bin/python3
"""min operation"""
from math import sqrt


def minOperations(n):
    """ a function for getting min operations needed to get n number
    H when you can only copy and paste """
    if n <= 1:
        return 0
    elif is_prime(n):
        return n
    else:
        prime = small_prime(n)
        if prime:
            return prime + minOperations(int(n/prime))


def is_prime(n):
    """ funtion is_prime, to check if a number is prime """
    result = True
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            result = False
    return result


def small_prime(n):
    """ get the smallest prime factor """
    result = None
    for i in range(2, int(n/2 + 1)):
        if n % i == 0:
            result = i
            break
    return result
