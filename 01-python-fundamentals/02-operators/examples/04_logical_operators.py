# ============================================================================
# FILENAME: 04_logical_operators.py
# DESCRIPTION: Demonstrating Python's logical operators with examples
# ============================================================================

# ----------------------------------------------------------------------------
# 1. The Three Logical Operators: and, or, not
# ----------------------------------------------------------------------------

# Python has three logical operators:
# - and: Returns True if both operands are True
# - or: Returns True if at least one operand is True
# - not: Returns the opposite boolean value of the operand

# Basic logical AND operation
x = True
y = False

print("Basic Logical Operations:")
print(f"True and True = {True and True}")      # True
print(f"True and False = {True and False}")    # False
print(f"False and True = {False and True}")    # False
print(f"False and False = {False and False}")  # False

# Basic logical OR operation
print(f"True or True = {True or True}")      # True
print(f"True or False = {True or False}")    # True
print(f"False or True = {False or True}")    # True
print(f"False or False = {False or False}")  # False

# Basic logical NOT operation
print(f"not True = {not True}")    # False
print(f"not False = {not False}")  # True

print("\n" + "-" * 50 + "\n")

# ----------------------------------------------------------------------------
# 2. Truth Table Representations
# ----------------------------------------------------------------------------

print("Truth Tables:")

# AND Truth Table
print("AND Truth Table:")
print("┌─────────┬─────────┬─────────────┐")
print("│    A    │    B    │   A and B   │")
print("├─────────┼─────────┼─────────────┤")
print("│  True   │  True   │    True     │")
print("│  True   │  False  │    False    │")
print("│  False  │  True   │    False    │")
print("│  False  │  False  │    False    │")
print("└─────────┴─────────┴─────────────┘")

# OR Truth Table
print("\nOR Truth Table:")
print("┌─────────┬─────────┬────────────┐")
print("│    A    │    B    │   A or B   │")
print("├─────────┼─────────┼────────────┤")
print("│  True   │  True   │    True    │")
print("│  True   │  False  │    True    │")
print("│  False  │  True   │    True    │")
print("│  False  │  False  │    False   │")
print("└─────────┴─────────┴────────────┘")

# NOT Truth Table
print("\nNOT Truth Table:")
print("┌─────────┬───────────┐")
print("│    A    │   not A   │")
print("├─────────┼───────────┤")
print("│  True   │   False   │")
print("│  False  │   True    │")
print("└─────────┴───────────┘")

print("\n" + "-" * 50 + "\n")

# ----------------------------------------------------------------------------
# 3. Short-Circuit Evaluation
# ----------------------------------------------------------------------------

print("Short-Circuit Evaluation:")

# Python uses short-circuit evaluation: if the result can be determined
# from the first operand alone, the second operand is not evaluated

# Example 1: Short-circuit with 'and'
print("Example with 'and':")
def print_and_return_false():
    print("Function 'print_and_return_false' was called.")
    return False

def print_and_return_true():
    print("Function 'print_and_return_true' was called.")
    return True

# First operand is False, so second operand is not evaluated
result = print_and_return_false() and print_and_return_true()
print(f"Result: {result}")  # False, and only the first function was called

print("\nExample with 'or':")
# First operand is True, so second operand is not evaluated
result = print_and_return_true() or print_and_return_false()
print(f"Result: {result}")  # True, and only the first function was called

# When first operand doesn't determine the result, the second is evaluated
print("\nWhen both operands need to be evaluated:")
result = print_and_return_true() and print_and_return_true()
print(f"Result: {result}")  # True, and both functions were called

print("\n" + "-" * 50 + "\n")

# ----------------------------------------------------------------------------
# 4. Using Logical Operators with Non-Boolean Values
# ----------------------------------------------------------------------------

print("Logical Operators with Non-Boolean Values:")

# In Python, any non-zero number or non-empty container is considered True
# Zero, None, and empty containers are considered False

# Examples of values considered False:
print("Values evaluated as False:")
print(f"bool(0): {bool(0)}")            # False
print(f"bool(0.0): {bool(0.0)}")        # False
print(f"bool(''): {bool('')}")          # False (empty string)
print(f"bool([]): {bool([])}")          # False (empty list)
# print(f"bool({}): {bool({})}")          # False (empty dictionary)
print(f"bool(None): {bool(None)}")      # False
print(f"bool(set()): {bool(set())}")    # False (empty set)
print(f"bool(()): {bool(())}")          # False (empty tuple)

