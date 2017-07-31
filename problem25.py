#!/usr/bin/env python

################################################################################
#
# Project Euler - Problem 25
#
# The Fibonacci sequence is defined by the recurrence relation:
#
# Fn = Fn-1 + Fn-2, where F1 = 1 and F2 = 1.
# Hence the first 12 terms will be:
#
# F1 = 1
# F2 = 1
# F3 = 2
# F4 = 3
# F5 = 5
# F6 = 8
# F7 = 13
# F8 = 21
# F9 = 34
# F10 = 55
# F11 = 89
# F12 = 144
# The 12th term, F12, is the first term to contain three digits.
#
# What is the index of the first term in the Fibonacci sequence to contain
# 1000 digits?
#
# Joaquin Derrac - carrdelling@gmail.com
#
################################################################################

def fibonacci():

    first = 1
    second = 1

    yield first
    yield second

    while True:

        third = first + second

        yield third

        first = second
        second = third

if __name__ == "__main__":

    fib_gen = fibonacci()
    index = 1
    while True:

        number = next(fib_gen)
        length =  len(str(number))

        if length >= 1000:

            break
        index += 1

    print(index)
