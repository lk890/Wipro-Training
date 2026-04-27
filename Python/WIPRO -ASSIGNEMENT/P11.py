# Write a program that uses a for loop to count the number of vowels in a given
# string. Print the count.

string = input("Please enter a string: ")
vowel_count = 0
for char in string.lower():
    if char in 'aeiou':
        vowel_count += 1
print(f"The number of vowels in the string is: {vowel_count}.")