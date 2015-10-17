#!/usr/bin/env python

################################################################################
#
# Project Euler - Problem 15
#
# Starting in the top left corner of a 2x2 grid, and only being able to move to
# the right and down, there are exactly 6 routes to the bottom right corner.
#
#
# How many such routes are there through a 20x20 grid?
#
# Joaquin Derrac - carrdelling@gmail.com
#
################################################################################

from math import factorial

if __name__ == "__main__":

    n = 20

    # How many ways of storing 20 eggs in 40 boxes??? -> [(2n)!]/[n!*n!]
    solution = factorial(2 * n) / (factorial(n) ** 2)

    print solution
