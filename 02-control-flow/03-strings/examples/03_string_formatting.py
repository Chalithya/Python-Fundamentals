# ============================================================================
# FILENAME: 03_string_formatting.py
# DESCRIPTION: Demonstrates various string formatting techniques in Python
# ============================================================================

# ----------------------------------------------------------------------------
# 1. Basic String Concatenation
# ----------------------------------------------------------------------------

print("BASIC STRING CONCATENATION:")

# Simple concatenation with +
name = "Python"
version = "3.9"
message = name + " " + version
print(f"Concatenation with +: {message}")

# String concatenation with multiple strings
message = name + " version " + version + " is awesome!"
print(f"Multiple concatenation: {message}")

# Concatenation with numbers (type conversion required)
year = 1991
release_message = name + " was first released in " + str(year)
print(f"Concatenation with numbers: {release_message}")

# ----------------------------------------------------------------------------
# 2. Old-style String Formatting (% operator)
# ----------------------------------------------------------------------------

print("\nOLD-STYLE STRING FORMATTING (% OPERATOR):")

# Basic formatting with %s (string) and %d (decimal/integer)
name = "Python"
version = 3.9
message = "%s version %.1f" % (name, version)
print(f"Basic % formatting: {message}")

# Multiple placeholders with different types
age = 30
price = 49.99
message = "Name: %s, Age: %d, Price: $%.2f" % (name, age, price)
print(f"Multiple placeholders: {message}")

# Named placeholders
message = "%(language)s is %(age)d years old" % {"language": "Python", "age": 30}
print(f"Named placeholders: {message}")

# Width and alignment
for num in range(1, 6):
    # Right-aligned with width 5
    print("Right-aligned: |%5d|" % num)

for num in range(1, 6):
    # Left-aligned with width 5
    print("Left-aligned: |%-5d|" % num)

# Zero padding
for num in range(1, 6):
    # Zero-padded with width 3
    print("Zero-padded: |%03d|" % num)

# ----------------------------------------------------------------------------
# 3. String format() Method
# ----------------------------------------------------------------------------

print("\nSTRING FORMAT() METHOD:")

# Basic usage with positional arguments
name = "Python"
version = 3.9
message = "{} version {}".format(name, version)
print(f"Basic format(): {message}")

# Specifying positions
message = "{1} version {0}".format(version, name)
print(f"Positional arguments: {message}")

# Named arguments
message = "{name} version {version}".format(name="Python", version=3.9)
print(f"Named arguments: {message}")

# Formatting numbers
pi = 3.14159265359
message = "Pi rounded to {:.2f}".format(pi)
print(f"Number formatting: {message}")

# Width and alignment
for num in range(1, 6):
    # Right-aligned with width 5
    print("Right-aligned: |{:5d}|".format(num))

for num in range(1, 6):
    # Left-aligned with width 5
    print("Left-aligned: |{:<5d}|".format(num))

for num in range(1, 6):
    # Center-aligned with width 5
    print("Center-aligned: |{:^5d}|".format(num))

# Thousands separator
large_num = 1000000
message = "Large number: {:,}".format(large_num)
print(f"Thousands separator: {message}")

# Binary, octal, and hexadecimal
num = 42
print("Binary: {:b}".format(num))
print("Octal: {:o}".format(num))
print("Hexadecimal: {:x}".format(num))
print("Hexadecimal (uppercase): {:X}".format(num))

# Percentage
percent = 0.75
print("Percentage: {:.1%}".format(percent))

# ----------------------------------------------------------------------------
# 4. F-strings (Formatted String Literals - Python 3.6+)
# ----------------------------------------------------------------------------

print("\nF-STRINGS (PYTHON 3.6+):")

# Basic usage
name = "Python"
version = 3.9
message = f"{name} version {version}"
print(f"Basic f-string: {message}")

# Expressions inside f-strings
a = 5
b = 10
message = f"{a} + {b} = {a + b}"
print(f"Expressions in f-strings: {message}")

# Calling methods inside f-strings
message = f"{name.lower()} version {version}"
print(f"Methods in f-strings: {message}")

# Formatting numbers in f-strings
pi = 3.14159265359
message = f"Pi rounded to {pi:.2f}"
print(f"Number formatting in f-strings: {message}")

# Width and alignment
for num in range(1, 6):
    # Right-aligned with width 5
    print(f"Right-aligned: |{num:5d}|")

for num in range(1, 6):
    # Left-aligned with width 5
    print(f"Left-aligned: |{num:<5d}|")

for num in range(1, 6):
    # Center-aligned with width 5
    print(f"Center-aligned: |{num:^5d}|")

