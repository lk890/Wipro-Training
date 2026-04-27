#  Write a program that takes a number as input and checks if it is divisible by 5.
# Print a message if it is divisible or not.


number = int(input("Please enter a number: "))
if number % 5 == 0:
    print(f"{number} is divisible by 5.")
else:
    print(f"{number} is not divisible by 5.")