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


def get_ith_prime(ith):

    if ith == 1:
        return 2
    if ith == 2:
        return 3

    primes = {2, 3}

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


def get_sieve(n):
    sieve = [False, False] + [True] * (n - 1)

    for i in range(2, n):
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
