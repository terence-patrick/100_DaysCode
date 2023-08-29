print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

# The indentation under the 'if' and 'else' statement is important.
# if height >= 120:
#     print("You can ride the rollercoaster.")
# else:
#     print("Sorry, you have to be taller to go on the ride.")

# Nested if/else statements and elif

if height >= 120:
    print("You can ride the rollercoaster.")
    age = int(input("What is your age? "))
    if age < 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry, you have to be taller to go on the ride.")
