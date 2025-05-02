# ============================================================================
# FILENAME: 04_user_input.py
# DESCRIPTION: Demonstrating how to get and process user input in Python
# ============================================================================

# ----------------------------------------------------------------------------
# 1. Basic Input - Getting Strings from Users
# ----------------------------------------------------------------------------

# The input() function reads a line of text from the user
name = input("What is your name? ")  # Displays prompt and waits for user input
print(f"Hello, {name}!")  # Output depends on what the user entered

# Notice that input() always returns a string, even if the user types numbers
# Let's see this in action
user_entry = input("Type something (anything): ")
print(f"You entered: {user_entry}")
print(f"Type of your entry: {type(user_entry)}")  # Always shows <class 'str'>

# ----------------------------------------------------------------------------
# 2. Getting Numeric Input - Converting Strings to Numbers
# ----------------------------------------------------------------------------

# To get a number, we need to convert the string returned by input()
age_str = input("How old are you? ")

age = int(age_str)  # Convert string to integer
print(f"Next year, you'll be {age + 1} years old")

# We can combine the input and conversion in one line
height = float(input("Enter your height in meters: "))
print(f"Your height in centimeters is {height * 100} cm")

# ----------------------------------------------------------------------------
# 3. Error Handling When Getting Numeric Input
# ----------------------------------------------------------------------------

# If the user enters non-numeric data when we expect a number, it will cause an error
# Let's add basic error handling

try:
    weight = float(input("Enter your weight in kg: "))
    print(f"Your weight in pounds is approximately {weight * 2.20462} lbs")
except ValueError:
    print("Error: Please enter a valid number for weight")

# ----------------------------------------------------------------------------
# 4. Getting Multiple Inputs
# ----------------------------------------------------------------------------

# Method 1: Multiple input() calls
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print(f"Your full name is {first_name} {last_name}")

# Method 2: Splitting a single input
# This asks for multiple values on one line, separated by spaces
coordinates = input("Enter x and y coordinates separated by a space: ")
x, y = coordinates.split()  # Split the input string at whitespace
x, y = float(x), float(y)   # Convert both strings to floats
print(f"You entered the point ({x}, {y})")
print(f"Distance from origin: {(x**2 + y**2)**0.5}")

# ----------------------------------------------------------------------------
# 5. Input Validation - Making Sure We Get Valid Data
# ----------------------------------------------------------------------------

# Example: Validating a yes/no response
while True:
    response = input("Do you want to continue? (yes/no): ").strip().lower()
    if response in ["yes", "y"]:
        print("Continuing...")
        break
    elif response in ["no", "n"]:
        print("Stopping.")
        break
    else:
        print("Invalid response. Please enter 'yes' or 'no'.")

# Example: Ensuring a number is within range
while True:
    try:
        rating = int(input("Rate your experience (1-5): "))
        if 1 <= rating <= 5:
            print(f"You rated your experience as {rating}/5. Thank you!")
            break
        else:
            print("Error: Please enter a number between 1 and 5.")
    except ValueError:
        print("Error: Please enter a valid number.")

# ----------------------------------------------------------------------------
# 6. Password Input (Hiding User Input)
# ----------------------------------------------------------------------------

# Note: This requires the getpass module and may not work in all environments
# such as some IDEs. It works best in terminal/command prompt.

# Uncommenting the following will demonstrate hidden password input
# import getpass
# password = getpass.getpass("Enter your password: ")
# print(f"Password received. Length: {len(password)} characters")

# ----------------------------------------------------------------------------
# SUMMARY:
# - input() function gets text input from users
# - input() always returns a string, regardless of what was typed
# - To get numeric data, convert the input with int() or float()
# - Always handle potential errors when converting types
# - For multiple values, either use multiple input() calls or split one input
# - Input validation ensures the data meets requirements before processing
# - For sensitive data like passwords, use getpass.getpass() for hidden input
# ============================================================================ 