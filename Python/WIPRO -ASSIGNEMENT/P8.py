# Write a program that takes a number as input and uses a for loop to calculate its
# factorial. Print the result.

number = int(input("Please enter a number: "))
factorial = 1
for i in range(1, number + 1):
    factorial *= i
print(f"The factorial of {number} is {factorial}.") 