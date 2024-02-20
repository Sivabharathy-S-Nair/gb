from tkinter import *
class hospital:
    def __init__(self,rootone):
        frame=Frame(rootone)
        frame.pack()
        self.label=Label(frame,text="doctorname")
        self.label.pack()
        self.label1=Label(frame,text="patientname")
        self.label1.pack()
        self.label2=Label(frame,text="number")
        self.label2.pack()
        self.pbutton=Button(frame,text="click",command=self.pmsg)
        self.pbutton.pack(side=LEFT)
        self.cbutton=Button(frame,text="cancel",command=self.pmsg1)
        self.cbutton.pack(side=LEFT)
        self.qbutton=Button(frame,text="quit",command=quit)
        self.qbutton.pack()
    def pmsg(self):
        print("clicked")
    def pmsg1(self):
        print("cancelled")

root=Tk()
obj=hospital(root)
root.mainloop()
