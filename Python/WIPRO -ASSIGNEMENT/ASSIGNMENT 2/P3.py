# Do the following in sequence and record the results in a single program
# Create a set of 5 unique colors. Print the set.
# Add a new color to the set, then try removing an existing color. Print the updated set.
# Create another set with 3 different colors. Find the intersection, union, and difference
# between both sets.
# Check if a specific color is in the set and print the result.
# Convert a list of fruits (with some duplicates) into a set and print the unique fruits.



colors = {"Red", "Blue", "Green", "Yellow", "Purple"}
print("Set of colors:", colors)


colors.add("Orange")
colors.remove("Blue")
print("Updated set of colors:", colors)


more_colors = {"Green", "Black", "White"}


print("Intersection:", colors.intersection(more_colors))
print("Union:", colors.union(more_colors))
print("Difference (colors - more_colors):", colors.difference(more_colors))


print("Is 'Red' in colors?", "Red" in colors)
print("Is 'Blue' in colors?", "Blue" in colors)


fruits_list = ["Apple", "Banana", "Apple", "Orange", "Banana", "Mango"]
unique_fruits = set(fruits_list)
print("Unique fruits:", unique_fruits)
