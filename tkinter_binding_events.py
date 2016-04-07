from Tkinter import *
def motion(event):
  root=Tk()
  root.mainloop()
  return

master = Tk()
whatever_you_do = "Whatever you do will be insignificant, but it is very important that you do it.\n(Mahatma Gandhi)"
msg = Message(master, text = whatever_you_do, cursor="hand2")
msg.config(bg='lightgreen', font=('times', 24, 'italic'))
msg.bind('<Button-1>',motion)
msg.pack()
mainloop()
