# Do the following in sequence and record the results in a single program
# Create a list with 5 different types of fruits. Print the list.
# Add two more fruits to the list, then remove one fruit from it. Print the updated list.
# Access the second and fourth fruits in the list. Print them.
# Slice the list to get the first three fruits and print the result.
# Find and print the length of your list.



fruits = ["Apple", "Banana", "Cherry", "Mango", "Kiwi"]
print("List of fruits:", fruits)

fruits.append("Litchi")
fruits.append("Grape")
fruits.remove("Cherry")
print("Updated list of fruits:", fruits)

second_fruit = fruits[1]
fourth_fruit = fruits[3]
print("Second fruit:", second_fruit)
print("Fourth fruit:", fourth_fruit)

first_three_fruits = fruits[:3]
print("First three fruits:", first_three_fruits)

length_of_fruits = len(fruits)
print("Length of the fruits list:", length_of_fruits)
