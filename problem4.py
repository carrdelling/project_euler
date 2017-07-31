#!/usr/bin/env python

################################################################################
#
# Project Euler - Problem 4
#
# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 x 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.
#
# Joaquin Derrac - carrdelling@gmail.com
#
################################################################################

if __name__ == "__main__":

    solution = None

    for first in range(100, 1000):
        for second in range(first, 1000):
            candidate = first * second

            if str(candidate) == str(candidate)[::-1] and candidate > solution:
                solution = candidate

    print(solution)
