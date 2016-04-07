# Hangman game in Python
# Sep 11, 2014
# Ashlyn Kan

import random
import sys

print "Welcome to the hangman game!!"
print "_ is a normal character"
print "* is a vowel"
print "Only input one character at a time."

def readWords(fileName):
    words = []
    file = open(fileName)
    word = file.readline()
    while word:
        word = word.strip()      # remove line endings
        if len(word) > 0:       # ignore blank lines
            words.append(word) # notice the 'eval'
        word = file.readline()
    file.close()
    return words

def main():
    tup = readWords("words.txt")
    a = []
    for i in range(len(tup)):
        s = random.choice(tup)
        a.append(s)
    return a
        
def playGame():
    i = 0
    x = random.choice(main())
    y = list(x)
    z = list(x)

    #print y

    for i in range(len(z)):
        if (z[i] == "A" or z[i] == "E" or z[i] == "E" or z[i] == "I" or z[i] == "O" or z[i] == "U"):
            z[i] = "*"
        else:
            z[i] = "_"
    print "The word is:",z

    check = z.count("_") + z.count("*")
    trial = 9

    print "You have 9 trial."
    
    while trial <= 9:
        i = 0
        uInput = raw_input("guess a character: ").upper()
        multiChars(uInput)
        
        for i in range(len(x)):
            if (y[i] == uInput):
                z[i] = uInput

        if (z.count('_') + z.count('*') == check):
            trial -= 1
            print "Sorry, incorrect!"
            print "Trial left: ",trial
        else:
            print "Correct!"
            check = z.count('_') + z.count('*')
        print z
        
        if (z.count('_') + z.count('*') == 0):
            print "You win!"
            pass
            playAgain()
            
        gameOver(trial,y)

def playAgain():
    again = raw_input("Play again? [y/n] ").lower()
    if again == 'y':
        playGame()
    else:
        print "Bye-bye."
        sys.exit()

def multiChars(u):
    if len(u) > 1:
        print "Invalid: multiple characters detected."
        playAgain()

def gameOver(trial,y):
    if (trial == 0):
        print "Game over!"
        print y
        pass
        playAgain()
        
main()
playGame()
