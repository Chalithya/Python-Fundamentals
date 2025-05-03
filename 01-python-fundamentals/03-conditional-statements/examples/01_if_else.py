# ============================================================================
# FILENAME: 01_if_else.py
# DESCRIPTION: Demonstrates the basic if-else statement structure in Python
# ============================================================================

# ----------------------------------------------------------------------------
# 1. Basic if-else Structure
# ----------------------------------------------------------------------------

print("BASIC IF-ELSE STRUCTURE:")
print("-" * 50)

# The if-else statement is used to execute one block of code if a condition
# is True, and another block if it's False

# Example with a simple comparison
temperature = 28

if temperature > 25:
    print(f"The temperature is {temperature}°C. It's hot today!")
else:
    print(f"The temperature is {temperature}°C. It's not hot today.")

# Example with a variable containing a boolean value
is_sunny = True

if is_sunny:
    print("Don't forget your sunglasses!")
else:
    print("You might not need sunglasses today.")

print("\n" + "-" * 50 + "\n")

# ----------------------------------------------------------------------------
# 2. Multiple Conditions with if-elif-else
# ----------------------------------------------------------------------------

print("MULTIPLE CONDITIONS WITH IF-ELIF-ELSE:")
print("-" * 50)

# The if-elif-else structure allows you to check multiple conditions
# in sequence. The first condition that evaluates to True will have
# its block executed, and the rest will be skipped.

score = 85

if score >= 90:
    grade = "A"
    print(f"Score: {score} - Grade: {grade} (Excellent!)")
elif score >= 80:
    grade = "B"
    print(f"Score: {score} - Grade: {grade} (Good!)")
elif score >= 70:
    grade = "C"
    print(f"Score: {score} - Grade: {grade} (Satisfactory)")
elif score >= 60:
    grade = "D"
    print(f"Score: {score} - Grade: {grade} (Needs Improvement)")
else:
    grade = "F"
    print(f"Score: {score} - Grade: {grade} (Failed)")

# Example with a time of day greeting
import datetime

current_hour = datetime.datetime.now().hour
print(f"Current hour: {current_hour}")

if current_hour < 12:
    print("Good morning!")
elif current_hour < 17:
    print("Good afternoon!")
elif current_hour < 21:
    print("Good evening!")
else:
    print("Good night!")

print("\n" + "-" * 50 + "\n")

# ----------------------------------------------------------------------------
# 3. If-else with Complex Conditions
# ----------------------------------------------------------------------------

print("IF-ELSE WITH COMPLEX CONDITIONS:")
print("-" * 50)

# You can combine multiple conditions using logical operators
# - and: True if both conditions are True
# - or: True if at least one condition is True
# - not: Inverts a boolean value

age = 25
has_license = True
is_insured = True

# Using 'and' - all conditions must be True
if age >= 18 and has_license and is_insured:
    print("You can rent a car.")
else:
    print("You cannot rent a car.")

# Using 'or' - at least one condition must be True
is_student = False
is_senior = False

if is_student or is_senior:
    print("You are eligible for a discount.")
else:
    print("No discount available.")

# Using 'not' - inverts the boolean value
is_weekend = False

if not is_weekend:
    print("It's a weekday. Time to work!")
else:
    print("It's the weekend. Time to relax!")

# Combining logical operators with parentheses for clarity
has_cash = False
has_credit_card = True
has_payment_app = True

if has_cash or (has_credit_card and has_payment_app):
    print("You have valid payment methods.")
else:
    print("You don't have valid payment methods.")

print("\n" + "-" * 50 + "\n")

# ----------------------------------------------------------------------------
# 4. Truthiness and Falsiness in Conditions
# ----------------------------------------------------------------------------

print("TRUTHINESS AND FALSINESS IN CONDITIONS:")
print("-" * 50)

# In Python, values can be evaluated as either "truthy" or "falsy" 
# in a boolean context.

# Falsy values include: False, None, 0, 0.0, '', [], {}, set(), ()
# Everything else is considered truthy

# Examples of falsy values
print("Examples of falsy values:")
if False:
    print("This won't print because False is falsy")
else:
    print("False is falsy")

if None:
    print("This won't print because None is falsy")
else:
    print("None is falsy")

if 0:
    print("This won't print because 0 is falsy")
else:
    print("0 is falsy")

if "":
    print("This won't print because an empty string is falsy")
else:
    print("Empty string is falsy")

if []:
    print("This won't print because an empty list is falsy")
else:
    print("Empty list is falsy")

# Examples of truthy values
print("\nExamples of truthy values:")
if True:
    print("True is truthy")

if 42:
    print("Non-zero numbers like 42 are truthy")

if "Hello":
    print("Non-empty strings like 'Hello' are truthy")

