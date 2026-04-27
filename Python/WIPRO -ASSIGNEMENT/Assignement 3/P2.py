# Write a user-defined function factorial(n) that takes a positive integer n as an argument
# and returns its factorial. Use the function in a program and print the factorial of a given
# number.


def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

# Step 2: Use the function in a program
number = 13  
print(f"Factorial of {number} is:", factorial(number))
