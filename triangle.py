# triangle.py
# challenge: write a function that calculates the
# perimeter and area of a triangle
# Sep 2014, Unchitta Kan


import sys
import math

print "Finding perimeter and area of a triangle"

def pna(a,b,c):
    perimeter = int(a+b+c)
    s = float(perimeter/2.0)
    area = float(math.sqrt(s*(s-a)*(s-b)*(s-c)))
    print "perimeter is " , perimeter
    print "area is " , area

pna(3,4,5)
