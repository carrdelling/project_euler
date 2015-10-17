#!/usr/bin/env python

################################################################################
#
# Project Euler - Problem 7
#
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
# that the 6th prime is 13.
#
# What is the 10 001st prime number?
#
################################################################################

from common.primes import get_ith_prime


def get_ith_prime(ith):

    if ith == 1:
        return 2
    if ith == 2:
        return 3

    primes = set()
    primes.add(2)
    primes.add(3)

    current = 5
    inc_4 = False

    while len(primes) < ith:
        possible = [p for p in primes if p*p <= current]
        for p in possible:
            if current % p == 0:
                break
        else:
            primes.add(current)

        current = current + 4 if inc_4 else current + 2
        inc_4 = not inc_4

    return current - 2 if inc_4 else current - 4

if __name__ == "__main__":

    solution = get_ith_prime(10001)

    print solution