if [1, 2, 3]:
    print("Non-empty lists are truthy")

if {"key": "value"}:
    print("Non-empty dictionaries are truthy")

print("\n" + "-" * 50 + "\n")

# ----------------------------------------------------------------------------
# 5. Checking for Object Existence
# ----------------------------------------------------------------------------

print("CHECKING FOR OBJECT EXISTENCE:")
print("-" * 50)

# A common pattern is to check if a variable exists or has a value before using it

# Example 1: Checking if a variable has a value before using it
user_name = "Alice"  # Try changing this to an empty string or None

if user_name:
    print(f"Hello, {user_name}!")
else:
    print("Hello, anonymous user!")

# Example 2: Safe dictionary access
user_data = {"name": "Bob", "age": 30}  # Try removing 'email' key

if "email" in user_data:
    print(f"User email: {user_data['email']}")
else:
    print("No email found for this user")

# Alternative using .get() method
email = user_data.get("email", "No email provided")
print(f"User email (using .get()): {email}")

print("\n" + "-" * 50 + "\n")

# ----------------------------------------------------------------------------
# 6. Real-World Example: Form Validation
# ----------------------------------------------------------------------------

print("REAL-WORLD EXAMPLE: FORM VALIDATION:")
print("-" * 50)

# Let's simulate validating a user registration form

username = "user123"
password = "pass123"
email = "user@example.com"
age = 17

# Validate username
if not username:
    print("Error: Username cannot be empty")
elif len(username) < 5:
    print("Error: Username must be at least 5 characters long")
else:
    print("Username is valid")

# Validate password
if not password:
    print("Error: Password cannot be empty")
elif len(password) < 8:
    print("Error: Password must be at least 8 characters long")
else:
    print("Password is valid")

# Validate email (simplified)
if not email:
    print("Error: Email cannot be empty")
elif "@" not in email or "." not in email:
    print("Error: Email must contain '@' and '.'")
else:
    print("Email is valid")

# Validate age
if not isinstance(age, int):
    print("Error: Age must be a number")
elif age < 18:
    print("Error: You must be at least 18 years old to register")
else:
    print("Age is valid")

# Final validation
if (len(username) >= 5 and len(password) >= 8 and 
        "@" in email and "." in email and 
        isinstance(age, int) and age >= 18):
    print("\nRegistration successful!")
else:
    print("\nRegistration failed. Please fix the errors above.")

print("\n" + "-" * 50 + "\n")

# ----------------------------------------------------------------------------
# 7. Common Mistakes with if-else Statements
# ----------------------------------------------------------------------------

print("COMMON MISTAKES WITH IF-ELSE STATEMENTS:")
print("-" * 50)

# Mistake 1: Using assignment (=) instead of equality (==)
x = 10
if x == 10:  # Correct: equality check
    print("x equals 10")

# The following would be a mistake:
# if x = 10:  # This would cause a syntax error

# Mistake 2: Forgetting the colon
if x == 10:  # Correct: has a colon
    print("Colon included correctly")

# Mistake 3: Incorrect indentation
if True:
    print("This is properly indented")
    print("This is also properly indented")
# print("This would cause an IndentationError if it were indented incorrectly")

# Mistake 4: Redundant elif after a catch-all condition
score = 75

# Incorrect - the second elif will never execute
if score >= 70:
    print("You passed!")
else:
    print("You failed!")
    # The following would never execute:
    # elif score >= 90:
    #     print("You got an A!")

# Mistake 5: Not handling all possible cases
# Here we ensure all cases are covered with a final else
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:  # This catches all remaining cases
    print("Grade: F")

# Mistake 6: Overusing nested conditionals when they can be simplified
user_type = "admin"
is_active = True

# Nested approach (more complex)
if user_type == "admin":
    if is_active:
        print("Active admin")
    else:
        print("Inactive admin")
else:
    if is_active:
        print("Active regular user")
    else:
        print("Inactive regular user")

# Simplified approach with combined conditions
if user_type == "admin" and is_active:
    print("Active admin")
elif user_type == "admin" and not is_active:
    print("Inactive admin")
elif user_type != "admin" and is_active:
    print("Active regular user")
else:
    print("Inactive regular user")

print("\n" + "-" * 50 + "\n")

# ----------------------------------------------------------------------------
# SUMMARY:
# - The if-else statement allows code to make decisions based on conditions
# - if-elif-else allows checking multiple conditions in sequence
# - Conditions can be combined using logical operators (and, or, not)
# - Python values are evaluated as "truthy" or "falsy" in conditional contexts
# - Common patterns include checking for existence and validating inputs
# - Common mistakes include confusion between = and ==, indentation errors,
#   and not handling all possible cases
# ============================================================================ 