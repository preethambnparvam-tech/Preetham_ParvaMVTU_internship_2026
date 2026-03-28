class Computer:
    def __init__(self,ram,rom,type,generation):
        self.ram=ram
        self.rom=rom
        self.processor = self.Processor(type, generation)

    def displayConfig(self):
        print(f"Computer has {self.ram} RAM and {self.rom}  ROM")
        self.processor.internalDetails()

    class Processor:
        def __init__(self,type,generation):
            self.type=type
            self.generation=generation

        def internalDetails(self):
            print(f"Processor is {self.type} of {self.generation} generation")



comp1=Computer("8GB","512GB","Intel","12th gen")
comp1.displayConfig()

comp2=Computer("16GB","1TB","AMD","13th gen")
comp2.displayConfig()

#Example 2
class Car:
    def __init__(self, brand, model, engine_type, horsepower):
        self.brand = brand
        self.model = model
        # Instantiating the inner class
        self.engine = self.Engine(engine_type, horsepower)
    def display_info(self):
        print(f"Car: {self.brand} {self.model}")
        # Calling a method from the inner class
        self.engine.display_engine_specs()
    # Inner class
    class Engine:
        def __init__(self, engine_type, horsepower):
            self.engine_type = engine_type
            self.horsepower = horsepower
        def display_engine_specs(self):
            print(f"Engine Specs -> Type: {self.engine_type}, Horsepower: {self.horsepower} HP")
# Creating Car objects
print("\n")

car1 = Car("Toyota", "Camry", "V6", 301)
car1.display_info()

print("-" * 30)

car2 = Car("Tesla", "Model S", "Electric Motor", 1020)
car2.display_info()

#Example 3
class University:
    def __init__(self,name,affliated, college, cet_code,type,location):
        self.name=name
        self.affliated=affliated
        self.college=self.College(college,cet_code,type,location)

    def info(self):
        print(f"{self.name} University is affliated to {self.affliated}") 
        self.college.info()

    class College:
        def __init__(self,college,cet_code,type,location):
            self.college=college
            self.cet_code=cet_code
            self.type=type
            self.location=location

        def info(self):
            print(f"College is {self.college} with CET code {self.cet_code} of type {self.type} and location {self.location}")

print("\n")
# Creating University objects
university1 = University("VTU", "Karnataka", "BMS College of Engineering", "CET", "Government", "Bangalore")
university1.info()

print("-" * 30)

university2 = University("VTU", "Karnataka", "RV College of Engineering", "CET", "Government", "Bangalore")
university2.info()
