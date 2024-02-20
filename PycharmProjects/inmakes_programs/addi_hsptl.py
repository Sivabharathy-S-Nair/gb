class hospital:
    def __init__(self,admin,doctor,sister,department):
        self.admin=admin
        self.doctor=doctor
        self.sister=sister
        self.department=department
    def get(self):
        self.admin=input("enter admin name:")
        self.doctor=input("enter doctor name:")
        self.sister=input("enter sister name:")
        self.department=input("enter department name:")
class d:
    def display(self,admin,doctor,sister,department,):
        print( self.admin,self.doctor,self.sister,self.department)
class patientward(d,hospital):
    def __init__(self,name,age,number,disease):
        self.name=name
        self.age=age
        self.number=number
        self.disease=disease
    def  patientdetails(self):
        self.name=input("enter patient name:")
        self.age=int(input("enter your age:"))
        self.number=int(input("enter your number:"))
        self.disease=input("enter your disease:")
    def view(self):
        print(self.name,self.age,self.number,self.disease)
o=patientward('','','','')
o.get()
o.display('','','','')
o.patientdetails()
o.view()
