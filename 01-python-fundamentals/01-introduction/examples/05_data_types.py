# ============================================================================
# FILENAME: 05_data_types.py
# DESCRIPTION: Comprehensive examples of Python's basic data types
# ============================================================================

# ----------------------------------------------------------------------------
# 1. Integer (int) - Whole Numbers
# ----------------------------------------------------------------------------

# Integer literals
positive_int = 42         # Positive integer
negative_int = -73        # Negative integer
zero = 0                  # Zero is also an integer
large_int = 10000000000   # Large integers are handled automatically
readable_int = 1_000_000  # Underscores for readability (Python 3.6+)

# Integer operations
sum_result = 5 + 3        # Addition: 8
diff_result = 10 - 7      # Subtraction: 3
product = 4 * 6           # Multiplication: 24
quotient = 15 // 2        # Integer division: 7 (discards remainder)
remainder = 15 % 4        # Modulo (remainder): 3
power = 2 ** 3            # Exponentiation: 8

print("Integer Examples:")
print(f"Positive: {positive_int}, Negative: {negative_int}, Zero: {zero}")
print(f"Sum: {sum_result}, Difference: {diff_result}, Product: {product}")
print(f"Quotient: {quotient}, Remainder: {remainder}, Power: {power}")

# Integer properties
num = 42
print(f"\nInteger properties of {num}:")
print(f"Type: {type(num)}")               # Output: <class 'int'>
print(f"Max value: {num.bit_length()} bits")  # Minimum bits needed
print(f"Is it a boolean? {isinstance(num, bool)}")  # False

# ----------------------------------------------------------------------------
# 2. Floating-Point (float) - Decimal Numbers
# ----------------------------------------------------------------------------

# Float literals
pi = 3.14159              # Decimal notation
e = 2.71828               # Another float
negative_float = -0.5     # Negative float
sci_notation = 1.23e-4    # Scientific notation: 0.000123
sci_notation2 = 1.23e6    # Also scientific notation: 1230000.0

# Float operations
float_sum = 3.5 + 2.1     # Addition: 5.6
float_diff = 5.7 - 2.3    # Subtraction: 3.4
float_product = 2.5 * 3   # Multiplication: 7.5
float_division = 5 / 2    # Division: 2.5 (always returns float)
float_power = 2.0 ** 3    # Exponentiation: 8.0

print("\nFloat Examples:")
print(f"Pi: {pi}, e: {e}, Negative: {negative_float}")
print(f"Scientific notation: {sci_notation}, {sci_notation2}")
print(f"Sum: {float_sum}, Difference: {float_diff}, Product: {float_product}")
print(f"Division: {float_division}, Power: {float_power}")

# Float properties and precision
num = 0.1 + 0.2
print(f"\nFloat properties:")
print(f"Type: {type(num)}")  # Output: <class 'float'>
print(f"0.1 + 0.2 = {num}")  # Shows floating-point precision issues (0.30000000000000004)
print(f"Rounded: {round(num, 1)}")  # Rounded to 1 decimal place: 0.3

# ----------------------------------------------------------------------------
# 3. String (str) - Text Data
# ----------------------------------------------------------------------------

# String literals
single_quote = 'Python'              # Using single quotes
double_quote = "Programming"         # Using double quotes
triple_quote = """Multiple
line string"""                       # Using triple quotes for multi-line
escape_chars = "Tab: \t Newline: \n Backslash: \\"  # Escape characters
raw_string = r"C:\Users\name\Documents"  # Raw string (ignores escapes)
emoji = "😊 Python is fun! 🐍"       # Strings support Unicode (including emoji)

# String operations
greeting = "Hello"
name = "World"
concatenated = greeting + ", " + name + "!"  # Concatenation: "Hello, World!"
repeated = "Python " * 3              # Repetition: "Python Python Python "
substring = "Programming"[0:4]        # Slicing: "Prog"
uppercase = "python".upper()          # Upper case: "PYTHON"
lowercase = "PYTHON".lower()          # Lower case: "python"
word_count = "Python is amazing".split()  # Splitting: ['Python', 'is', 'amazing']
joined = ", ".join(["apples", "bananas", "cherries"])  # Joining: "apples, bananas, cherries"

print("\nString Examples:")
print(f"Single quote: {single_quote}")
print(f"Double quote: {double_quote}")
print(f"Triple quote: {triple_quote}")
print(f"Escape characters: {escape_chars}")
print(f"Raw string: {raw_string}")
print(f"Unicode/emoji: {emoji}")
print(f"Concatenation: {concatenated}")
print(f"Repetition: {repeated}")
print(f"Substring: {substring}")
print(f"Uppercase: {uppercase}, Lowercase: {lowercase}")
print(f"Split: {word_count}")
print(f"Joined: {joined}")

