# Practice 5 - List Overlap
# Take two lists, say for example these two:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains
# only the elements that are common between the lists
# (without duplicates). Make sure your program works on
# two lists of different sizes.

# Extras:
# Randomly generate two lists to test this (in 1 line of code)

import random

a = random.sample(xrange(1, 20), 9)
b = random.sample(xrange(1, 20), 11)
c = []

for item in b:
    if item in a:
        c.append(item)
print "List A: ", a
print "List B: ", b
print "List C: ", c
