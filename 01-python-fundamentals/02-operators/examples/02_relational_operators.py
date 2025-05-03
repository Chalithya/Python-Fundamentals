# ============================================================================
# FILENAME: 02_relational_operators.py
# DESCRIPTION: Demonstrates the use of relational operators in Python
# ============================================================================

# ----------------------------------------------------------------------------
# 1. Basic Relational Operators
# ----------------------------------------------------------------------------

a = 10
b = 5
c = 10

# Equal to (==)
# Returns True if the values are equal
equal_result = a == b
print(f"{a} == {b}: {equal_result}")  # Output: False

equal_result = a == c
print(f"{a} == {c}: {equal_result}")  # Output: True

# Not equal to (!=)
# Returns True if the values are not equal
not_equal_result = a != b
print(f"{a} != {b}: {not_equal_result}")  # Output: True

not_equal_result = a != c
print(f"{a} != {c}: {not_equal_result}")  # Output: False

# Greater than (>)
# Returns True if the left value is greater than the right value
greater_result = a > b
print(f"{a} > {b}: {greater_result}")  # Output: True

greater_result = a > c
print(f"{a} > {c}: {greater_result}")  # Output: False

# Less than (<)
# Returns True if the left value is less than the right value
less_result = a < b
print(f"{a} < {b}: {less_result}")  # Output: False

less_result = b < a
print(f"{b} < {a}: {less_result}")  # Output: True

# Greater than or equal to (>=)
# Returns True if the left value is greater than or equal to the right value
greater_equal_result = a >= b
print(f"{a} >= {b}: {greater_equal_result}")  # Output: True

greater_equal_result = a >= c
print(f"{a} >= {c}: {greater_equal_result}")  # Output: True

# Less than or equal to (<=)
# Returns True if the left value is less than or equal to the right value
less_equal_result = a <= b
print(f"{a} <= {b}: {less_equal_result}")  # Output: False

less_equal_result = a <= c
print(f"{a} <= {c}: {less_equal_result}")  # Output: True

print("\n" + "-" * 50 + "\n")

# ----------------------------------------------------------------------------
# 2. Using Relational Operators in Control Structures
# ----------------------------------------------------------------------------

# If statements
age = 20
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

# Nested if-else statements
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# Using relational operators in while loops
counter = 1
while counter <= 5:
    print(f"Loop iteration: {counter}")
    counter += 1

print("\n" + "-" * 50 + "\n")

# ----------------------------------------------------------------------------
# 3. Chained Comparisons
# ----------------------------------------------------------------------------

# Python allows chaining multiple comparisons
# This is more concise than using logical operators

x = 15

# These two expressions are equivalent:
# Using logical AND
result1 = x > 10 and x < 20
print(f"{x} > 10 and {x} < 20: {result1}")  # Output: True

# Using chained comparison (more pythonic)
result2 = 10 < x < 20
print(f"10 < {x} < 20: {result2}")  # Output: True

# More complex chained comparisons
a, b, c = 3, 5, 7
result3 = a < b < c
print(f"{a} < {b} < {c}: {result3}")  # Output: True

# Chained comparisons with different operators
result4 = 1 <= x <= 10
print(f"1 <= {x} <= 10: {result4}")  # Output: False

result5 = a < b > 2
print(f"{a} < {b} > 2: {result5}")  # Output: True

# Note: Chained comparisons use short-circuit evaluation
# Each value is evaluated only once

print("\n" + "-" * 50 + "\n")

# ----------------------------------------------------------------------------
# 4. Comparing Different Data Types
# ----------------------------------------------------------------------------

# Comparing strings (lexicographical comparison)
str1 = "apple"
str2 = "banana"
print(f"'{str1}' < '{str2}': {str1 < str2}")  # Output: True (alphabetically)
print(f"'A' < 'a': {'A' < 'a'}")  # Output: True (ASCII value comparison)

# Comparing different types may work but is not recommended
# In Python 3, comparing different numeric types works
print(f"5 == 5.0: {5 == 5.0}")  # Output: True

# But comparing numbers to strings doesn't work in Python 3
try:
    result = 5 < "10"
    print(f"5 < '10': {result}")
except TypeError as e:
    print(f"Error: {e}")  # Output: Error: '<' not supported between instances of 'int' and 'str'

# Comparing sequences (list, tuple)
list1 = [1, 2, 3]
list2 = [1, 2, 4]
list3 = [1, 2, 3, 0]

print(f"{list1} < {list2}: {list1 < list2}")  # Output: True
# Compares item by item until a difference is found
print(f"{list1} < {list3}: {list1 < list3}")  # Output: True
# If all elements match but one list is longer, the shorter list is smaller

print("\n" + "-" * 50 + "\n")

