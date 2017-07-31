#!/usr/bin/env python

################################################################################
#
# Project Euler - Problem 12
#
# The sequence of triangle numbers is generated by adding the natural numbers.
# So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first
# ten terms would be:
#
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
# Let us list the factors of the first seven triangle numbers:
#
#  1: 1
#  3: 1,3
#  6: 1,2,3,6
# 10: 1,2,5,10
# 15: 1,3,5,15
# 21: 1,3,7,21
# 28: 1,2,4,7,14,28
#
# We can see that 28 is the first triangle number to have over five divisors.
#
# What is the value of the first triangle number to have over five hundred
# divisors?
#
# Joaquin Derrac - carrdelling@gmail.com
#
################################################################################

from math import sqrt


def count_divisors(n):
    # somewhat 'clever' brute force: search for factors up to srqt(n)
    # (for each factor there will be a reciprocal; discount 1 if n is a
    # perfect square)
    divisors = 0
    sqrt_n = int(sqrt(n))

    for i in range(1, sqrt_n + 1):
        if not n % i:
            divisors += 2

    if sqrt_n ** 2 == n:
        divisors -= 1
    return divisors


def triangular_generator():
    current = 1
    acumulator = 0
    while True:
        acumulator += current
        yield acumulator
        current += 1


if __name__ == "__main__":

    solution = -1
    numbers = triangular_generator()

    for solution in numbers:
        div = count_divisors(solution)

        if div > 500:
            break

    print(solution)
