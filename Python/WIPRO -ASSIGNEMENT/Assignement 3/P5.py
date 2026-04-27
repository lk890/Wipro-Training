# Combining Built-in and User-Defined Functions:
# Find the Average of a List:
# Write a user-defined function average(numbers) that takes a list of numbers as an
# argument and returns the average of the numbers. Call the function with a list of
# numbers and print the average.


def average(numbers):
    if len(numbers) == 0:
        return "List is empty, cannot compute average"
    return sum(numbers) / len(numbers)   # Using built-in sum() and len()


nums = [10, 20, 30, 40, 50]
print("Numbers:", nums)
print("Average:", average(nums))
