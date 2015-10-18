#!/usr/bin/env python

################################################################################
#
# Project Euler - Problem 67
#
# By starting at the top of the triangle below and moving to adjacent numbers on
# the row below, the maximum total from top to bottom is 23.
#
# 3
# 7 4
# 2 4 6
# 8 5 9 3
#
# That is, 3 + 7 + 4 + 9 = 23.
#
# Find the maximum total from top to bottom in triangle.txt (right click and
# 'Save Link/Target As...'), a 15K text file containing a triangle with
# one-hundred rows.
#
# NOTE: This is a much more difficult version of Problem 18. It is not possible
# to try every route to solve this problem, as there are 299 altogether! If you
# could check one trillion (1012) routes every second it would take over twenty
# billion years to check them all. There is an efficient algorithm to solve it
# . ;o)
#
# Joaquin Derrac - carrdelling@gmail.com
#
################################################################################

def load_data():
    data = []

    with open('./data/problem67.txt','r') as input_file:

        for row in input_file:
            values = row.split()
            data.append(values)

    return data


if __name__ == "__main__":

    triangle = load_data()

    current = [int(x) for x in triangle[-1]]

    # traverse the triangle upwards
    for level in xrange(len(triangle)-2, -1, -1):

        paths = [int(x) for x in triangle[level]]
        new_current = []
        for p in xrange(0, len(paths)):

            new_cost = paths[p] + max(current[p], current[p + 1])
            new_current.append(new_cost)

        current = list(new_current)

    print current[0]
