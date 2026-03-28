# Multiple Inheritance will have 2 or more Parent with 1 Child
# A     B
#    c

#Example 1
class A:
    def printA(self):
        print("Class A is a base Class\n")

class B:
    def printB(self):
        print("Class B is also a base Class\n")

class C(A,B):
    def printC(self):
        print("Class C is a derived from Class A and Class B\n")

# Object of Class A
a = A()
a.printA()

# Object of Class B
b = B()
b.printB()

# Object of Class C
c = C()
c.printA()
c.printB()
c.printC()


#Example 2
class Father:
    def printFatherInfo(self):
        print(f"Father's name is Nagaraju B N\n")

class Mother:
    def printMotherInfo(self):
        print(f"Mother's name is Savitha B N\n")

class Child(Father,Mother):
    def printChildInfo(self):
        print(f"Child's name is Preetham B N\n")

# Object of Class Child
child = Child()
child.printFatherInfo()
child.printMotherInfo()
child.printChildInfo()

#Example 3
class Camera:
    def printCameraInfo(self):
        print(f"This is a camera\n")

class Phone:
    def printPhoneInfo(self):
        print(f"This is a phone\n")

class Smartphone(Camera,Phone):
    def printSmartphoneInfo(self):
        print(f"This is a smartphone\n")

# Object of Class Smartphone
smartphone = Smartphone()
smartphone.printCameraInfo()
smartphone.printPhoneInfo()
smartphone.printSmartphoneInfo()