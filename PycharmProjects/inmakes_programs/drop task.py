from tkinter import *
root=Tk()
def fun():
    print("this is for new project")
def fun1():
    print("this is for new ")
def fun2():
    print("this is for New Scratch file ")
def fun3():
    print("this is for Open ")
def fun4():
    print("this is for Learn")
def fun5():
    print("this is for close project")
def fun6():
    print("this is for new ")

mymenu=Menu(root)
root.config(menu=mymenu)
submenu=Menu(mymenu)
mymenu.add_cascade(label="File",menu=submenu)
submenu.add_command(label="New project",command=fun)
submenu.add_command(label="New",command=fun1)
submenu.add_separator()
submenu.add_command(label="New Scratch file",command=fun2)
submenu.add_command(label="Open",command=fun3)
submenu.add_separator()
submenu.add_command(label="Learn",command=fun4)
submenu.add_command(label="Close project",command=fun5)
submenu.add_separator()
submenu.add_command(label="Exit",command=exit)
def fun7():
    print("this is for Undo")
def fun8():
    print("this is for Cut")
def fun9():
    print("this is for Copy")
def fun10():
    print("this is for Paste")
def fun11():
    print("this is for Delete")
def fun12():
    print("this is for Find")
newmenu=Menu(mymenu)

mymenu.add_cascade(label="Edit",menu=newmenu)
newmenu.add_command(label="Undo",command= fun7)
newmenu.add_command(label="Cut",command= fun8)
newmenu.add_separator()
newmenu.add_command(label="Copy",command= fun9)
newmenu.add_command(label="Paste",command= fun10)
newmenu.add_separator()
newmenu.add_command(label="Delete",command= fun11)
newmenu.add_command(label="Find",command= fun12)
nmenu=Menu(mymenu)
def fun13():
    print("this is for Toolwindows")
def fun14():
    print("this is for Toolbar")
def fun15():
    print("this is for Appearence")
def fun16():
    print("this is for Type Info")
def fun17():
    print("this is for Content Info")
def fun18():
    print("this is for Recent Files")
mymenu.add_cascade(label="View",menu=nmenu)
nmenu.add_command(label="Toolwindows",command= fun13)
nmenu.add_command(label="Toolbar",command= fun14)
nmenu.add_separator()
nmenu.add_command(label="Appearence",command= fun15)
nmenu.add_command(label="Type Info",command= fun16)
nmenu.add_separator()
nmenu.add_command(label="Content Info",command= fun17)
nmenu.add_command(label="Recent Files",command= fun18)
mmenu=Menu(mymenu)
def fun19():
    print("this is for Back")
def fun20():
    print("this is for Class")
def fun21():
    print("this is for File")
def fun22():
    print("this is for Symbol")
def fun23():
    print("this is forLine:column..")
def fun24():
    print("this is for Navigate in File")
mymenu.add_cascade(label="Navigate",menu=mmenu)
mmenu.add_command(label="Back",command= fun19)
mmenu.add_command(label="Class",command= fun20)
mmenu.add_separator()
mmenu.add_command(label="File",command= fun21)
mmenu.add_command(label="Symbol",command= fun22)
mmenu.add_separator()
mmenu.add_command(label="Line:column..",command= fun23)
mmenu.add_command(label="Navigate in File",command= fun24)


Nmenu=Menu(mymenu)
Nmenu=Menu(mymenu)
def fun25():
    print("this is for Find Action")
def fun26():
    print("this is for Help")
def fun27():
    print("this is for Contact support")
def fun28():
    print("this is for submit feedback")
def fun29():
    print("this is for Tip of the day")
def fun30():
    print("this is for About")
mymenu.add_cascade(label="Help",menu=Nmenu)
Nmenu.add_command(label="Find Action",command= fun25)
Nmenu.add_command(label="Help",command= fun26)
Nmenu.add_separator()
Nmenu.add_command(label="Contact support",command= fun27)
Nmenu.add_command(label="submit feedback",command= fun28)
Nmenu.add_separator()
Nmenu.add_command(label="Tip of the day",command= fun29)
Nmenu.add_command(label="About",command= fun30)


root.mainloop()
