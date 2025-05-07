# ============================================================================
# FILENAME: 01_string_basics.py
# DESCRIPTION: Demonstrates basic string creation and operations in Python
# ============================================================================

# ----------------------------------------------------------------------------
# 1. String Creation
# ----------------------------------------------------------------------------

print("STRING CREATION:")

# Different ways to create strings
single_quoted = 'Hello, World!'
double_quoted = "Hello, World!"
triple_quoted = """This is a
multi-line string."""

print(f"Single quoted: {single_quoted}")
print(f"Double quoted: {double_quoted}")
print(f"Triple quoted: {triple_quoted}")

# Escape sequences in strings
with_quotes = "She said, \"Python is fun!\""
with_newline = "First line.\nSecond line."
with_tab = "Name:\tPython"
with_backslash = "File path: C:\\Users\\Documents"

print(f"\nWith quotes: {with_quotes}")
print(f"With newline: {with_newline}")
print(f"With tab: {with_tab}")
print(f"With backslash: {with_backslash}")

# Raw strings (ignore escape sequences)
raw_string = r"C:\Users\Documents\file.txt"
print(f"\nRaw string: {raw_string}")

# ----------------------------------------------------------------------------
# 2. String Concatenation and Repetition
# ----------------------------------------------------------------------------

print("\nSTRING CONCATENATION AND REPETITION:")

# Concatenation using + operator
first_name = "Python"
last_name = "Programming"
full_name = first_name + " " + last_name
print(f"Concatenation: {full_name}")

# String repetition using * operator
repeated = "Python! " * 3
print(f"Repetition: {repeated}")

# Concatenation in a loop
pieces = ["P", "y", "t", "h", "o", "n"]
result = ""
for piece in pieces:
    result += piece
print(f"Concatenation in loop: {result}")

# Joining strings (more efficient than +=)
joined = "".join(pieces)
print(f"Using join(): {joined}")

# ----------------------------------------------------------------------------
# 3. String Length and Membership
# ----------------------------------------------------------------------------

print("\nSTRING LENGTH AND MEMBERSHIP:")

# String length
text = "Python Programming"
length = len(text)
print(f"Length of '{text}': {length}")

# Membership tests
contains_py = "Py" in text
contains_java = "Java" in text
print(f"Contains 'Py': {contains_py}")
print(f"Contains 'Java': {contains_java}")

# Membership in conditional statements
if "thon" in text:
    print("'thon' is part of the text")
    
if "ruby" not in text:
    print("'ruby' is not part of the text")

# ----------------------------------------------------------------------------
# 4. String Indexing and Slicing
# ----------------------------------------------------------------------------

print("\nSTRING INDEXING AND SLICING:")

text = "Python Programming"

# Individual character access
first_char = text[0]
fifth_char = text[4]
print(f"First character: {first_char}")
print(f"Fifth character: {fifth_char}")

# Negative indexing (from the end)
last_char = text[-1]
second_last = text[-2]
print(f"Last character: {last_char}")
print(f"Second last character: {second_last}")

# Slicing
first_word = text[0:6]  # or text[:6]
second_word = text[7:]
print(f"First word: {first_word}")
print(f"Second word: {second_word}")

# Slicing with steps
every_second = text[::2]
reversed_text = text[::-1]
print(f"Every second character: {every_second}")
print(f"Reversed text: {reversed_text}")

# Partial slices
middle = text[3:10]
print(f"Middle section: {middle}")

# ----------------------------------------------------------------------------
# 5. String Immutability
# ----------------------------------------------------------------------------

print("\nSTRING IMMUTABILITY:")

text = "Python"
print(f"Original text: {text}")

# Strings cannot be modified in-place
try:
    text[0] = "J"  # This will raise an error
except TypeError as e:
    print(f"Error: {e}")

# Instead, create a new string
new_text = "J" + text[1:]
print(f"New text: {new_text}")

# ----------------------------------------------------------------------------
# 6. String Comparison
# ----------------------------------------------------------------------------

print("\nSTRING COMPARISON:")

str1 = "apple"
str2 = "banana"
str3 = "APPLE"
str4 = "apple"

print(f"str1 == str4: {str1 == str4}")  # Same content
print(f"str1 == str3: {str1 == str3}")  # Different case
print(f"str1 != str2: {str1 != str2}")  # Different content

print(f"str1 < str2: {str1 < str2}")    # Lexicographical comparison
print(f"str1 > str3: {str1 > str3}")    # ASCII/Unicode comparison

# Case-insensitive comparison
print(f"Case-insensitive comparison: {str1.lower() == str3.lower()}")

# ----------------------------------------------------------------------------
# SUMMARY:
# - Strings can be created with single, double, or triple quotes
# - Special characters can be represented with escape sequences
# - Strings can be concatenated with + and repeated with *
# - String length is found with len() and membership with in operator
# - Individual characters are accessed with [index]
# - Slices of strings use [start:end:step] notation
# - Strings are immutable - they cannot be changed in-place
# - String comparison is case-sensitive and follows lexicographical order
# ============================================================================ 