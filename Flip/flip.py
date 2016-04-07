# flip.py
# challenge: take in a word/phrase and flip it
# Nov 2014, Ashlyn Kan

from Tkinter import *

root = Tk()
root.title("Word Flipper")

def flip():
    wordlist = []
    flippedWord = ""
    word = entry.get()
    i = len(word)-1
    while i >= 0:
        wordlist.append(word[i])
        i -= 1
    Label(root, text=flippedWord.join(wordlist)).pack()
    
Label(text="Please input the word/phrase you want to flip").pack()
entry = Entry(root)
entry.pack(side=LEFT)
Button(root, text="Flip!", command=flip).pack(side=LEFT)

root.mainloop()
