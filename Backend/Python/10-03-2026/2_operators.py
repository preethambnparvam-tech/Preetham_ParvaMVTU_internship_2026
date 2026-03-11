operand1 = 50
operand2 = 30

#Arithmetic operators:
# +, -, *, /, %

sum = operand1 + operand2
difference = operand1 - operand2
product = operand1 * operand2
quotient = operand1 / operand2
remainder = operand1 % operand2
floor_division = operand1 // operand2

print("Sum: ", sum, "Difference: ", difference, "Product: ", product, "quotient: ", quotient,"Remainder: ", remainder, "Floor Division: ", floor_division )

#Assignment operators:
# =, +=, -=, *=, /=, %=, **=, //=

number = 20
print("Original Number: ", number)
number += 5
print("5 is added to the Number: ", number)
number -= 5
print("5 is subtracted to the Number: ", number)
number *= 5
print("5 is multiplied with the Number: ", number)
number /= 5
print("Number is divided by : ", number)
number = 2
number **= 5
print("Number is updated with power of 5: ", number)

#Comparision Operator:
# >, <, >=, <=, ==,!=

n1 = 25
n2 = 35
print("Number 1 is grater than number 2: ", n1 > n2)
print("Number 1 is lesser than number 2: ", n1 < n2)
print("Number 1 is greater than or eual to number 2: ", n1 >= n2)
print("Number 1 is lesser than or eual to number 2: ", n1 <= n2)
print("Number 1 is eual to number 2: ", n1 == n2)
print("Number 1 is not eual to number 2: ", n1 != n2)

#Logical Operators:
# and, or, not

print("Number 1 is greater than 5 and multiple of 5: ", n1 > 5 and n1 % 5 == 0)

print("Number 2 is lesser than 50 or it can divisible by 4: ", n2 < 5 or n2 % 4 == 0)

print("Number 2 is lesser than 50 and it can divisible by 4: ", not(n2 < 5 and n2 % 4 == 0))

#Identity Operators:
# is and is not

#Membership Operators:
# in and not in 