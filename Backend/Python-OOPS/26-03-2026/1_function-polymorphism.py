#Built-In Polymorphism

name = "Preetham"
hobbies = ["Coding", "Traveling", "Cooking", "Gaming"]
skills = {"Python": "Advanced", "Java": "Intermediate", "C++": "Beginner"}

# Demonstrating polymorphism with built-in functions
print("Length of name: ", len(name))
print("Length of hobbies: ", len(hobbies))
print("Length of skills: ", len(skills))

#type() function demonstrates polymorphism by returning the type of the object
print("Type of name: ", type(name)) 
print("Type of hobbies: ", type(hobbies))
print("Type of skills: ", type(skills))

#sum() function demonstrates polymorphism by calculating the sum of numbers in a list
print(sum([1, 2, 3, 4, 5])) 
print(sum((10, 20, 30)))
print(sum({1,2,3,4,5}))

# Custom Method
def display(value):
    print(f"Given value: {value}, It is of type: {type(value)}")

display("Preetham")
display(50)
display(50.5)
display([1, 2, 3, 15])

def findArea(sides, side1, side2 = None, side3 = None):
    if sides == 1:
        shape = "Square"
        print(f"Shape: {shape}, Area of {shape}: {side1 * side1}")
    elif sides == 2:
        shape = "Rectangle"
        print(f"Shape: {shape}, Area of {shape}: {side1 * side2}")
    elif sides == 3:
        shape = "Cube"
        print(f"Shape: {shape}, Area of {shape}: {6 * side2 * side3}")

findArea(1, 5)
findArea(2, 5, 10)
findArea(3, 5, 10, 15)