# String methods and properties
test_string = "Python Programming"
print(f"\nString properties and methods for '{test_string}':")
print(f"Length: {len(test_string)}")  # Length: 19
print(f"Contains 'Pro': {'Pro' in test_string}")  # True
print(f"Count of 'P': {test_string.count('P')}")  # 2
print(f"Index of 'P': {test_string.index('P')}")  # 0
print(f"Replace: {test_string.replace('Python', 'Java')}")  # "Java Programming"
print(f"Starts with 'Py': {test_string.startswith('Py')}")  # True
print(f"Ends with 'ing': {test_string.endswith('ing')}")  # True
print(f"Title case: {'hello world'.title()}")  # "Hello World"
print(f"Strip whitespace: {'  spaced  '.strip()}")  # "spaced"

# ----------------------------------------------------------------------------
# 4. Boolean (bool) - True or False Values
# ----------------------------------------------------------------------------

# Boolean literals
is_true = True   # Boolean True
is_false = False  # Boolean False

# Boolean operations
and_result = True and False  # Logical AND: False
or_result = True or False    # Logical OR: True
not_result = not True        # Logical NOT: False

print("\nBoolean Examples:")
print(f"True value: {is_true}, False value: {is_false}")
print(f"True AND False: {and_result}")
print(f"True OR False: {or_result}")
print(f"NOT True: {not_result}")

# Comparisons that return booleans
equality = (5 == 5)            # Equality: True
inequality = (5 != 10)         # Inequality: True
greater_than = (10 > 5)        # Greater than: True
less_than = (5 < 10)           # Less than: True
greater_equal = (5 >= 5)       # Greater than or equal: True
less_equal = (5 <= 10)         # Less than or equal: True

print("\nComparisons returning booleans:")
print(f"5 == 5: {equality}")
print(f"5 != 10: {inequality}")
print(f"10 > 5: {greater_than}")
print(f"5 < 10: {less_than}")
print(f"5 >= 5: {greater_equal}")
print(f"5 <= 10: {less_equal}")

# Values evaluated as True or False in boolean context
print("\nValues evaluated in boolean context:")
print(f"bool(0): {bool(0)}")              # False
print(f"bool(1): {bool(1)}")              # True
print(f"bool(42): {bool(42)}")            # True
print(f"bool(-3): {bool(-3)}")            # True
print(f"bool(''): {bool('')}")            # False (empty string)
print(f"bool('Hello'): {bool('Hello')}")  # True (non-empty string)
print(f"bool([]): {bool([])}")            # False (empty list)
print(f"bool([1, 2]): {bool([1, 2])}")    # True (non-empty list)
print(f"bool(None): {bool(None)}")        # False

# ----------------------------------------------------------------------------
# 5. None Type - Absence of a Value
# ----------------------------------------------------------------------------

# None represents the absence of a value
no_value = None
print("\nNone Type Examples:")
print(f"None value: {no_value}")
print(f"Type: {type(no_value)}")  # Output: <class 'NoneType'>
print(f"Is None: {no_value is None}")  # True
print(f"Boolean conversion: {bool(None)}")  # False

# Common use of None
def function_with_no_return():
    pass  # Function does nothing

result = function_with_no_return()
print(f"Function with no return gives: {result}")  # None

# ----------------------------------------------------------------------------
# 6. Additional Data Type Information
# ----------------------------------------------------------------------------

# Finding the type of a value
print("\nType information:")
print(f"Type of 42: {type(42)}")                 # <class 'int'>
print(f"Type of 3.14: {type(3.14)}")             # <class 'float'>
print(f"Type of 'hello': {type('hello')}")       # <class 'str'>
print(f"Type of True: {type(True)}")             # <class 'bool'>

# Type checking 
num = 42
print(f"\nType checking for {num}:")
print(f"Is int? {isinstance(num, int)}")         # True
print(f"Is float? {isinstance(num, float)}")     # False
print(f"Is numeric? {isinstance(num, (int, float))}")  # True
print(f"Is bool? {isinstance(num, bool)}")       # False (even though bool is a subclass of int)

# ----------------------------------------------------------------------------
# 7. Type Introspection and Limits
# ----------------------------------------------------------------------------

import sys

print("\nType Introspection:")
print(f"Integer max size: {'unlimited (depends on memory)'}")
print(f"Float max value: {sys.float_info.max}")  # Maximum float value
print(f"Float min value: {sys.float_info.min}")  # Minimum positive float value
print(f"Float epsilon: {sys.float_info.epsilon}")  # Smallest difference between floats

# ----------------------------------------------------------------------------
# SUMMARY:
# - Python has several built-in data types:
#   * Integer (int): Whole numbers like 42 or -7
#   * Float (float): Decimal numbers like 3.14 or -0.5
#   * String (str): Text data like "Hello" or 'Python'
#   * Boolean (bool): True or False values
#   * None: Represents the absence of a value
# - Each type has its own methods and operations
# - The type() function returns the data type of a value
# - isinstance() checks if a value is of a specific type
# - Type conversion functions (int(), float(), str(), bool()) convert between types
# - Python's dynamic typing allows variables to change types during execution
# ============================================================================ 