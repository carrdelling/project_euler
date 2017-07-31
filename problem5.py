#!/usr/bin/env python

################################################################################
#
# Project Euler - Problem 5
#
# 2520 is the smallest number that can be divided by each of the numbers from
# 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the
# numbers from 1 to 20?
#
# Joaquin Derrac - carrdelling@gmail.com
#
################################################################################

from common.primes import get_sieve, factorize

if __name__ == "__main__":

    end = 20

    sieve = get_sieve(end)

    primes = [x for x in range(2, end + 1) if sieve[x]]

    factors_group = {}

    for i in range(2, end + 1):
        factors = factorize(i, primes)

        for factor in factors:

            not_factor = factor not in factors_group
            if not_factor or factors_group[factor] < factors[factor]:
                factors_group[factor] = factors[factor]

    solution = 1

    for factor in factors_group:
        solution *= factor ** factors_group[factor]

    print(solution)
