#Single Inheritance
#"Base Class" Derives a "Derived Class"
#"Derived Class" is derived by a "Base Class"

#Example 1
# A -> B
# Base Class
class A:
    def show(self):
        print("This is class A\n")

# Derived Class
class B(A):
    def display(self):
        print("This is class B\n")

# Creating objects
a = A()
a.show()

b=B()
b.show()
b.display()


#Example 2
class Vehicle:
    def showVehicleInfo(self):
        print("This is a vehicle\n")

class Car(Vehicle):
    def showCarInfo(self):
        print("This is a car\n")

# Creating objects
vehicle = Vehicle()
vehicle.showVehicleInfo()

car = Car()
car.showVehicleInfo()
car.showCarInfo()


#Example 3
class Computer:
    def __init__(self,ram,rom):
        self.ram=ram
        self.rom=rom

    def displayBasicInfo(self):
        print(f"This is a computer with {self.ram} RAM and {self.rom} ROM\n")

class Laptop(Computer):
    def __init__(self,processor,ram,rom,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
        super().__init__(processor,ram,rom)

    def displayInfo(self):
        print(f"This is a laptop with {self.brand} {self.model} {self.price} and {self.brand} Brand and {self.model} Model\n")

# Creating objects
laptop1  = Laptop("Dell","XPS 15","150000")
laptop1.displayInfo()
laptop1.displayBasicInfo()

laptop2 = Laptop("HP","Spectre x360","120000")
laptop2.displayInfo()
laptop2.displayBasicInfo()

