#if statement
number = 20
if(number > 10):
    print("The given number is greater than 10")

if(number % 2 == 0):
    print(f"{number} is even number")

#if-else statement
if(number % 2 == 0 and number % 5 == 0):
    print(f"{number} is divisible by both 2 & 5")
else:
     print(f"{number} is not divisible by bothn 2 & 5")

#elif statement
num1 = 25
num2 = 35
if(num1 > num2):
    print(f"{num1} is greater than {num2}")
elif(num2 > num1):
    print(f"{num2} is greater than {num1}")
else:
    print(f"{num1} is equal to {num2}")

#shorthan if and if-else
if num1 > num2: print(f"{num1} is greater than {num2}")

#true statement | if condition | else | False
print(f"{num1} is greater than {num2}") if num1 > num2 else print(f"{num2} is greater than {num1}")

#Nested if
# num3 =45
# if(num1 > num2):
#     if(num1 > num3):
#         print(f"{num1} is greatest")
#     else:
#         print(f"{num3} is greatest")
# else:
#      if(num1 > num3):
#         print(f"{num2} is greatest")
#     else:
#         print(f"{num3} is greatest")

#match statement
month = 5
match month:
    case 1:
        print("Janavary")
    