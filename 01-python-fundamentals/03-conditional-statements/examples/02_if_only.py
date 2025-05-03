# ============================================================================
# FILENAME: 02_if_only.py
# DESCRIPTION: Demonstrates using if statements without else clauses
# ============================================================================

# ----------------------------------------------------------------------------
# 1. Basic "if" Without "else"
# ----------------------------------------------------------------------------

print("BASIC 'IF' WITHOUT 'ELSE':")
print("-" * 50)

# Sometimes you only need to execute code when a condition is True,
# and don't need to do anything when it's False.

age = 25

# Example 1: Simple if statement without else
if age >= 18:
    print("You are eligible to vote.")
    print("Make sure you're registered!")

# Nothing happens if the condition is False
if age >= 65:
    print("You are eligible for senior benefits.")

# Example 2: Series of independent if statements
temperature = 32
humidity = 80
is_raining = True

print(f"\nWeather conditions: {temperature}°C, {humidity}% humidity, raining: {is_raining}")

if temperature > 30:
    print("It's very hot today!")

if humidity > 70:
    print("It's very humid today!")
    
if is_raining:
    print("Don't forget your umbrella!")

print("\n" + "-" * 50 + "\n")

# ----------------------------------------------------------------------------
# 2. Guard Clauses
# ----------------------------------------------------------------------------

print("GUARD CLAUSES:")
print("-" * 50)

# A guard clause is an if statement at the beginning of a function 
# that checks for conditions where the function should return early.
# This avoids deeply nested if-else structures.

def process_payment(amount, account_balance, is_account_active):
    # Guard clauses to check for invalid conditions
    if not is_account_active:
        print("Error: Account is inactive. Cannot process payment.")
        return False
        
    if amount <= 0:
        print("Error: Payment amount must be positive.")
        return False
        
    if amount > account_balance:
        print("Error: Insufficient funds.")
        return False
    
    # If we reach here, all conditions are met
    print(f"Processing payment of ${amount:.2f}...")
    print(f"Payment successful. Remaining balance: ${account_balance - amount:.2f}")
    return True

# Test the function with different conditions
print("\nTest 1 - Active account with sufficient funds:")
process_payment(50, 100, True)

print("\nTest 2 - Inactive account:")
process_payment(50, 100, False)

print("\nTest 3 - Invalid amount:")
process_payment(-10, 100, True)

print("\nTest 4 - Insufficient funds:")
process_payment(150, 100, True)

print("\n" + "-" * 50 + "\n")

# ----------------------------------------------------------------------------
# 3. Multiple Conditions with Multiple Statements
# ----------------------------------------------------------------------------

print("MULTIPLE CONDITIONS WITH MULTIPLE STATEMENTS:")
print("-" * 50)

# You can execute multiple statements for each condition
file_size = 1500  # Size in MB
file_type = "video"
download_speed = 10  # MB/s

if file_size > 1000:
    print("This is a large file.")
    estimated_time = file_size / download_speed
    print(f"Estimated download time: {estimated_time:.1f} seconds")
    print(f"                         ({estimated_time / 60:.1f} minutes)")

if file_type == "video":
    print("This is a video file.")
    print("Recommended video players: VLC, Windows Media Player, QuickTime")
    print("You can stream this file instead of downloading it.")

print("\n" + "-" * 50 + "\n")

# ----------------------------------------------------------------------------
# 4. Conditional Initialization
# ----------------------------------------------------------------------------

print("CONDITIONAL INITIALIZATION:")
print("-" * 50)

# You can use if statements to conditionally initialize variables
is_weekend = True
is_holiday = False
is_morning = True

# Set greeting based on conditions
greeting = "Good morning! " if is_morning else "Hello! "

# Initialize work status
if is_weekend or is_holiday:
    work_status = "Enjoy your day off!"
    available_hours = "All day"
else:
    work_status = "It's a work day."
    available_hours = "After 5 PM"

# Print the results
print(f"{greeting}{work_status}")
print(f"You are available: {available_hours}")

# Alternative: Default value with conditional override
default_message = "Welcome to the system!"
login_count = 5

message = default_message
if login_count == 1:
    message = "Welcome to the system for the first time!"
if login_count > 10:
    message = "Welcome back, frequent user!"

print(f"\nLogin message: {message}")

