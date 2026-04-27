# Use the Datetime Module:
# Write a program that imports the datetime module and uses it to:
# Get and print the current date and time .
# Calculate and print the number of days between two dates.
# Format and print the current date in the format "DD-MM-YYYY"a/aa

import datetime

# Get and print the current date and time
current_dt = datetime.datetime.now()
print("Current date and time:", current_dt)

# Calculate and print the number of days between two dates
date1 = datetime.date(2026, 4, 1)   # April 1, 2026
date2 = datetime.date(2026, 4, 26)  # April 26, 2026
days_between = (date2 - date1).days
print(f"Number of days between {date1} and {date2}:", days_between)

# Format and print the current date in "DD-MM-YYYY"
formatted_date = current_dt.strftime("%d-%m-%Y")
print("Formatted current date:", formatted_date)
