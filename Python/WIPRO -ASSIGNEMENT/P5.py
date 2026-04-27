# Write a program that takes a password as input and checks if it is strong (at least
# 8 characters). Print a message based on the result

password = input("Please enter a password: ")
if len(password) >= 8:
    print("Your password is strong.")
else:
    print("Your password is weak. It should be at least 8 characters long.")