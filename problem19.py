#!/usr/bin/env python

################################################################################
#
# Project Euler - Problem 19
#
# You are given the following information, but you may prefer to do some
# research for yourself.
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century
# unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century
# (1 Jan 1901 to 31 Dec 2000)?

# Joaquin Derrac - carrdelling@gmail.com
#
################################################################################

def leap_year(year):
    if year % 4:
        return False
    if not year % 400:
        return True
    if not year % 100:
        return False
    return True


def days_in_a_month(month, year):
    if month in [4, 6, 9, 11]:
        return 30
    if month == 2:
        if leap_year(year):
            return 29
        return 28
    return 31


def days_to_next_day_one():
    year = 1900
    month = 1

    while True:

        for _ in range(12):
            days = days_in_a_month(month, year)
            yield days

            month = month + 1 if month < 12 else 1
        year += 1


if __name__ == "__main__":

    calendar = days_to_next_day_one()
    week_day = 1
    solution = 0

    for y in range(1900, 2001):
        for i in range(12):
            week_day = (week_day + next(calendar)) % 7

            if week_day == 0 and y > 1900:
                solution += 1

    print(solution)
