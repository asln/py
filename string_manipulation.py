# Challenge 1 - Input & String manipulation
''' Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that
tells them the year that they will turn 100 years old.

Extras:

Add on to the previous program by asking the user for another number
and printing out that many copies of the previous message.
(Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines.
(Hint: the string "\n is the same as pressing the ENTER button) '''


from datetime import date

def main():
    name = raw_input("What's your name? ")
    age = input("How old are you? ")
    thisyear = current_year()
    if ask_bday() == True:
        turn100 = (100 - age) + thisyear    # if the person has not had a birthday, 
    else:                            # it has to be 99 we subtract from in order
        turn100 = (99 - age) + thisyear  #for the expression to be logically right
    message = name + ', ' + 'you\'ll turn 100 in ' + str(turn100) + '\n'
    print_times(message)


def ask_bday():     # this function asks if the user has had a bday and returns bool
    bday = raw_input("have you had a birthday this year? (y/n) ")
    if bday.lower() == 'y':
        return True
    else:
        return False

def current_year():     # get the current year from date module
    year = date.today().year
    return year


def print_times(p):
    x = input("how many times do you want to print the message? ")
    print p * x

main()
