# ============================================================================
# FILENAME: 02_variables.py
# DESCRIPTION: Demonstration of Python variables, naming rules, and data types
# ============================================================================

# ----------------------------------------------------------------------------
# 1. Variable Declaration and Assignment
# ----------------------------------------------------------------------------

# In Python, variables are created when you assign a value
name = "John"         # A string variable
age = 25              # An integer variable 
height = 1.75         # A floating-point variable
is_student = True     # A boolean variable

# You can print variables along with text
print("Name:", name)          # Output: Name: John
print("Age:", age)            # Output: Age: 25
print("Height:", height)      # Output: Height: 1.75
print("Is student:", is_student)  # Output: Is student: True

# ----------------------------------------------------------------------------
# 2. Variable Naming Rules and Conventions
# ----------------------------------------------------------------------------

# Valid variable names
user_name = "Alice"       # Snake case (recommended for Python)
userName = "Bob"          # Camel case
UserName = "Charlie"      # Pascal case
_hidden = "Secret"        # Starting with underscore is valid
name2 = "David"           # Numbers are allowed (but not at the start)
NAME = "CONSTANT"         # ALL_CAPS usually indicates a constant

# These would cause errors (commented out to prevent the program from crashing)
# 2name = "Invalid"        # Cannot start with a number
# user-name = "Invalid"    # Cannot use hyphens
# class = "Invalid"        # Cannot use Python reserved keywords

# Python reserved keywords include:
# and, as, assert, break, class, continue, def, del, elif, else, except,
# False, finally, for, from, global, if, import, in, is, lambda, None,
# nonlocal, not, or, pass, raise, return, True, try, while, with, yield

# ----------------------------------------------------------------------------
# 3. Multiple Assignments
# ----------------------------------------------------------------------------

# Assign the same value to multiple variables
x = y = z = 0
print("x =", x, "y =", y, "z =", z)  # Output: x = 0 y = 0 z = 0

# Assign multiple values to multiple variables
a, b, c = 1, 2, 3
print("a =", a, "b =", b, "c =", c)  # Output: a = 1 b = 2 c = 3

# Swap variables (a Python-specific trick)
a, b = b, a
print("After swap: a =", a, "b =", b)  # Output: After swap: a = 2 b = 1

# ----------------------------------------------------------------------------
# 4. Data Types in Python
# ----------------------------------------------------------------------------

# Integer (int) - whole numbers
count = 100
negative_num = -42
big_num = 1_000_000  # Underscores for readability (Python 3.6+)
print("Integer examples:", count, negative_num, big_num) # Output: Integer examples: 100 -42 1000000

# Floating-point (float) - numbers with decimal places
pi = 3.14159
e = 2.71828
negative_float = -0.5
print("Float examples:", pi, e, negative_float) # Output: Float examples: 3.14159 2.71828 -0.5

# String (str) - text
single_quoted = 'Single quotes'
double_quoted = "Double quotes"
triple_quoted = """Triple quotes
allow multi-line text
like this"""
print("String example:", single_quoted) # Output: String example: Single quotes

# Boolean (bool) - True or False
is_valid = True
has_error = False
print("Boolean examples:", is_valid, has_error) # Output: Boolean examples: True False

# None type - represents the absence of a value
empty_value = None
print("None example:", empty_value)  # Output: None example: None

# ----------------------------------------------------------------------------
# 5. Checking Variable Types
# ----------------------------------------------------------------------------

# The type() function returns the data type of a variable
print("Type of name:", type(name))            # Output: <class 'str'>
print("Type of age:", type(age))              # Output: <class 'int'>
print("Type of height:", type(height))        # Output: <class 'float'>
print("Type of is_student:", type(is_student))  # Output: <class 'bool'>
print("Type of empty_value:", type(empty_value))  # Output: <class 'NoneType'>

# ----------------------------------------------------------------------------
# 6. Variable Scope and Re-assignment
# ----------------------------------------------------------------------------

# Variables can be reassigned to new values
count = 100
print("Original count:", count)  # Output: Original count: 100

count = 200
print("New count:", count)  # Output: New count: 200

# Variables can be reassigned to different types (dynamic typing)
variable = 10
print("Variable (integer):", variable)  # Output: Variable (integer): 10

variable = "Now I'm a string"
print("Variable (string):", variable)  # Output: Variable (string): Now I'm a string

# ----------------------------------------------------------------------------
# SUMMARY:
# - Variables are created when you assign a value (no declaration needed)
# - Python uses dynamic typing (variables can change type)
# - Follow naming conventions: lowercase with underscores (snake_case)
# - Variable names can contain letters, numbers, and underscores
# - Cannot start with a number or use Python keywords
# - Basic data types: int, float, str, bool, None
# - The type() function shows a variable's data type
# - Variables can be reassigned at any time
# ============================================================================ 