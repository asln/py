# Flashcards.py
# Feb 2014, Ashlyn Kan

import sys
import re
from random import shuffle

def main():
    print("Welcome to the Monkey Flashcards!")
    print("To begin sharpening your memory, please input the path to the file")
    print("To quit at any time, type Exit")

def Exit():
    print("The Monkey Flashcards is closing now.. Bye-bye!")
    sys.exit(0)

def readFlashcards():
    with open("state-capitals.txt") as f:
        cards = f.readlines()
        print("There're " + str(len(cards)) + " flashcards")
        goThroughTimes = int(input("How many flashchards would you like to go through?  "))
        shuffle(cards)
        gotRight = 0
        for line in cards[:goThroughTimes]:
            flashcard, flashcardFlipped = line.strip().split(",") # split questions and answers by comma to store in different variables
            flashcard = re.sub('[!@#$()""]', '', flashcard)
            flashcardFlipped = re.sub('[!@#$()""]', '', flashcardFlipped)
            flashcardFlipped = flashcardFlipped.strip(' ')
            answer = raw_input(flashcard + '\n')
            if (answer.title() == flashcardFlipped):  # use .title() to ignore user's decapitalization
                print("You little genius!")
                gotRight = gotRight + 1
            elif (answer.capitalize() == "Exit"):
                Exit()
            else:
                print "Try again! Hint: starts with" , flashcardFlipped[0]  # [2] should be [0] after get rid of the space, " , and (
                answer = raw_input(flashcard + '\n')
                if (answer.title() == flashcardFlipped):
                    print("Now you got it!")
                    gotRight = gotRight + 0.5
                elif (answer.capitalize() == "Exit"):
                    Exit()
                else:
                    print "Oh no, still wrong! Answer is" , flashcardFlipped
                    raw_input("Typing in the answer will help you remember:  ")
        rightPercentage = float(gotRight / goThroughTimes * 100)
        print "You got %.2f" %(rightPercentage) , "% right!"  # round the float to 2 decimals
        if rightPercentage >= 80:
            print ("You're a Monkey Lord!")

main()
path = raw_input("For path to State-Capitals flashcards, type state-capitals.txt\n")
if path == ("state-capitals.txt"):
    readFlashcards()
elif path.capitalize() == ("Exit"):
    Exit()
else:
    print ("wrong path!")
    
    
    
