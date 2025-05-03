# ============================================================================
# FILENAME: 07_logical_expressions_in_conditionals.py
# DESCRIPTION: Demonstrates how to use logical expressions in conditional statements
# ============================================================================

"""
This module demonstrates how to use logical operators (and, or, not) in conditional
statements to create complex conditions. Logical expressions allow us to combine
multiple conditions, creating more sophisticated logic in a clean, readable way.
"""

# ----------------------------------------------------------------------------
# 1. The Basic Logical Operators: and, or, not
# ----------------------------------------------------------------------------

# AND operator - True only if both conditions are True
age = 25
income = 50000

if age >= 18 and income >= 30000:
    print("You qualify for a standard credit card.")
else:
    print("You don't qualify for a standard credit card.")
# Output: You qualify for a standard credit card.

# OR operator - True if at least one condition is True
has_good_credit = True
has_high_income = False

if has_good_credit or has_high_income:
    print("You qualify for a loan.")
else:
    print("You don't qualify for a loan.")
# Output: You qualify for a loan.

# NOT operator - Inverts a Boolean value
is_weekend = False

if not is_weekend:
    print("Time to work!")
else:
    print("Time to relax!")
# Output: Time to work!

# ----------------------------------------------------------------------------
# 2. Combining Multiple Logical Operators
# ----------------------------------------------------------------------------

# Example: Movie ticket pricing logic
age = 15
is_student = False
is_senior = False
is_military = False
is_matinee = True

# Standard ticket price
ticket_price = 12.00

# Check for various discounts using multiple logical operators
if (age < 13) or (13 <= age <= 18 and is_student) or (age >= 65 and is_senior) or is_military:
    ticket_price = 8.00
    discount_type = "special discount"
elif is_matinee:
    ticket_price = 10.00
    discount_type = "matinee discount"
else:
    discount_type = "no discount"

print(f"Ticket price: ${ticket_price:.2f} ({discount_type})")
# Output: Ticket price: $10.00 (matinee discount)

# ----------------------------------------------------------------------------
# 3. Short-Circuit Evaluation
# ----------------------------------------------------------------------------

"""
Python uses short-circuit evaluation for logical expressions:
- For 'and': If the first condition is False, the second is not evaluated
- For 'or': If the first condition is True, the second is not evaluated

This can be used to avoid errors and optimize performance.
"""

# Example 1: Avoiding division by zero error
denominator = 0

# Bad approach (would cause ZeroDivisionError)
# if denominator != 0 and 10 / denominator > 2:
#     print("Result is greater than 2")

# Good approach (using short-circuit evaluation)
if denominator != 0 and 10 / denominator > 2:
    print("Result is greater than 2")
else:
    print("Cannot perform the calculation")
# Output: Cannot perform the calculation

# Example 2: Optimization with short-circuit evaluation
def simple_check():
    print("Running simple check...")
    return False

def complex_check():
    print("Running complex check...")
    return True

# The complex_check() function won't run because simple_check() is False
if simple_check() and complex_check():
    print("Both checks passed")
else:
    print("At least one check failed")
# Output:
# Running simple check...
# At least one check failed

# ----------------------------------------------------------------------------
# 4. Using Parentheses for Clarity
# ----------------------------------------------------------------------------

# Example: Determining eligibility for a premium service
age = 30
income = 75000
credit_score = 720
existing_customer = True

# Without parentheses (harder to read)
if age >= 25 and income >= 50000 and credit_score >= 700 or existing_customer and income >= 100000:
    print("Eligible for premium service (without parentheses)")

# With parentheses (much clearer)
if ((age >= 25 and income >= 50000 and credit_score >= 700) or 
    (existing_customer and income >= 100000)):
    print("Eligible for premium service (with parentheses)")
# Output: Eligible for premium service (with parentheses)

# ----------------------------------------------------------------------------
# 5. Truth Value Testing
# ----------------------------------------------------------------------------

"""
Python considers the following values as False in a logical context:
- False
- None
- Zero of any numeric type (0, 0.0, 0j)
- Empty sequences ('', [], ())
- Empty mappings ({})
- Objects that implement __bool__() that returns False
- Objects that implement __len__() that returns 0

Everything else is considered True.
"""

# Example: Using truth value testing for cleaner code
items = []
name = ""
amount = 0
settings = {}

# Checking if values are "empty" or "falsy"
if not items:
    print("The items list is empty")

if not name:
    print("No name provided")

if not amount:
    print("Amount is zero")

if not settings:
    print("No settings configured")

# Using truth value testing as a guard clause
def process_data(data=None):
    """
    Process the given data.
    
    Args:
        data: The data to process (any type)
        
    Returns:
        str: A message indicating the result
    """
    if not data:  # This handles None, empty strings, empty lists, etc.
        return "No data to process"
    
    # Process the data (simplified for example)
    return f"Processed {len(str(data))} units of data"

