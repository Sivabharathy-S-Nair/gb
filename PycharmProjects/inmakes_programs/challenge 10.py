class vehicle:
    def __init__(self,bodytype,engine):
        self.bodytype=bodytype
        self.engine=engine
    def getspecs(self):
        self.bodytype=input("enter the bodytype:")
        self.engine=input("enter the engine:")
    def displayspecs(self):
        print(self.bodytype,self.engine)
class car(vehicle):
    def __init__(self,wheel):
        self.wheel=wheel
    def details(self):
        self.wheel=input("does the car wheel have mark on it?")
    def display(self):
        print(self.wheel)
class bike:
    def __init__(self,wheel):
        self.wheel=wheel
    def details(self):
        self.wheel=input("does the car wheel have mark on it?")
    def view(self):
        print(self.wheel)
car1=car('')
car1.getspecs()
car1.displayspecs()
car1.details()
car1.display()

