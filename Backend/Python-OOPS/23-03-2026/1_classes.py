#syntax:
# class ClassName:
#variables or data members(attributes)
#methods or functions(behaviour)

# 100 students data with name, age, roll number, marks in 5 subjects
class Student:
    def __init__(self, name, age, roll_number, marks):
        self.name = name
        self.age = age
        self.roll_number = roll_number
        self.marks = marks

    def printDetails(self):
        print("Student Details will be displayed here")
        print(f"Name of the student: {self.name}, he is {self.age} years old, his roll number is {self.roll_number} and his marks in 5 subjects are {self.marks}")

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Roll Number: {self.roll_number}")
        print(f"Marks: {self.marks}")

student1 = Student(name = "Dhari", age = 20, roll_number = 1, marks = [85, 90, 88, 92, 95])
student1.display()

student2 = Student(name = "Preetham", age = 21, roll_number = 2, marks = [80, 85, 82, 88, 90])
student2.display()

student3 = Student(name = "Tejas", age = 19, roll_number = 3, marks =   [78, 82, 80, 85, 87])
student3.display()

Student.printDetails(student1)

Student.printDetails(student2) 

Student.printDetails(student3)

student1.printDetails()
student2.printDetails()
student3.printDetails()