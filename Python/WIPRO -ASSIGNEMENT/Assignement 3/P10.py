# Use the OS Module:
# Write a program that imports the os module and uses it to:
# Print the current working directory
# Create a new directory and verify its existence.
# List all files and directories in the current directory

import os

# Print the current working directory
cwd = os.getcwd()
print("Current working directory:", cwd)

# Create a new directory and verify its existence
new_dir = "test_directory"
os.makedirs(new_dir, exist_ok=True)   # creates directory if it doesn't exist
print(f"Directory '{new_dir}' created.")

# Verify existence
print("Does the directory exist?", os.path.exists(new_dir))

# List all files and directories in the current directory
items = os.listdir(cwd)
print("Files and directories in current directory:")
for item in items:
    print("-", item)
