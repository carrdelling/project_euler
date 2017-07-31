#!/usr/bin/env python

################################################################################
#
# Project Euler - Problem 10
#
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.
#
# Joaquin Derrac - carrdelling@gmail.com
#
################################################################################

from common.primes import get_sieve

if __name__ == "__main__":

    limit = 2000000
    solution = 0

    sieve = get_sieve(limit)

    for i in range(0, limit):
        if sieve[i]:
            solution += i

    print(solution)
