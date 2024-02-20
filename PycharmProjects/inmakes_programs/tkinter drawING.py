from tkinter import *
root=Tk()
canvas=Canvas(root,width=100,height=100)
canvas.pack()
#canvas.create_line(0,0,8,90)
newline=canvas.create_line(0,0,8,90)
newline1=canvas.create_line(10,10,10,80)
root.mainloop()
