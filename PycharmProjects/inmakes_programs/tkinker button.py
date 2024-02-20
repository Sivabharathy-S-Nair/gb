
from tkinter import *
root=Tk()
Label(root,text="hello ").pack()
#Button(root,text="login").pack()
frame1=Frame(root)
frame1.pack()
but=Button(frame1,text="login",fg="red",bg="violet")
but.pack()
root.mainloop()
