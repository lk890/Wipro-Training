# Write a program that takes a traffic light color (Red, Yellow, Green) as input and
# uses match-case to print the corresponding action (e.g., "Stop" for Red, "Wait"
# for Yellow, etc.).

light_color = input("Please enter a traffic light color: ").capitalize()
match light_color:
    case 'Red':
        print("Stop")
    case 'Yellow':  
        print("Wait")
    case 'Green':
        print("Go")
    case _:
        print("Invalid traffic light color. Please enter Red, Yellow, or Green.")
