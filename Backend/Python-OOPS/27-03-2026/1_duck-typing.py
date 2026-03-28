#It is a type of polymorphism in Python
# #"If it looks like a duck and quacks like a duck, then it must be a duck"

class Duck:
    def eat(self):
        print("Duck is eats Biscuits")

    def makeSound(self):
        print("Duck says Quack!")

    def sleep(self):
        print("Duck is sleeping")

class Dog:
    def eat(self):
        print("Dog is eats Dog food")

    def makeSound(self):
        print("Dog says Woof!")

    def sleep(self):
        print("Dog is sleeping") 

class Cat:
    def eat(self):
        print("Cat is eats fish")

    def makeSound(self):
        print("Cat says Meow!")

    def sleep(self):
        print("Cat is sleeping peacefully")

d1 = Dog()

d1.eat()
d1.makeSound()
d1.sleep()

c1 = Cat()

c1.eat()
c1.makeSound()
c1.sleep()

duck1 = Duck()

duck1.eat()
duck1.makeSound()   
duck1.sleep()

#Example 2

class Item:
    def fly(self, item):
        print(f"{item} is flying in the sky")

    def lives(self, item, type):
        print(f"{item} lives in the {type} object\n")

#object
aeroplane = Item()
aeroplane.fly("Aeroplane")
aeroplane.lives("Aeroplane", "Non-living")

#object
bird = Item()
bird.fly("Bird")
bird.lives("Bird", "Living")

#object
superman = Item()
superman.fly("Superman")
superman.lives("Superman", "Non-living")

#Example 3
class Email:
    def send_email(self):
        print("Message sent to email")

class Whatsapp:
    def send_message(self):
        print("Message sent to Whatsapp")

class Telegram:
    def send_message(self):
        print("Message sent to Telegram")

class Letter:
    def send_message(self):
        print("Message sent to Letter")

def notify(mode):
    mode.sendMessage()

e = Email()
w = Whatsapp()  
t = Telegram()
l = Letter()

print("\n")
notify(e)
notify(w)   
notify(t)
notify(l)
