# Write a program that asks the user for their age and checks if they are eligible to
# vote (18 years and older). Print a message based on their eligibility.



age = int(input("Please enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
    