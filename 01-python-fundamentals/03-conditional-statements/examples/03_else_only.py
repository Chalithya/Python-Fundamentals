# ============================================================================
# FILENAME: 03_else_only.py
# DESCRIPTION: Demonstrates effective usage of else clauses in Python
# ============================================================================

# Note: In Python, 'else' can't exist on its own - it must follow a control 
# statement like 'if', 'for', 'while', or 'try'. This file demonstrates 
# different ways 'else' is used for default actions.

# ----------------------------------------------------------------------------
# 1. Else as a Default Case in if-else
# ----------------------------------------------------------------------------

print("ELSE AS A DEFAULT CASE:")
print("-" * 50)

# The else clause provides a default action when all conditions are False
age = 25

if age < 18:
    print("You are a minor.")
else:  # Default case - executes when the 'if' condition is False
    print("You are an adult.")

# Example with multiple conditions
score = 68

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:  # Default case - catches all remaining possibilities
    grade = "Needs improvement"

print(f"Score: {score}, Grade: {grade}")

print("\n" + "-" * 50 + "\n")

# ----------------------------------------------------------------------------
# 2. Else as a Error Handler
# ----------------------------------------------------------------------------

print("ELSE AS AN ERROR HANDLER:")
print("-" * 50)

# Else can be used to handle errors or exceptional cases
user_input = "42"  # Simulate user input

# Try to convert to an integer, handle error with else
try:
    number = int(user_input)
    print(f"Successfully converted '{user_input}' to integer: {number}")
except ValueError:
    print(f"Error: '{user_input}' is not a valid integer.")

# Better approach is often to use try/except/else
user_input = "42"  # Simulate user input

# Try to convert to an integer, with separate error and success paths
try:
    number = int(user_input)
except ValueError:
    print(f"Error: '{user_input}' is not a valid integer.")
else:  # Executes if no exception occurred
    print(f"Successfully converted '{user_input}' to integer: {number}")
    print(f"Double the value is: {number * 2}")

print("\n" + "-" * 50 + "\n")

# ----------------------------------------------------------------------------
# 3. Else in Loops
# ----------------------------------------------------------------------------

print("ELSE IN LOOPS:")
print("-" * 50)

# The else clause in loops executes after the loop completes normally
# (i.e., not terminated by a break statement)

# Example with a for loop
print("For loop with else:")
for i in range(5):
    print(f"Loop iteration {i}")
else:
    print("Loop completed normally")

print()

# Example where else won't execute due to break
print("For loop with break:")
for i in range(5):
    print(f"Loop iteration {i}")
    if i == 2:
        print("Breaking out of loop")
        break
else:  # This won't execute because the loop was terminated by break
    print("This won't print because the loop didn't complete normally")

print()

# Example with a while loop
print("While loop with else:")
count = 0
while count < 3:
    print(f"Count is {count}")
    count += 1
else:
    print("While loop completed normally")

print()

# Practical example: searching in a collection
search_term = "banana"
fruits = ["apple", "orange", "mango", "grape"]

for fruit in fruits:
    if fruit == search_term:
        print(f"Found {search_term}!")
        break
else:
    print(f"{search_term} not found in the fruit list")

print("\n" + "-" * 50 + "\n")

# ----------------------------------------------------------------------------
# 4. Else in Function Returns
# ----------------------------------------------------------------------------

print("ELSE IN FUNCTION RETURNS:")
print("-" * 50)

# Using else to provide default return values

def find_user(username, user_list):
    for user in user_list:
        if user["name"] == username:
            return user  # Return the user if found
    else:  # Executes if the loop completes without finding a match
        return {"name": "Guest", "role": "Anonymous"}  # Default user

# Test the function
users = [
    {"name": "Alice", "role": "Admin"},
    {"name": "Bob", "role": "User"},
    {"name": "Charlie", "role": "Moderator"}
]

result1 = find_user("Alice", users)
result2 = find_user("Unknown", users)

print(f"Result 1: {result1}")
print(f"Result 2: {result2}")

# Alternative using an if-else approach
def get_user_role(username, user_list):
    for user in user_list:
        if user["name"] == username:
            return user["role"]
    # No else needed here - this is an implicit else
    return "Unknown role"

print(f"Alice's role: {get_user_role('Alice', users)}")
print(f"Unknown user role: {get_user_role('Unknown', users)}")

print("\n" + "-" * 50 + "\n")

# ----------------------------------------------------------------------------
# 5. Else in Data Validation
# ----------------------------------------------------------------------------

print("ELSE IN DATA VALIDATION:")
print("-" * 50)

# Using else to provide feedback on validation

def validate_password(password):
    if len(password) < 8:
        return "Password must be at least 8 characters long"
    elif not any(c.isupper() for c in password):
        return "Password must contain at least one uppercase letter"
    elif not any(c.isdigit() for c in password):
        return "Password must contain at least one digit"
    else:  # All validations passed
        return "Password is valid"

# Test with different passwords
test_passwords = ["short", "nouppercase1", "NODIGITS", "Valid123"]

for password in test_passwords:
    result = validate_password(password)
    print(f"Password: '{password}' → {result}")

print("\n" + "-" * 50 + "\n")

# ----------------------------------------------------------------------------
# 6. Real-World Example: Input Validation Loop
# ----------------------------------------------------------------------------

print("REAL-WORLD EXAMPLE: INPUT VALIDATION LOOP:")
print("-" * 50)

# Using else with loops for validation

def get_valid_number():
    # For this example, we'll simulate user inputs
    simulated_inputs = ["abc", "-5", "0", "10"]
    
    for user_input in simulated_inputs:
        print(f"User entered: {user_input}")
        
        try:
            number = int(user_input)
            if number <= 0:
                print("Error: Please enter a positive number.")
                continue
        except ValueError:
            print("Error: Please enter a valid integer.")
            continue
        
        # If we reach here, the input is valid
        print(f"Valid input received: {number}")
        return number
    
    # If all inputs are exhausted without a valid one
    else:
        print("Error: Maximum attempts reached. Using default value.")
        return 1  # Default value

result = get_valid_number()
print(f"Final result: {result}")

print("\n" + "-" * 50 + "\n")

# ----------------------------------------------------------------------------
# 7. Nested if-else vs. elif
# ----------------------------------------------------------------------------

print("NESTED IF-ELSE VS ELIF:")
print("-" * 50)

# Compare nested if-else statements with elif

# Example 1: Nested if-else (harder to read)
temp = 75

print("Using nested if-else:")
if temp >= 90:
    print("It's hot!")
else:
    if temp >= 70:
        print("It's warm.")
    else:
        if temp >= 50:
            print("It's cool.")
        else:
            print("It's cold!")

# Example 2: Using elif (cleaner and easier to read)
print("\nUsing elif:")
if temp >= 90:
    print("It's hot!")
elif temp >= 70:
    print("It's warm.")
elif temp >= 50:
    print("It's cool.")
else:
    print("It's cold!")

print("\n" + "-" * 50 + "\n")

# ----------------------------------------------------------------------------
# SUMMARY:
# - The 'else' clause provides a default action when other conditions are False
# - In try-except, 'else' executes when no exception occurs
# - In loops, 'else' executes when the loop completes without a 'break'
# - 'else' is useful for providing default values or handling cases that
#   don't match any specific condition
# - Using 'elif' instead of nested if-else structures makes code cleaner
# ============================================================================ 