#!/usr/bin/env python

################################################################################
#
# Project Euler - Problem 3
#
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?
#
# Joaquin Derrac - carrdelling@gmail.com
#
################################################################################

if __name__ == "__main__":

    number = 600851475143
    current = 2

    while current * current < number:
        while number % current == 0:
            number /= current
        current += 1

    print(number)