# Examples of values considered True:
print("\nValues evaluated as True:")
print(f"bool(1): {bool(1)}")                    # True
print(f"bool(-1): {bool(-1)}")                  # True
print(f"bool(0.1): {bool(0.1)}")                # True
print(f"bool('hello'): {bool('hello')}")        # True (non-empty string)
print(f"bool([1, 2]): {bool([1, 2])}")          # True (non-empty list)
print(f"bool({{'a': 1}}): {bool({'a': 1})}")    # True (non-empty dictionary)

# When using logical operators with non-boolean values,
# Python returns the last evaluated operand, not a boolean

# Examples with 'and':
print("\nExamples of 'and' with non-boolean values:")
print(f"10 and 20: {10 and 20}")          # 20 (both are true-ish, returns last value)
print(f"10 and 0: {10 and 0}")            # 0 (0 is false-ish, returns 0)
print(f"0 and 10: {0 and 10}")            # 0 (0 is false-ish, short-circuits, returns 0)
print(f"'' and 'hello': {'' and 'hello'}")  # '' (empty string is false-ish, returns '')

# Examples with 'or':
print("\nExamples of 'or' with non-boolean values:")
print(f"10 or 20: {10 or 20}")          # 10 (10 is true-ish, short-circuits, returns 10)
print(f"0 or 10: {0 or 10}")            # 10 (0 is false-ish, returns 10)
print(f"0 or '': {0 or ''}")            # '' (both are false-ish, returns last value)
print(f"'' or 'hello': {'' or 'hello'}")  # 'hello' ('' is false-ish, returns 'hello')

# This behavior is useful for providing default values
print("\nUsing 'or' for default values:")
user_name = ""
display_name = user_name or "Guest"
print(f"Display name: {display_name}")  # "Guest" (since user_name is empty)

user_name = "Alice"
display_name = user_name or "Guest"
print(f"Display name: {display_name}")  # "Alice" (since user_name is non-empty)

print("\n" + "-" * 50 + "\n")

# ----------------------------------------------------------------------------
# 5. Combining Logical Operators and Operator Precedence
# ----------------------------------------------------------------------------

print("Operator Precedence and Combining Logical Operators:")

# Operator precedence (from highest to lowest):
# 1. not
# 2. and
# 3. or

# Examples of operator precedence:
a, b, c = True, False, True

# not has higher precedence than and
result = not a and b  # Equivalent to (not a) and b
print(f"not a and b = {result}")  # False

# and has higher precedence than or
result = a and b or c  # Equivalent to (a and b) or c
print(f"a and b or c = {result}")  # True

# Using parentheses to override precedence
result = a and (b or c)  # Explicit grouping
print(f"a and (b or c) = {result}")  # True

# More complex examples
result = not a or b and c  # Equivalent to (not a) or (b and c)
print(f"not a or b and c = {result}")  # False

result = not (a or b) and c  # Explicit grouping
print(f"not (a or b) and c = {result}")  # False

# Best practice: use parentheses to make complex expressions clearer
result = (not a) and (b or c)
print(f"(not a) and (b or c) = {result}")  # False

print("\n" + "-" * 50 + "\n")

# ----------------------------------------------------------------------------
# 6. Practical Applications of Logical Operators
# ----------------------------------------------------------------------------

print("Practical Applications:")

# 1. Conditional execution (if statements)
age = 25
has_id = True

if age >= 21 and has_id:
    print("You may enter the venue and purchase alcohol.")
elif age >= 18 and has_id:
    print("You may enter the venue but cannot purchase alcohol.")
else:
    print("You cannot enter the venue.")

# 2. Filtering data
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [num for num in numbers if num % 2 == 0]
odds = [num for num in numbers if num % 2 != 0]

print(f"\nOriginal list: {numbers}")
print(f"Even numbers: {evens}")
print(f"Odd numbers: {odds}")

# Combined conditions
even_and_greater_than_5 = [num for num in numbers if num % 2 == 0 and num > 5]
print(f"Even numbers greater than 5: {even_and_greater_than_5}")

