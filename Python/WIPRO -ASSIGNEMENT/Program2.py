# Write a program that takes a year as input and checks if it is a leap year or not.
# Print the result.

year = int(input("Please enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")