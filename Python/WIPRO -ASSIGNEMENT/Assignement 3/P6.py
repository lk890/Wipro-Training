# Check Palindrome:
# Write a user-defined function is_palindrome(s) that takes a string as an argument and
# returns True if the string is a palindrome (reads the same forward and backward), and
# False otherwise. Test the function with different strings and print the results.


def is_palindrome(s):
    # remove spaces and convert to lowercase
    s = s.replace(" ", "").lower()
    return s == s[::-1]  


test_strings = ["madam", "racecar", "hello", "level", "Love Khanna"]

for word in test_strings:
    result = is_palindrome(word)
    print(f"Is '{word}' a palindrome? {result}")
