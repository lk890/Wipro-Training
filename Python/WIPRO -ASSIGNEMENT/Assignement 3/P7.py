# Use the Math Module:
# Write a program that imports the math module and uses it to:
# Find the square root of a number.
# Calculate the sine of an angle .
# Find the greatest common divisor (GCD) of two numbers .

import math

# Find the square root of a number
num = 25
sqrt_result = math.sqrt(num)
print(f"Square root of {num} is:", sqrt_result)

# Calculate the sine of an angle (in radians)
angle_degrees = 30
angle_radians = math.radians(angle_degrees) 
sine_result = math.sin(angle_radians)
print(f"Sine of {angle_degrees} degrees is:", sine_result)

# Find the greatest common divisor (GCD) of two numbers
a, b = 48, 18
gcd_result = math.gcd(a, b)
print(f"GCD of {a} and {b} is:", gcd_result)
