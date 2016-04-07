# Exercise 3 - List

# Take a list, say for example this one:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 8, 9]
# and write a program that prints out all the
# elements of the list that are less than 5.

# Extras:

# Ask the user for a number and return a list that
# contains only elements from the original list a that are
# smaller than that number given by the user.

myList = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 8, 9]
newList = []

num = input("give me one number: ")

for item in myList:
    if item < num:
        newList.append(item)

print newList
