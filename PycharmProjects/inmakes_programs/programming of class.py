class student:
    def __init__(self,name,mark):
        self.name=name
        self.mark=mark
    def getdetails(self):
        self.name=input("enter student name:")
        self.mark=int(input("enter your mark:"))
        #print(self.name,self.mark)
    def putdetails(self):
        print(self.name,self.mark)

please=student('','')
please1=student('','')
please.getdetails()
please1.getdetails()
please.putdetails()
please1.putdetails()
