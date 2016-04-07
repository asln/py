# smallest_num.py
# challenge: write a function that takes 3 numbers returns the smallest one
# Sep 2014, Ashlyn Kan


print "Finding the smallest number"

def getMin(a,b,c):
    x = 0
    if (a > b):
        x = b
    else:
        x = a
    if (x < c):
        print "the smallest number is " , x
    else:
        print "the smallest number is " , c

getMin(3,10,14)
