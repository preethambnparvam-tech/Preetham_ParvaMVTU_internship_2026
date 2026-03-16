#Parts of function:
# 1) Function Decleration
# 2) Function Definition
# 3) Function Call

#Function Decleration & Definition
def sayHello():
    print("Hello Students!")

#Function Call
sayHello()
sayHello()
sayHello()

#Function with parameter
def greet(fName):
    print(f"Good Morning, {fName}")

greet("Preetham")

def sum(a,b):
    print(f"Sum of {a} and {b}: {a+b}")

sum(10,20)

#Parameter and Arguments

#Function with Default Parameter
def myIntership(Company="ParvaM"):
    print(f"I'm doing my Internship at {Company}")

myIntership()
myIntership("VTU")

#Function with Return value
def square(number):
    return number**2

SquareOf5 = square(5)
print(f"Square of 5: {SquareOf5}")

#Two types of Functions
# 1)Arbitrary Arguments (*args)
# 2)Arbitrary Keyword Arguments (**kwargs)

def internshipRegistration(*args):
    print("Completed Student List: ", args)

internshipRegistration("Preetham", "Ajay","Tejas", "Dhari")
internshipRegistration()

#Sum of given variable number of arguments
def sumOfNumber(*numbers):
    sum = 0
    for num in numbers:
        sum += num
    return sum
print("Sum: ", sumOfNumber())
print("Sum of 2 Numbers: ", sumOfNumber(2,3))
print("Sum of 5 Numbers: ", sumOfNumber(5,7,10,20))
print("Sum of 8 Numbers: ", sumOfNumber(5,10,20,30,40,50,15,30))

#Combining Regular Argument with Arbitrary Argument
def welcomeStudent(domain,*students):
    for std in students:
        print(f"Hello {std}, Welcome to {domain} Internship")

welcomeStudent("Python", "Preetham", "Sai", "Adarsh")
welcomeStudent("Java", "Tejas", "Darshan", "Swaran")

#Arbitrary Keyword Arguments(**kwargs)
def printLastName(**person):
    print("My Last Name is :", person["lName"])

printLastName(fName = "Preetham", lName = "B N")
printLastName(fName = "Preetham", lName = "Gowda")

def userDetails(**info):
    print("User Details are as follows")
    print("Name:", info["name"])
    print("Email:", info["email"])
    print("Phone Number:", info["phone"])

userDetails(name = "Preetham", email = "preetham@gmail.com", phone = "9663194306")

#Combination of all arguments
def printInfo(title, *args, **kwargs):
    roles = kwargs["roles"]
    depts = kwargs["depts"]

    for name, role, dept in zip(args, roles, depts):
        print(f"{title} of {name}:")
        print(f"    Role: {role}")
        print(f"    Deparment: {dept}")

printInfo("Details","Preetham", "Ajay", roles = ["Assistant Engineer", "Associate Enginner"], depts = ["Web Development", "QA"] )

def printDetails(title, *args, **kwargs):
    for i, name in enumerate(args):
        print(f"{title} of {name}:")

        for key, value in kwargs.items():
            print(f"    {key}: {value[i]}:")

printDetails("Details","Preetham", "Ajay", roles = ["Assistant Engineer", "Associate Enginner"], depts = ["Web Development", "QA"], Experience = [3,1.5] )

names = ["Preetham", "Tejas", "Dhari"]
ages = [21,22,24]
for name in names:
    print(name)

#Enumerate
for index, name in enumerate(names):
    print(index,name)

for index, name in enumerate(names, start =1):
    print(index,name)

#zip
for name, age in zip(names, ages):
    print(name, age)