# 3. Input validation
def validate_username(username):
    if not username:  # Check if username is empty
        return "Username cannot be empty"
    
    if len(username) < 3 or len(username) > 20:
        return "Username must be between 3 and 20 characters"
    
    if not username.isalnum():  # Check if username contains only alphanumeric characters
        return "Username can only contain letters and numbers"
    
    return "Username is valid"

print("\nUsername Validation:")
print(f"'': {validate_username('')}")
print(f"'ab': {validate_username('ab')}")
print(f"'user123': {validate_username('user123')}")
print(f"'user@123': {validate_username('user@123')}")

# 4. Simplifying complex conditions
is_weekend = True
is_holiday = False
is_morning = False

# Instead of nested if statements
if is_weekend or is_holiday:
    if not is_morning:
        print("\nYou can sleep in!")

# Same logic in one condition
if (is_weekend or is_holiday) and not is_morning:
    print("You can sleep in! (same logic, one line)")

print("\n" + "-" * 50 + "\n")

# ----------------------------------------------------------------------------
# 7. Common Logical Patterns and Idioms
# ----------------------------------------------------------------------------

print("Common Logical Patterns and Idioms:")

# 1. Checking if a value is in a range
x = 25
in_range = 0 <= x <= 100  # Chained comparison, equivalent to 0 <= x and x <= 100
print(f"Is {x} between 0 and 100? {in_range}")

# 2. Safely accessing potentially None values
person = {"name": "Alice", "age": 30}
# person = None  # Uncomment to test None case

# Without logical operators
if person is not None:
    name = person.get("name")
else:
    name = "Unknown"

# With logical operators (more concise)
name = person and person.get("name") or "Unknown"
print(f"Name: {name}")

# 3. Multiple conditions for the same action (using 'or')
color = "purple"

# Verbose way
if color == "red" or color == "blue" or color == "green":
    print(f"{color} is a primary RGB color")
else:
    print(f"{color} is not a primary RGB color")

# More concise way (using the 'in' operator)
if color in ["red", "blue", "green"]:
    print(f"{color} is a primary RGB color (concise check)")
else:
    print(f"{color} is not a primary RGB color (concise check)")

# 4. Boolean flags with logical operators
is_admin = False
is_staff = True
is_active = True

can_edit = is_admin or (is_staff and is_active)
print(f"\nCan edit: {can_edit}")

# 5. Guard clauses (early returns)
def process_data(data):
    # Guard clauses using logical operators
    if not data:
        return "No data provided"
    
    if not isinstance(data, list):
        return "Data must be a list"
    
    return f"Processing {len(data)} items..."

print("\nGuard Clauses Examples:")
print(process_data(None))       # "No data provided"
print(process_data("not_list")) # "Data must be a list"
print(process_data([1, 2, 3]))  # "Processing 3 items..."

print("\n" + "-" * 50 + "\n")

# ----------------------------------------------------------------------------
# 8. Logical Operators vs. Bitwise Operators
# ----------------------------------------------------------------------------

print("Logical Operators vs. Bitwise Operators:")

# Logical operators (and, or, not) work with boolean expressions
# Bitwise operators (&, |, ~) work with individual bits

a, b = True, False

# Logical operators
logical_and = a and b
logical_or = a or b
logical_not = not a

# Bitwise operators (when used with boolean values)
bitwise_and = a & b
bitwise_or = a | b
bitwise_not = ~a  # Note: This doesn't give the expected boolean complement!

print("With boolean values:")
print(f"a and b: {logical_and}, a & b: {bitwise_and}")  # Same result
print(f"a or b: {logical_or}, a | b: {bitwise_or}")     # Same result
print(f"not a: {logical_not}, ~a: {bitwise_not}")       # Different! (~True is -2)

# With integers, the behavior differs significantly
x, y = 5, 3  # 5 = 101, 3 = 011 in binary

print("\nWith integer values:")
# Logical operators evaluate truthiness
print(f"x and y: {x and y}")  # Returns y (3) because both are truthy
print(f"x or y: {x or y}")    # Returns x (5) because x is truthy (short-circuit)

# Bitwise operators work on the binary representation
print(f"x & y: {x & y}")  # 101 & 011 = 001 (1 in decimal)
print(f"x | y: {x | y}")  # 101 | 011 = 111 (7 in decimal)

