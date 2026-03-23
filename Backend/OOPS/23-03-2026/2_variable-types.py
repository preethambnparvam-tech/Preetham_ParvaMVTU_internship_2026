# In python OOPs, there are two types of variables:
# Instance variables & Class variables

class Internship:
    # class variable
    company = "ParvaM"
    duration = "15 weeks"

    def __init__(self, name, college, branch, internship):
        # instance variables
        self.name = name
        self.college = college
        self.branch = branch
        self.internship = internship

    def enroll(self):
        print(f"{self.name}, Thank you for enrolling in {Internship.company} for {self.internship} Internship")  

    def jointClass(self):
        print("Joint class will be conducted for all the interns enrolled in ParvaM")

    def practice(self):
        print("Practice on the concepts learned in the class")

    def interview(self):
        print("Interview will be conducted at the end of the internship. \n") 

#Object Creation or Inintialization of the class

std1 = Internship(name = "Dhari", college = "AIEMS", branch = "CSE", internship = "Backend")

std2 = Internship(name = "Preetham", college = "MVJ", branch = "CSE", internship = "Backend")

#Internship.company = "ParvaMVTU"

std1.enroll()
std1.jointClass()
std1.practice()
std1.interview()

std2.enroll()
std2.jointClass()
std2.practice()
std2.interview()

#Example 2
class car:
    #class variable
    mode_of_transport = "Road"
    no_of_wheels = 4

    def __init__(self, brand, model, fuel_type, color, price):
         #instance variables
        self.carbrand = brand
        self.carmodel = model
        self.fuel_type = fuel_type
        self.carcolor = color
        self.price = price

    def demo(self):
        print(f"{self.carbrand} {self.carmodel} is a {self.fuel_type} car, it is {self.carcolor} in color and costs {self.price} rupees")

    def driveCar(self):
        print(f"{self.carbrand} {self.carmodel} is being driven on the {car.mode_of_transport}")

    def refillFuel(self):
        print(f"Refilling {self.fuel_type} in the {self.carbrand} {self.carmodel}")

    def parkCar(self):
        print(f"Parking the {self.carbrand} {self.carmodel} in the parking lot. \n")

car1 = car(brand = "Tesla", model = "Model S", fuel_type = "Electric", color = "Red", price = 8000000)

car2 = car(brand = "BMW", model = "X5", fuel_type = "Petrol", color = "Black", price = 7000000)

car1.demo()
car1.driveCar()
car1.refillFuel()
car1.parkCar()

car2.demo()
car2.driveCar()
car2.refillFuel()
car2.parkCar()
