'''
gmail_authentication.py

This app mimics the communication between database and user
when they sign up or log in, using the concept of opening, reading,
and writing files. However, the database in this app is served by a 
local .txt file and no actual email threads are associated with each user.

October 2014, Ashlyn Kan
'''

from Tkinter import *
import tkMessageBox
import sys
import webbrowser

app = Tk()
app.geometry("300x200")
app.title("Gmail Authentication")
    

def signUp():

    def signUpGo():

        firstName = firstNameEntry.get()
        lastName = lastNameEntry.get()
        username = usernameEntry.get()
        password = passEntry.get()
        passConfirm = passConfirmEntry.get()

        if password == passConfirm:
        
            with open("gmaildatabase.txt", "r+") as f:
                oldLines = f.read() # read everything in the file
                f.seek(0)      # rewind
                f.write(firstName)
                f.write('\n')
                f.write(username)
                f.write('\n')### to write in one line at a time
                f.write(password)
                f.write('\n')
                f.write(oldLines)
 

            tkMessageBox.showinfo('Info', "You've successfully signed up!")
            signUpWindow.destroy()
            signIn()
            
            
        else:
            tkMessageBox.showinfo('Info', "Error: Passwords don't match")

    
    signUpWindow = Tk()
    signUpWindow.geometry("300x380")
    signUpWindow.title("Sign up - Gmail")
    
    Label(signUpWindow, text="Create an account with Google", height=3).pack()
    
    Label(signUpWindow, text="First Name").pack()
    firstNameEntry = Entry(signUpWindow)
    firstNameEntry.pack()
    
    Label(signUpWindow, text="Last Name").pack()
    lastNameEntry = Entry(signUpWindow)
    lastNameEntry.pack()
    
    Label(signUpWindow, text="Username").pack()
    usernameEntry = Entry(signUpWindow)
    usernameEntry.pack()
    
    Label(signUpWindow, text="Password").pack()
    passEntry = Entry(signUpWindow, show="*")
    passEntry.pack()
    
    Label(signUpWindow, text="Confirm Password").pack()
    passConfirmEntry = Entry(signUpWindow, show="*")
    passConfirmEntry.pack()


    Button(signUpWindow, text="Sign up", command=signUpGo, height=3).pack()


def signIn():

    def readTokens(fileName):
        tokens = []
        file = open(fileName)
        Token = file.readline()
        while Token:
            Token = Token.strip()
            if len(Token) > 0:
                tokens.append(Token)
            Token = file.readline()
        file.close()
        return tokens

    def signInGo():
        returnToken = readTokens("gmaildatabase.txt")
        print returnToken
        username = userEntry.get()
        password = passEntry.get()

        i = 1
        while i < len(returnToken):
            try:
                username == returnToken[i] and password == returnToken[i+1]
            except ValueError:
                tkMessageBox.showinfo('Info', "Error: wrong username or password")
            else:
                tkMessageBox.showinfo('Info', "We're taking you to your inbox")
                signInWindow.destroy()
                app.destroy()
                openBrowser()
                sys.exit()
            i += 2
            
    
    signInWindow = Tk()
    signInWindow.geometry("300x200")
    signInWindow.title("Sign in - Gmail")

    Label(signInWindow, text="Sign in to your inbox", height=2).pack()
    
    Label(signInWindow, text="Username:").pack()
    userEntry = Entry(signInWindow)
    userEntry.pack()
    
    Label(signInWindow, text="Password:").pack()
    passEntry = Entry(signInWindow, show="*")
    passEntry.pack()
    

    Button(signInWindow, text="Sign In", command = signInGo, height=2).pack()
    

def openBrowser():
    url = "http://www.gmail.com"
    webbrowser.open_new(url)
    

Label(app, text="Welcome to Gmail! You can either:", height = 4).pack()
Button(app, text="Sign up", command=signUp).pack()
Label(app, text="Or", height=2).pack()
Button(app, text="Sign in", command=signIn).pack()



app.mainloop()
