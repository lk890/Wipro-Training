# Do the following in sequence and record the results in a single program
# Create a tuple with the names of 3 different cities you’d like to visit. Print the tuple.:
# Access and print the first and last elements of the tuple.:
# Create another tuple with 2 more cities. Concatenate both tuples and print the result.
# Try changing one element of the tuple. What happens?
# Unpack the elements of the tuple into separate variables and print them


cities = ("Tokyo", "Las Vegas", "Miami")
print("Tuple of cities:", cities)


print("First city:", cities[0])
print("Last city:", cities[-1])


more_cities = ("Sydney", "Rome")
all_cities = cities + more_cities
print("Concatenated tuple:", all_cities)


try:
    cities[1] = "London" 
except TypeError as e:
    print("Error when trying to modify tuple:", e)


city1, city2, city3 = cities
print("Unpacked cities:")
print("City 1:", city1)
print("City 2:", city2)
print("City 3:", city3)
