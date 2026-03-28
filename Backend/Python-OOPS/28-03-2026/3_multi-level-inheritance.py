#Multi-Level Inheritance
# Derived Class derives a new Derived Class
# Base Class -> Derived Class1 -> Derived Class2
# Base Class(Level 1) -> Base Class(Level 2) -> Base Class(Level 3)

#Example 1
# A -> B -> C
# Base Class
class A:
    def printA(self):
        print("This is class A\n")

# Derived Class
class B(A):
    def printB(self):
        print("This is class B\n")

# Base Class
class C(B):
    def printC(self):
        print("This is class C\n")

# Creating objects
b = B()
b.printA()
b.printB()

c = C()
c.printA()
c.printB()
c.printC()


#Example 2
# Animal -> Mammal -> Dog

# Base Class
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating...\n")

# Derived Class 1 (Intermediate)
class Mammal(Animal):
    def __init__(self, name, has_fur):
        super().__init__(name)
        self.has_fur = has_fur

    def walk(self):
        fur_status = "has fur" if self.has_fur else "has no fur"
        print(f"{self.name} (Mammal, {fur_status}) is walking...\n")

# Derived Class 2
class Dog(Mammal):
    def __init__(self, name, has_fur, breed):
        super().__init__(name, has_fur)
        self.breed = breed
        
    def bark(self):
        print(f"{self.name} the {self.breed} is barking...\n")

# Creating objects
print("--- Dog Object ---")
d = Dog("Buddy", True, "Golden Retriever")
d.eat()   
d.walk()  
d.bark()  

#Example 3
class Device:
    def __init__(self, type):
        self.type = type

    def display_device(self):
        print(f"This is a {self.type}\n")

class PowerType(Device):
    def __init__(self, type, current):
        super().__init__(type)
        self.current = current

    def display_type(self):
        super().display_device()
        print(f"It uses {self.current} current for Power Supply\n")

class Gadget(PowerType):
    def __init__(self, type, current, gadget_name):
        super().__init__(type, current)
        self.gadget_name = gadget_name

    def display_gadget(self):
        print(f"It is a {self.gadget_name}\n")

# Creating objects
print("--- Gadget Objects ---")
mobile = Gadget("Electronics", "5V", "Mobile")
mobile.display_device()

mixer = Gadget("Appliance", "230V", "Mixer")
mixer.display_device()


calculator = Gadget("Electronics", "3V", "Calculator")
calculator.display_device()

