#!/usr/bin/env python

################################################################################
#
# Project Euler - Problem 9
#
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
#
# Joaquin Derrac - carrdelling@gmail.com
#
################################################################################

if __name__ == "__main__":

    solution = -1

    for a in range(1, 350):
        for b in range(a, 500):
            for c in range(b, 1000):
                if c ** 2 == a ** 2 + b ** 2 and a + b + c == 1000:
                    solution = a * b * c

    print(solution)
