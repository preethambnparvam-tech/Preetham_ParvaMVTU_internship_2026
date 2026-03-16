#Methods: min,max,abs,pow

numbers = [2,7,3,5,9,6]

#min
minValue = min(numbers)

#max
maxValue = max(numbers)

print(f"Min value: {minValue}, Max value: {maxValue}")

#abs
negative = [-3,2,-5,4]
for num in negative:
    print(abs(num))

#pow
print(f"5^2: {pow(5,2)}")

#Math Module Methods: sqrt, sin, cos, tan, ceil, floor, isnan, issqrt, prod, remainder

import math

#sqrt
print(f"Square Root of 25: {math.sqrt(25)}")

#issqrt
print(f"Square Root of 27: {math.isqrt(27)}")

#ceil & floor
number = 2.75
print(f"Cell Value of {number}: {math.ceil(number)}")
print(f"Floor Value of {number}: {math.floor(number)}")

#sin, cos, tan
print(f"Sine of 90: {math.sin(90)}")
print(f"Cos of 90: {math.cos(90)}")
print(f"Tan of 90: {math.tan(90)}")

#remainder
print(f"You need {math.remainder(32,7)} to divide 31 completly by 3")

#isnan