# Thousands separator in f-strings
large_num = 1000000
message = f"Large number: {large_num:,}"
print(f"Thousands separator in f-strings: {message}")

# Binary, octal, and hexadecimal in f-strings
num = 42
print(f"Binary: {num:b}")
print(f"Octal: {num:o}")
print(f"Hexadecimal: {num:x}")
print(f"Hexadecimal (uppercase): {num:X}")

# Percentage in f-strings
percent = 0.75
print(f"Percentage: {percent:.1%}")

# F-strings with dictionaries
person = {"name": "Alice", "age": 30}
print(f"Name: {person['name']}, Age: {person['age']}")

# Debugging with f-strings (Python 3.8+)
name = "Python"
age = 30
# print(f"{name=}, {age=}")  # Uncomment for Python 3.8+

# ----------------------------------------------------------------------------
# 5. Template Strings
# ----------------------------------------------------------------------------

print("\nTEMPLATE STRINGS:")

from string import Template

# Basic template string
template = Template("$name is $age years old")
message = template.substitute(name="Python", age=30)
print(f"Basic template: {message}")

# Using a dictionary with template strings
values = {"name": "Python", "age": 30}
message = template.substitute(values)
print(f"Template with dictionary: {message}")

# Safe substitution (doesn't raise error for missing keys)
template = Template("$name is $age years old and created by $creator")
message = template.safe_substitute(values)
print(f"Safe substitution (missing key): {message}")

# ----------------------------------------------------------------------------
# 6. Format Specification Mini-Language
# ----------------------------------------------------------------------------

print("\nFORMAT SPECIFICATION MINI-LANGUAGE:")

# Syntax: [[fill]align][sign][#][0][width][grouping_option][.precision][type]

# Alignment options (< left, > right, ^ center) with fill character
num = 42
print(f"{'Left-aligned with hyphens:':<30}|{num:<10}|")
print(f"{'Right-aligned with hyphens':>30}|{num:>10}|")
print(f"{'Center-aligned with hyphens':^30}|{num:^10}|")
print(f"{'Fill with * (centered)':<30}|{num:*^10}|")

# Sign options (+ always show, - negative only (default), space for positive)
num_pos = 42
num_neg = -42
print(f"{'Default sign:':<30}|{num_pos:d}|{num_neg:d}|")
print(f"{'Always show sign:':<30}|{num_pos:+d}|{num_neg:+d}|")
print(f"{'Space for positive:':<30}|{num_pos: d}|{num_neg: d}|")

# Width, precision, and types
pi = 3.14159265359
print(f"{'Width of 10, 2 decimal places:':<30}|{pi:10.2f}|")
print(f"{'Width of 10, 4 decimal places:':<30}|{pi:10.4f}|")
print(f"{'Scientific notation:':<30}|{pi:.2e}|")
print(f"{'Fixed-point notation:':<30}|{pi:.2f}|")
print(f"{'General format (e or f):':<30}|{pi:.2g}|")
print(f"{'Percentage:':<30}|{0.25:.1%}|")

# Types for integers
num = 42
print(f"{'Decimal (default):':<30}|{num:d}|")
print(f"{'Binary:':<30}|{num:b}|")
print(f"{'Binary with prefix:':<30}|{num:#b}|")
print(f"{'Octal:':<30}|{num:o}|")
print(f"{'Octal with prefix:':<30}|{num:#o}|")
print(f"{'Hexadecimal (lower):':<30}|{num:x}|")
print(f"{'Hexadecimal (upper):':<30}|{num:X}|")
print(f"{'Hex with prefix (lower):':<30}|{num:#x}|")
print(f"{'Hex with prefix (upper):':<30}|{num:#X}|")
print(f"{'Character:':<30}|{65:c}|")  # ASCII 65 = 'A'

# Grouping options
large_num = 1234567890
print(f"{'No grouping:':<30}|{large_num:d}|")
print(f"{'Comma separator:':<30}|{large_num:,d}|")
print(f"{'Underscore separator:':<30}|{large_num:_d}|")

# ----------------------------------------------------------------------------
# SUMMARY:
# - Python offers several string formatting methods with increasing flexibility
# - The % operator offers C-style string formatting (legacy but still used)
# - The str.format() method provides a more flexible and readable alternative
# - F-strings (Python 3.6+) are the most concise and offer best performance
# - Template strings provide a simpler syntax for basic string substitution
# - The Format Specification Mini-Language provides detailed control over formatting
# - For modern Python code, f-strings are generally the preferred option
# ============================================================================ 