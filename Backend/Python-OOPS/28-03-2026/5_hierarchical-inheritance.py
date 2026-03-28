# 1 Parent with multiple Children
# A Base Class derives multiple "Derived Class"
class A:
    def printA(self):
        print("This is class A\n")

class B(A):
    def printB(self):
        print("This is class B\n")

class C(A):
    def printC(self):
        print("This is class C\n")

class D(A):
    def printD(self):
        print("This is class D\n")


b = B()
b.printA()
b.printB()

c = C()
c.printA()
c.printC()

d = D()
d.printA()
d.printD()

#Exaple 2
class Animal:
    def eat(self):
        print(f"is eating\n")

class Dog(Animal):
    def bark(self):
        super().eat()
        print(f"is barking\n")

class Cat(Animal):
    def meow(self):
        super().eat()
        print(f"is meowing\n")

# Creating objects
print("--- Dog Object ---")
dog = Dog()
dog.eat()
dog.bark()

print("--- Cat Object ---")
cat = Cat()
cat.eat()
cat.meow()

#Example 3
class Vehicle:
    def __init__(self,brand):
        self.brand=brand

    def displayBrand(self):
        print(f"Brand is {self.brand}\n")

class Car(Vehicle):
    def __init__(self,brand,model):
        super().__init__(brand)
        self.model=model

    def displayModel(self):
        print(f"Model is {self.model}\n")

class Bike(Vehicle):
    def __init__(self,brand,model):
        super().__init__(brand)
        self.model=model

    def displayModel(self):
        print(f"Model is {self.model}\n")

# Creating objects
print("--- Car Object ---")
car = Car("Toyota","Camry")
car.displayBrand()
car.displayModel()

print("--- Bike Object ---")
bike = Bike("Honda","CBR")
bike.displayBrand()
bike.displayModel()