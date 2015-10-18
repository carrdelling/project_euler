#!/usr/bin/env python

################################################################################
#
# Project Euler - Problem 17
#
# If the numbers 1 to 5 are written out in words: one, two, three, four, five,
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
# words, how many letters would be used?
#
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
# forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20
# letters. The use of "and" when writing out numbers is in compliance with
# British usage.
#
# Joaquin Derrac - carrdelling@gmail.com
#
################################################################################

units = {1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4, 0: 0}

tens = {2: 6, 3: 6, 4: 5, 5: 5, 6: 5, 7: 7, 8: 6, 9: 6}

hundreds = {0: 0, 1: 13, 2: 13, 3: 15, 4: 14, 5: 14, 6: 13, 7: 15, 8: 15, 9: 14}

ten_to_nineteen = {10: 3, 11: 6, 12: 6, 13: 8, 14: 8, 15: 7, 16: 7, 17: 9,
                   18: 8, 19: 8}


def number_str_lenght(number):
    h = number / 100
    du = number % 100
    d = du / 10
    u = du % 10

    if du < 1:
        # no need for the 'and'
        num_length = hundreds[h] - 3
    elif 0 < du <= 9:
        num_length = hundreds[h] + units[u]
    elif 9 < du <= 19:
        num_length = hundreds[h] + ten_to_nineteen[du]
    else:
        num_length = hundreds[h] + tens[d] + units[u]

    return num_length


if __name__ == "__main__":

    solution = 0
    for i in xrange(1, 1000):
        length = number_str_lenght(i)
        solution += length

    # the last one - 1000
    solution += 11

    print solution
