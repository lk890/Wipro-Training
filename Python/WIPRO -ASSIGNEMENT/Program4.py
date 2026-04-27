# Write a program that takes a character as input and checks if it is a vowel or
# consonant. Print the result.

char = input("Please enter a character: ").lower()
if char in 'aeiou':
    print(f"{char} is a vowel.")
elif char.isalpha():
    print(f"{char} is a consonant.")
else:
    print("Please enter a valid alphabet character.")