#!/usr/bin/env python

################################################################################
#
# Project Euler - Primes
#
# Auxiliary functions to work with prime numbers
#
# Joaquin Derrac - carrdelling@gmail.com
#
################################################################################


def get_sieve(n):
    sieve = [False, False] + [True] * (n - 1)

    for i in xrange(2, n):
        if sieve[i]:
            sieve[2 * i::i] = [False] * (n // i - 1)

    return sieve


def factorize(n, primes):
    factors = []

    for p in primes:

        while n % p == 0:

            n /= p
            factors.append(p)

    dic_factors = {}

    for factor in factors:

        dic_factors.setdefault(factor, 0)
        dic_factors[factor] += 1

    return dic_factors
