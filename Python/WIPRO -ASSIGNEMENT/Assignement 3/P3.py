# Write a user-defined function "find_largest(a, b, c)" that takes three numbers as
# arguments and returns the largest of the three. Use the function in a program to find and
# print the largest of three given numbers


def find_largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


x, y, z = 12, 45, 23
largest = find_largest(x, y, z)
print(f"The largest of {x}, {y}, and {z} is:", largest)
