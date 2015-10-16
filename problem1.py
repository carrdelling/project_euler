#!/usr/bin/env python

################################################################################
#
# Project Euler - Problem 1
#
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we
# get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.
#
# Joaquin Derrac - carrdelling@gmail.com
#
################################################################################

if __name__ == "__main__":

    multiples = [x for x in xrange(3,1000) if x%3 == 0 or x%5 == 0]

    solution = sum(multiples)

    print solution