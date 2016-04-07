# Create a program that asks the user for a number
# and then prints out a list of all the divisors of that number.

num = input("input a number: ")
i = 1
list = []

while i <= num:
    if num % i == 0:
        list.append(i)
    i += 1

print list
