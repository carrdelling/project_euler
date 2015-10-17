#!/usr/bin/env python

################################################################################
#
# Project Euler - Problem 7
#
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
# that the 6th prime is 13.
#
# What is the 10 001st prime number?
#
# Joaquin Derrac - carrdelling@gmail.com
#
################################################################################

from common.primes import get_ith_prime

if __name__ == "__main__":

    solution = get_ith_prime(10001)

    print solution
