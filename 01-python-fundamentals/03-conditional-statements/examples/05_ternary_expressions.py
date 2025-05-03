# ============================================================================
# FILENAME: 05_ternary_expressions.py
# DESCRIPTION: Demonstrates how to use ternary conditional expressions in Python
# ============================================================================

"""
This module demonstrates the usage of ternary conditional expressions in Python.
Ternary expressions provide a concise way to write simple if-else statements
in a single line, making code more readable for straightforward conditions.

The syntax for a ternary expression in Python is:
    value_if_true if condition else value_if_false
"""

# ----------------------------------------------------------------------------
# 1. Basic Ternary Expression Syntax
# ----------------------------------------------------------------------------

# Traditional if-else statement
x = 10
result = ""

if x > 5:
    result = "x is greater than 5"
else:
    result = "x is less than or equal to 5"

print(f"Traditional if-else result: {result}")  # Output: x is greater than 5

# Same logic using ternary expression
result_ternary = "x is greater than 5" if x > 5 else "x is less than or equal to 5"
print(f"Ternary expression result: {result_ternary}")  # Output: x is greater than 5

# ----------------------------------------------------------------------------
# 2. Using Ternary Expressions with Variables
# ----------------------------------------------------------------------------

def get_ticket_price(age):
    """
    Determines ticket price based on age using a ternary expression.
    
    Args:
        age (int): The age of the person
        
    Returns:
        float: The ticket price
    """
    # Using a ternary expression to determine the ticket price
    ticket_price = 10.0 if age < 18 else 20.0
    return ticket_price

# Example usage
child_age = 12
adult_age = 35

print(f"Ticket price for a {child_age}-year-old: ${get_ticket_price(child_age)}")  # Output: $10.0
print(f"Ticket price for a {adult_age}-year-old: ${get_ticket_price(adult_age)}")  # Output: $20.0

# ----------------------------------------------------------------------------
# 3. Ternary Expressions with Function Calls
# ----------------------------------------------------------------------------

def is_even(number):
    """
    Check if a number is even.
    
    Args:
        number (int): The number to check
        
    Returns:
        bool: True if the number is even, False otherwise
    """
    return number % 2 == 0

# Using ternary expression with function call
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    status = "even" if is_even(num) else "odd"
    print(f"The number {num} is {status}")

# ----------------------------------------------------------------------------
# 4. Nested Ternary Expressions (Use With Caution)
# ----------------------------------------------------------------------------

# Determine a grade based on score
score = 85

# Nested ternary (harder to read - use with caution)
grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "D" if score >= 60 else "F"
print(f"Score of {score} gets a grade of: {grade}")  # Output: B

# The same logic is often clearer with if-elif-else
def get_grade(score):
    """
    Determine a letter grade based on a numeric score.
    
    Args:
        score (int): Numeric score from 0-100
        
    Returns:
        str: Letter grade (A, B, C, D, or F)
    """
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

print(f"Score of {score} gets a grade of: {get_grade(score)}")  # Output: B

# ----------------------------------------------------------------------------
# 5. Ternary Expressions in Return Statements
# ----------------------------------------------------------------------------

def check_temperature(temp):
    """
    Check if the temperature is hot, cold, or moderate.
    
    Args:
        temp (float): Temperature in Celsius
        
    Returns:
        str: Description of the temperature
    """
    return "hot" if temp > 30 else "cold" if temp < 10 else "moderate"

# Test the function
print(f"35°C is {check_temperature(35)}")    # Output: hot
print(f"20°C is {check_temperature(20)}")    # Output: moderate
print(f"5°C is {check_temperature(5)}")      # Output: cold

# ----------------------------------------------------------------------------
# 6. Using Ternary Expressions for Default Values
# ----------------------------------------------------------------------------

def get_full_name(first_name, last_name, middle_name=None):
    """
    Generate a full name with optional middle name.
    
    Args:
        first_name (str): First name
        last_name (str): Last name
        middle_name (str, optional): Middle name
        
    Returns:
        str: Formatted full name
    """
    # Use ternary to include middle name only if it exists
    middle = f" {middle_name} " if middle_name else " "
    return f"{first_name}{middle}{last_name}"

print(get_full_name("John", "Doe", "Smith"))  # Output: John Smith Doe
print(get_full_name("Jane", "Doe"))           # Output: Jane Doe

# ----------------------------------------------------------------------------
# 7. Common Pitfalls and Best Practices
# ----------------------------------------------------------------------------

# Pitfall 1: Overly complex ternary expressions
# Bad practice - hard to read and understand
complex_score = 75
result = ("High Pass" if complex_score >= 90 else "Pass" if complex_score >= 70 else "Conditional Pass" if complex_score >= 60 else "Fail") if complex_score >= 0 and complex_score <= 100 else "Invalid Score"

print(result)  # Output: Pass

# Better approach: Use functions for complex logic
def evaluate_score(score):
    """
    Evaluate a score and return the appropriate result.
    
    Args:
        score (int): The score to evaluate
        
    Returns:
        str: The evaluation result
    """
    if score < 0 or score > 100:
        return "Invalid Score"
    
    if score >= 90:
        return "High Pass"
    elif score >= 70:
        return "Pass"
    elif score >= 60:
        return "Conditional Pass"
    else:
        return "Fail"

print(evaluate_score(75))  # Output: Pass

# ----------------------------------------------------------------------------
# 8. Practical Application
# ----------------------------------------------------------------------------

def pluralize(count, singular, plural=None):
    """
    Return singular or plural form of a word based on count.
    
    Args:
        count (int): The count determining plurality
        singular (str): Singular form of the word
        plural (str, optional): Plural form of the word. 
                               If not provided, adds 's' to singular form.
    
    Returns:
        str: Appropriate form of the word based on count
    """
    if plural is None:
        plural = singular + 's'
    
    return singular if count == 1 else plural

# Example usage in a sentence generation function
def item_count_message(count, item):
    """
    Generate a message about the count of an item.
    
    Args:
        count (int): Number of items
        item (str): The item name (singular form)
        
    Returns:
        str: A formatted message
    """
    return f"You have {count} {pluralize(count, item)}"

print(item_count_message(1, "apple"))   # Output: You have 1 apple
print(item_count_message(5, "apple"))   # Output: You have 5 apples
print(item_count_message(1, "child"))   # Output: You have 1 child
print(item_count_message(3, "child", "children"))  # Output: You have 3 children

# ----------------------------------------------------------------------------
# SUMMARY:
# - Ternary expressions use the syntax: value_if_true if condition else value_if_false
# - They provide a concise way to write simple if-else statements in one line
# - Ternary expressions can make code more readable for simple conditions
# - Avoid overly complex or nested ternary expressions as they reduce readability
# - Use functions instead of complex ternary expressions for better maintenance
# - Ternary expressions are ideal for simple value selection, defaults, or formatting
# - They can be particularly useful in return statements and assignments
# ============================================================================ 