print(process_data())         # Output: No data to process
print(process_data([]))       # Output: No data to process
print(process_data("Hello"))  # Output: Processed 5 units of data

# ----------------------------------------------------------------------------
# 6. Common Patterns with Logical Expressions
# ----------------------------------------------------------------------------

# Pattern 1: Range checking
temperature = 75

if 70 <= temperature <= 80:
    print("Temperature is comfortable")
# Output: Temperature is comfortable

# Pattern 2: Either/or with mutual exclusion
is_weekday = True
is_holiday = False

if is_weekday and not is_holiday:
    print("It's a working day")
elif not is_weekday:
    print("It's the weekend")
else:
    print("It's a holiday")
# Output: It's a working day

# Pattern 3: Required and optional conditions
has_required_docs = True
has_optional_docs = False

if has_required_docs:
    status = "Complete" if has_optional_docs else "Acceptable"
    print(f"Application status: {status}")
else:
    print("Application status: Incomplete")
# Output: Application status: Acceptable

# ----------------------------------------------------------------------------
# 7. Simplifying Complex Conditions with Helper Functions
# ----------------------------------------------------------------------------

def is_eligible_for_discount(age, is_student, is_senior, is_military):
    """
    Determine if a person is eligible for a discount.
    
    Args:
        age (int): The person's age
        is_student (bool): Whether the person is a student
        is_senior (bool): Whether the person is a senior
        is_military (bool): Whether the person is military personnel
        
    Returns:
        bool: True if eligible for a discount, False otherwise
    """
    return (age < 13 or 
            (13 <= age <= 18 and is_student) or 
            (age >= 65 and is_senior) or 
            is_military)

# Using the helper function makes the main code cleaner
age = 15
is_student = True
is_senior = False
is_military = False
is_matinee = True

if is_eligible_for_discount(age, is_student, is_senior, is_military):
    ticket_price = 8.00
    print(f"Ticket price: ${ticket_price:.2f} (special discount)")
elif is_matinee:
    ticket_price = 10.00
    print(f"Ticket price: ${ticket_price:.2f} (matinee discount)")
else:
    ticket_price = 12.00
    print(f"Ticket price: ${ticket_price:.2f} (no discount)")
# Output: Ticket price: $8.00 (special discount)

# ----------------------------------------------------------------------------
# 8. Real-World Example: Login Authentication
# ----------------------------------------------------------------------------

def authenticate_user(username, password, use_two_factor=False, two_factor_code=None):
    """
    Authenticate a user based on credentials.
    
    Args:
        username (str): The username
        password (str): The password
        use_two_factor (bool): Whether two-factor authentication is enabled
        two_factor_code (str): The two-factor authentication code
        
    Returns:
        tuple: (success, message)
    """
    # Simulate a user database
    users = {
        "admin": {"password": "admin123", "two_factor_enabled": True},
        "user1": {"password": "pass123", "two_factor_enabled": False},
        "guest": {"password": "guest", "two_factor_enabled": False}
    }
    
    # Check if username exists
    if username not in users:
        return (False, "Invalid username")
    
    # Check if password is correct
    if users[username]["password"] != password:
        return (False, "Invalid password")
    
    # Check two-factor authentication if enabled
    if users[username]["two_factor_enabled"]:
        if not use_two_factor:
            return (False, "Two-factor authentication required")
        
        if not two_factor_code or two_factor_code != "123456":  # Simplified for example
            return (False, "Invalid two-factor code")
    
    # If all checks passed, authentication is successful
    return (True, f"Welcome, {username}!")

# Test cases
def login(username, password, use_two_factor=False, two_factor_code=None):
    """
    Attempt to log in with the given credentials.
    
    Args:
        username (str): The username
        password (str): The password
        use_two_factor (bool): Whether to use two-factor authentication
        two_factor_code (str): The two-factor authentication code
    """
    result, message = authenticate_user(username, password, use_two_factor, two_factor_code)
    print(f"Login attempt for '{username}': {message}")
    return result

print("\nLogin Authentication Tests:")
login("nonexistent", "password")             # Invalid username
login("admin", "wrongpassword")              # Invalid password
login("admin", "admin123")                   # Missing two-factor
login("admin", "admin123", True, "wrong")    # Wrong two-factor code
login("admin", "admin123", True, "123456")   # Successful admin login
login("user1", "pass123")                    # Successful regular user login

# ----------------------------------------------------------------------------
# SUMMARY:
# - Logical operators (and, or, not) allow combining multiple conditions
# - Short-circuit evaluation can optimize code and prevent errors
# - Use parentheses for clarity in complex logical expressions
# - Truth value testing simplifies checking for empty or zero values
# - Extract complex conditions into helper functions for readability
# - Understand common patterns like range checking and mutual exclusion
# - Logical expressions are essential for creating sophisticated program logic
# ============================================================================ 