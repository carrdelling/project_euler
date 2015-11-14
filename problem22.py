#!/usr/bin/env python

################################################################################
#
# Project Euler - Problem 22
#
# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
# containing over five-thousand first names, begin by sorting it into
# alphabetical order. Then working out the alphabetical value for each name,
# multiply this value by its alphabetical position in the list to obtain a
# name score.
# For example, when the list is sorted into alphabetical order, COLIN, which is
# worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN
# would obtain a score of 938 x 53 = 49714.
#
# What is the total of all the name scores in the file?
#
# Joaquin Derrac - carrdelling@gmail.com
#
################################################################################

letter_score = {'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4, 'g': 7, 'f': 6,
                'i': 9, 'h': 8, 'k': 11, 'j': 10, 'm': 13, 'l': 12, 'o': 15,
                'n': 14, 'q': 17, 'p': 16, 's': 19, 'r': 18, 'u': 21, 't': 20,
                'w': 23, 'v': 22, 'y': 25, 'x': 24, 'z': 26}


def name_score(name):
    return sum([letter_score[s] for s in name])


if __name__ == "__main__":

    names_path = './data/p022_names.txt'

    names = []

    with open(names_path, 'r') as names_file:

        for row in names_file:

            parts = row.split(',')

            for part in parts:

                name = part.replace('"', '')

                names.append(name.lower())

    result = sum([(pos + 1) * name_score(name) for pos, name in
                  enumerate(sorted(names))])

    print result