print("\n" + "-" * 50 + "\n")

# ----------------------------------------------------------------------------
# 5. Accumulating Results with if Statements
# ----------------------------------------------------------------------------

print("ACCUMULATING RESULTS WITH IF STATEMENTS:")
print("-" * 50)

# You can use if statements to build up a result incrementally
symptoms = ["fever", "cough", "fatigue", "loss_of_taste"]

diagnosis = "Based on your symptoms:\n"

if "fever" in symptoms:
    diagnosis += "- You have a fever, which could indicate an infection.\n"
    
if "cough" in symptoms:
    diagnosis += "- Your cough could be from a respiratory condition.\n"
    
if "fatigue" in symptoms:
    diagnosis += "- Fatigue is common with many illnesses and conditions.\n"
    
if "loss_of_taste" in symptoms:
    diagnosis += "- Loss of taste has been associated with COVID-19.\n"
    
if "headache" in symptoms:
    diagnosis += "- Headaches can be caused by stress or illness.\n"

# Add a recommendation regardless of specific symptoms
diagnosis += "\nRecommendation: Please consult with a doctor for proper evaluation."

print(diagnosis)

# Another example: Building a shopping cart
cart_items = ["apple", "banana", "milk", "bread", "cheese"]
cart_total = 0

# Add up prices (simplified)
prices = {"apple": 0.5, "banana": 0.3, "milk": 2.0, "bread": 1.5, "cheese": 3.0}

receipt = "Receipt:\n"
for item in cart_items:
    if item in prices:
        price = prices[item]
        cart_total += price
        receipt += f"- {item.capitalize()}: ${price:.2f}\n"

receipt += f"\nTotal: ${cart_total:.2f}"

# Apply discounts
if cart_total > 10:
    discount = cart_total * 0.1
    cart_total -= discount
    receipt += f"\nDiscount (10%): -${discount:.2f}"
    receipt += f"\nFinal Total: ${cart_total:.2f}"

if "milk" in cart_items and "bread" in cart_items:
    receipt += "\nSpecial offer: You qualify for a free butter on your next purchase!"

print("\n" + receipt)

print("\n" + "-" * 50 + "\n")

# ----------------------------------------------------------------------------
# 6. Implicit return with if
# ----------------------------------------------------------------------------

print("IMPLICIT RETURN WITH IF:")
print("-" * 50)

# In Python functions, if a return statement is inside an if block,
# and the condition is False, the function continues executing.

def get_passing_grade(score):
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"  # Implicit else - executed if all conditions are False

# Test the function
test_scores = [95, 82, 71, 65, 50]
for score in test_scores:
    grade = get_passing_grade(score)
    print(f"Score: {score} → Grade: {grade}")

print("\n" + "-" * 50 + "\n")

# ----------------------------------------------------------------------------
# 7. Real-World Example: Data Validation
# ----------------------------------------------------------------------------

print("REAL-WORLD EXAMPLE: DATA VALIDATION:")
print("-" * 50)

# Let's validate some user data without using else statements

def validate_username(username):
    errors = []
    
    if not username:
        errors.append("Username cannot be empty")
    
    if len(username) < 5:
        errors.append("Username must be at least 5 characters long")
    
    if len(username) > 20:
        errors.append("Username cannot be more than 20 characters long")
    
    if not username.isalnum():
        errors.append("Username can only contain letters and numbers")
    
    return errors

# Test with different usernames
test_usernames = ["", "abc", "user123", "valid_username", "extremely_long_username_12345", "user@name"]

for username in test_usernames:
    validation_results = validate_username(username)
    
    if validation_results:  # If there are any errors
        print(f"Username '{username}' is invalid:")
        for error in validation_results:
            print(f"  - {error}")
    
    if not validation_results:  # If there are no errors
        print(f"Username '{username}' is valid!")
    
    print()

print("-" * 50 + "\n")

# ----------------------------------------------------------------------------
# SUMMARY:
# - If statements without else are useful when you only need to execute code
#   for true conditions
# - Guard clauses use early returns to simplify code structure
# - If statements can be used to conditionally initialize variables
# - Multiple independent if statements can be used to check separate conditions
# - If statements can help accumulate results incrementally
# - If statements with return values in functions provide implicit control flow
# - Using if without else can lead to cleaner validation code in some cases
# ============================================================================ 