# http://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html
# Exercise 2 - Odd or Even (Modular arithmetic)
# Ask the user for a number. Depending on whether the number is even or odd,
# print out an appropriate message to the user. Also check if the number
# is a multiple of 4


num = input("Input a number: ")
if num % 2 == 0:
    print str(num) + " is an even number"
    if num % 4 == 0:
        print "and is a multiple of 4"

else:
    print str(num) + " is an odd number"

