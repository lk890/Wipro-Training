# Create a Package for String Utilities:
# Create a package called string_utils with two modules: string_operations.py and
# string_validations.py.
# In string_operations.py, define functions for reversing a string, converting a string to
# uppercase, and finding the length of a string.
# In string_validations.py, define functions to check if a string is a palindrome and if it
# contains only alphabetic characters.
# Write a program that imports and uses these functions from the string_utils package

# string_utils/
#     __init__.py
#     string_operations.py
#     string_validations.py
# main.py




# main.py
from string_utils.string_operations import reverse_string, to_uppercase, string_length
from string_utils.string_validation import is_palindrome, is_alpha

# String operations
text = "Love Khanna"
print("Original string:", text)
print("Reversed string:", reverse_string(text))
print("Uppercase string:", to_uppercase(text))
print("Length of string:", string_length(text))

# String validations
print("Is palindrome?", is_palindrome(text))
print("Contains only alphabetic characters?", is_alpha(text))
