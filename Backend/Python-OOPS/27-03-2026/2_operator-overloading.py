# Operator Overloading: The same operator behaves differently depending on the type of operands

# We can achieve in 2 ways:
# 1) Built-in methods
# 2) Special methods (dunder or magic methods)

# Built-in methods:
class Addition:
    def add(self, op1, op2):
        print(f"{op1 + op2}")

operation = Addition()

# Same "+" operator is behaving differenly for each input values:

# Integer Addition
operation.add(2, 5)

# Float Addition 
operation.add(2.5, 5.5)

# String Concatenation
operation.add("Akshay", "Rao")

# Merging 2 lists
operation.add([2, 5], [7, 9, 13])

# "*" operator
class Multiply:

    def mul(self, op1, op2=3):
        print(f"{op1 * op2}")

op = Multiply()

print("\n")
# Integer Multiplication: 5 * 3 =15
op.mul(5)

# Float Multiplication: 5.5 * 3 = 16.5
op.mul(5.5)

# String Multiplication: "Hello" * 3 = "Hello Hello Hello"
op.mul("Hello ")

# List Item Multiplication: [5] * 3 = [5, 5, 5]
op.mul([5])

# "in" - Membership Operator
class Membership:
    def check(self, op1, op2):
        print(f"Is {op1} present in {op2}? {op1 in op2}")

mem = Membership()

print("\n")
mem.check("A", "Akshay Rao")
mem.check(5, [1, 2, 3, 4, 5])
mem.check("a", ["a", "e", "i", "o", "u"])
mem.check("o", ["b", "a", "l", "l"])

# "Comparison Operator (> or <)"
class Comparison:
    def check(self, op1, op2):
        print(f"{op1} is greater than {op2}? {op1 > op2}")

comp = Comparison()

print("\n")
comp.check(50, 65)
comp.check(75.5, 55.8)
comp.check("R", "A")
comp.check([5, 8], [1, 4])

# Indexing Operator('[]')
print("Akshay"[2])
print([5, 7, 9, 3, 6][4])
print((5, 8, 11, 13, 7)[2])

# Magic Methods or Dunder
# Dunder - Double Underscore methods
# (+)__add__, (-)__sub__, (*)__mul__, (/)__truediv__, (==)__eq__,(>) __gt__, (<) __lt__

class StudentMarks:
    def __init__(self, marks):
        self.marks = marks

    def __add__(self, other):
        return self.marks + other.marks
    
    def __sub__(self, other):
        return self.marks - other.marks

    def __gt__(self, other):
        return self.marks > other.marks
    
    def __lt__(self, other):
        return self.marks < other.marks
    
    def __mul__(self, other):
        return self.marks * other.marks
    
    def __eq__(self, other):
        return self.marks == other.marks
    
    def __truediv__(self, other):
        return self.marks / other.marks

# object1 + object2    
sub1 = StudentMarks(94) # Initialization of marks for 1st object (subject)
sub2 = StudentMarks(86) # Initialization of marks for 2md object (subject)

print(sub1 + sub2)
print(sub1 - sub2)
print(sub1 > sub2)
print(sub1 < sub2)
print(sub1 * sub2)
print(sub1 == sub2)
print(sub1 / sub2)

# sub1 + sub2 <=> sub1.__add__(sub2)
# print(sub1.__add__(sub2))
# print(sub1.__sub__(sub2))
# print(sub1.__gt__(sub2))
# print(sub1.__lt__(sub2))
# print(sub1.__eq__(sub2))
# print(sub1.__truediv__(sub2))

fname = StudentMarks("Akshay")
lname = StudentMarks(" Rao")

print(fname.__add__(lname))

# Example 2:
# Ecommerce Mock Usecase
class Product:
    def __init__(self, item, cost):
        self.item = item
        self.cost = cost
        print(f"{item} added to the cart, Rs. {cost}/-")

    def total_cost(self):
        total = self.cost
        return total

    def __add__(self, other):
        return self.cost + other.total_cost()
    
    # __radd__ - Supports multiple value addition: sum()
    def __radd__(self, other):
        return self.cost + other
    
prod1 = Product("Sugar", 45)
prod2 = Product("Salt", 20)
prod3 = Product("Biscuit", 30)
prod4 = Product("Jam", 52)
prod5 = Product("Tea Powder", 26)
prod6 = Product("Horlicks", 95)

products = [prod1, prod2, prod3, prod4, prod5, prod6]

# sum - __radd__
total = sum(products)

print(f"Total Cost: Rs. {total}/-")

# Other Dunder methods:
# __str__, __len__, __setitem__, __getitem__

# __str__(): To print in user-friendly manner
class Employee:
    def __init__(self, emp_id, name, dept, experience):
        self.emp_id = emp_id
        self.name = name
        self.dept = dept
        self.experience = experience

    def __str__(self):
        return(f"Employee ID: {self.emp_id}\nEmployee Name: {self.name}\nEmployee Dept: {self.dept}\nEmployee Experience: {self.experience} yrs\n")

emp1 = Employee("PM-001", "Akshay Rao", "Python - Web Development", 5)

# emp1.__str__()
print(emp1)

# emp1_details = emp1.__str__()
# print(emp1_details)

emp2 = Employee("PM-002", "Murthy", "Java - Web Development", 3)

print(emp2)

# __len__
class Team:
    def __init__(self, members):
        self.members = members

    def __len__(self):
        return len(self.members)
    
parvam = Team(["Akshay", "Murthy", "Pavan", "Mahantesh"])
print(f"No. of Employees in ParvaM: {len(parvam)}")

rcb = Team(("Rajat Patidar", "Virat Kohli", "Phil Salt", "Hazzlewood", "Bhuvaneshwar", "Venkatesh Iyer"))
print(f"No. of Players in RCB: {len(rcb)}")