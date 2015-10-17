#!/usr/bin/env python

################################################################################
#
# Project Euler - Problem 16
#
# 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 2^1000?
#
# Joaquin Derrac - carrdelling@gmail.com
#
################################################################################


if __name__ == "__main__":

    solution = sum([int(c) for c in str(2 ** 1000)])

    print solution