# ----------------------------------------------------------------------------
# 5. Object Identity vs Value Equality (== vs is)
# ----------------------------------------------------------------------------

# == checks for value equality
# is checks for identity (same object)

a = [1, 2, 3]
b = [1, 2, 3]  # Same values but different list objects
c = a          # c references the same list object as a

print(f"a == b: {a == b}")  # Output: True (same values)
print(f"a is b: {a is b}")  # Output: False (different objects)
print(f"a is c: {a is c}")  # Output: True (same object)

# ID function shows the memory address of an object
print(f"id(a): {id(a)}")
print(f"id(b): {id(b)}")
print(f"id(c): {id(c)}")

# Integer cache in Python (implementation detail)
# Small integers are pre-cached for efficiency
x = 5
y = 5
print(f"x == y: {x == y}")  # Output: True (same values)
print(f"x is y: {x is y}")  # Output: True (likely same objects due to caching)

# This may not apply to larger integers
large_x = 1000
large_y = 1000
print(f"large_x == large_y: {large_x == large_y}")  # Output: True (same values)
print(f"large_x is large_y: {large_x is large_y}")  # Output: May vary by Python implementation

print("\n" + "-" * 50 + "\n")

# ----------------------------------------------------------------------------
# 6. Floating-Point Comparisons and Precision Issues
# ----------------------------------------------------------------------------

# Floating-point arithmetic may lead to surprising results
a = 0.1 + 0.2
b = 0.3
print(f"0.1 + 0.2 = {a}")
print(f"0.3 = {b}")
print(f"0.1 + 0.2 == 0.3: {a == b}")  # Output: False (due to floating-point precision)

# Better approach for comparing floats: use a small epsilon (tolerance)
epsilon = 1e-10  # Very small threshold value
print(f"abs((0.1 + 0.2) - 0.3) < epsilon: {abs(a - b) < epsilon}")  # Output: True

# Using Python's built-in module for safer float comparison
import math
print(f"math.isclose(0.1 + 0.2, 0.3): {math.isclose(a, b)}")  # Output: True

print("\n" + "-" * 50 + "\n")

# ----------------------------------------------------------------------------
# 7. Practical Applications
# ----------------------------------------------------------------------------

# Input validation
user_age = 16
if user_age < 0:
    print("Error: Age cannot be negative")
elif user_age < 18:
    print("Access denied: You must be 18 or older")
else:
    print("Access granted")

# Range checking
temperature = 72.5
if 70 <= temperature <= 75:
    print("Temperature is in the optimal range")
else:
    print("Temperature is out of the optimal range")

# Sorting and searching
scores = [85, 92, 78, 95, 88]
scores.sort()  # Uses comparisons internally
print(f"Sorted scores: {scores}")

# Find scores above a threshold
threshold = 85
high_scores = [score for score in scores if score >= threshold]
print(f"Scores >= {threshold}: {high_scores}")

# Data validation with if-else
def validate_username(username):
    if len(username) < 3:
        return "Username too short"
    elif len(username) > 20:
        return "Username too long"
    else:
        return "Username valid"

print(validate_username("al"))     # Too short
print(validate_username("alice"))  # Valid
print(validate_username("a" * 25)) # Too long

print("\n" + "-" * 50 + "\n")

# ----------------------------------------------------------------------------
# 8. Common Mistakes and Best Practices
# ----------------------------------------------------------------------------

# Common mistake: Using assignment (=) instead of equality (==)
x = 5
if x == 10:  # Correct: comparison
    print("x equals 10")
else:
    print("x does not equal 10")

# This would be a mistake (assignment, not comparison):
# if x = 10:  # SyntaxError in Python (which is good)
#     print("This would always execute and modify x!")

# Best practice: Use 'in' for multiple equality checks
color = "green"
# Instead of:
if color == "red" or color == "green" or color == "blue":
    print("Primary RGB color")
# Better approach:
if color in ["red", "green", "blue"]:
    print("Primary RGB color")

# Best practice: Be careful with None comparisons
result = None
# Preferred way to check for None (using identity)
if result is None:
    print("Result is None")

# Best practice: Use parentheses for clarity in complex conditions
a, b, c = 5, 10, 15
if (a < b) and (b < c):
    print("Values are in ascending order")

print("\n" + "-" * 50 + "\n")

# ----------------------------------------------------------------------------
# SUMMARY:
# - Relational operators compare values and return boolean results
# - Python has six main relational operators: ==, !=, >, <, >=, <=
# - Chained comparisons allow for concise, readable code
# - Use 'is' for identity comparison and '==' for value comparison
# - Be cautious with floating-point comparisons due to precision issues
# - Understand how Python compares different data types
# - Use appropriate operators when None is involved (is/is not)
# - Relational operators are fundamental to control structures and logic
# ============================================================================ 