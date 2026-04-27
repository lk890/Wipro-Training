# Do the following in sequence and record the results in a single program
# Create a dictionary with your name, age, and favorite hobby as keys, and provide
# appropriate values. Print the dictionary.
# Access and print the value associated with your name in the dictionary.
# Add a new key-value pair for your favorite food, then update the value for your favorite
# hobby. Print the updated dictionary.
# Print all the keys and all the values in the dictionary separately.
# Remove the age key-value pair from the dictionary. Print the dictionary to see the
# change

# Step 1: Create a dictionary with name, age, and favorite hobby
person = {
    "name": "Love Khanna",
    "age": 22,
    "hobby": "BrainStorming"
}
print("Initial dictionary:", person)

# Step 2: Access and print the value associated with the name
print("Name value:", person["name"])

# Step 3: Add a new key-value pair for favorite food, then update hobby
person["food"] = "Pizza"
person["hobby"] = "Astrology"
print("Updated dictionary:", person)

# Step 4: Print all keys and all values separately
print("Keys:", list(person.keys()))
print("Values:", list(person.values()))

# Step 5: Remove the age key-value pair
person.pop("age")
print("Dictionary after removing age:", person)

