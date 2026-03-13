# 1. Function that prints Welcome message
def welcome():
    print("Welcome to Python Programming")
welcome()

# 2. Function with Parameters (Sum of two numbers)
def add_numbers(a, b):
    print("Sum:", a + b)
add_numbers(5, 10)

# 3. Function with Return (Square of a number)
def square(n):
    return n * n
result = square(4)
print("Square:", result)

# 4. Default Parameter Function
def greet(name="Student"):
    print("Hello", name)
greet()
greet("Preetham")

# 5. Keyword Arguments
def student(name, age):
    print("Name:", name)
    print("Age:", age)
student(age=20, name="Rahul")

# 6. Variable Length Arguments (*args)
def total_sum(*numbers):
    print("Sum:", sum(numbers))
total_sum(10, 20, 30, 40)

# 7. Keyword Variable Arguments (**kwargs)
def student_details(**data):
    for key, value in data.items():
        print(key, ":", value)
student_details(name="Preetham", age=21, course="Python")

# 8. Lambda Function
multiply = lambda a, b: a * b
print("Multiplication:", multiply(5, 4))

# 9. Recursion (Factorial)
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print("Factorial:", factorial(5))

# 10. Scope of Variables (Local & Global)
x = 10  
def show():
    x = 5  
    print("Local x:", x)
show()
print("Global x:", x)