# Important differences:
print("\nKey differences:")
print("1. Logical operators return the operand (not necessarily True/False)")
print("2. Bitwise operators always return a numeric result")
print("3. Logical operators short-circuit, bitwise operators always evaluate both")
print("4. Use logical operators for control flow, bitwise for bit manipulation")

print("\n" + "-" * 50 + "\n")

# ----------------------------------------------------------------------------
# 9. Common Mistakes and Best Practices
# ----------------------------------------------------------------------------

print("Common Mistakes and Best Practices:")

# Mistake 1: Confusing '==' (equality) with '=' (assignment)
x = 5
# if x = 10:  # This would cause a SyntaxError in Python (which is good)
#     print("x is 10")

# Correct
if x == 10:
    print("x is 10")
else:
    print("x is not 10")

# Mistake 2: Not understanding short-circuit evaluation
# This code is safe because of short-circuiting
user = None
if user and user.is_active:  # If user is None, user.is_active isn't evaluated
    print("User is active")
else:
    print("No active user")

# This would fail if user is None (AttributeError)
# if user.is_active:  # No check for None first
#     print("User is active")

# Mistake 3: Redundant boolean comparisons
is_valid = True

# Unnecessarily verbose
if is_valid == True:  # Redundant comparison
    print("Valid (verbose)")

# Cleaner version
if is_valid:
    print("Valid (clean)")

# Mistake 4: Not properly checking for empty collections
items = []

# Unnecessarily verbose
if len(items) == 0:  # Works but not Pythonic
    print("List is empty (verbose)")

# More Pythonic
if not items:  # Preferred way to check for empty collections
    print("List is empty (Pythonic)")

# Mistake 5: Complex boolean logic without parentheses
a, b, c = True, False, True

# Hard to understand at a glance
result = a and b or not c and a

# Better with parentheses for clarity
result = (a and b) or ((not c) and a)
print(f"\nResult with parentheses for clarity: {result}")

# Best Practices:
print("\nBest Practices:")
print("1. Use parentheses for complex expressions to clarify precedence")
print("2. Take advantage of short-circuit evaluation for efficiency")
print("3. Use 'in' operator for membership tests instead of multiple 'or' conditions")
print("4. Test boolean values directly, don't compare with True/False")
print("5. For empty checks, use 'if not collection:' rather than length comparisons")

print("\n" + "-" * 50 + "\n")

# ----------------------------------------------------------------------------
# 10. De Morgan's Laws in Python
# ----------------------------------------------------------------------------

print("De Morgan's Laws in Python:")

# De Morgan's Laws state:
# 1. not (a and b) == (not a) or (not b)
# 2. not (a or b) == (not a) and (not b)

a, b = True, False

# First law: not (a and b) == (not a) or (not b)
left_side = not (a and b)
right_side = (not a) or (not b)
print(f"Law 1: not (a and b) = {left_side}")
print(f"Law 1: (not a) or (not b) = {right_side}")
print(f"Law 1 holds: {left_side == right_side}")

# Second law: not (a or b) == (not a) and (not b)
left_side = not (a or b)
right_side = (not a) and (not b)
print(f"\nLaw 2: not (a or b) = {left_side}")
print(f"Law 2: (not a) and (not b) = {right_side}")
print(f"Law 2 holds: {left_side == right_side}")

# Practical application: simplifying complex conditions
customers = ["Alice", "Bob", "Charlie"]
premium_members = ["Alice", "David"]

# Complex condition
user = "Bob"
if not ((user in customers) and (user in premium_members)):
    print(f"\n{user} is not both a customer and premium member")

# Equivalent using De Morgan's Law
if (user not in customers) or (user not in premium_members):
    print(f"{user} is not both a customer and premium member (using De Morgan)")

print("\n" + "-" * 50 + "\n")

# ----------------------------------------------------------------------------
# SUMMARY:
# - Python has three logical operators: and, or, not
# - and: Returns True if both operands are True
# - or: Returns True if at least one operand is True
# - not: Returns the opposite boolean value
# - Short-circuit evaluation stops evaluating once the result is determined
# - Non-boolean values are converted to boolean based on their "truthiness"
# - Logical operators with non-booleans return the last evaluated operand
# - Operator precedence: not (highest), then and, then or (lowest)
# - Use parentheses to clarify complex expressions
# - Common applications: conditionals, filtering, input validation
# - De Morgan's Laws help simplify complex logical expressions
# ============================================================================ 