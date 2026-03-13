#while loop
i = 0
while i < 10:
    print(f"{i}")
    i += 1

print("Even number from 10 to 20")
while i < 20:
    if i % 2 == 0:
        print(i)
    i += 1

print("Odd number from 20 to 30")
while i <= 30:
    if i % 2 != 0:
        print(i)
    i += 1

#while loop



#for loop
x = 1
for x in range(11):
    print(x)

for x in range(20):
    if x % 3 ==0:
        print(x)

print("Multiples of 3 from 10 to 30:")
for x in range(10, 30):
    if x % 3 == 0:
        print(x)

print("Multiples of 5:")
for x in range(0,21,5):
    print(x)

#for loop with list, tuple
milkProduct = ["Milk", "Curd", "Butter", "Panner", "Cheese"]
print(milkProduct)

for item in milkProduct:
    print(item)

#tuple
movie = ["KGF", "KD", "Toxic", "Kantara"]
print(movie)

for movie in movie:
    print(movie)

#Nested for loop
language = ["Kannada", "Tamil", "Marati", "Hindi"]
states = ["Karnataka", "Tamil nadu", "Maharastra", "Delhi"]

for state in states:
    for lang in language:
        print(f"{state}, {lang}")

#Functions, Math Method and date Method