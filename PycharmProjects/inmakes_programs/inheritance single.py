class student:
    def __init__(self,name,mark):
        self.name=name
        self.mark=mark
    def getd(self):
        self.name=input("enter the name:")
        self.mark=int(input("enter the mark:"))
    def putd(self):
        print(self.name,self.mark)
class teacher(student):
    def view(self):
        print("am derived class")
pta=teacher('','')
pta.getd()
pta.putd()
pta.view()

