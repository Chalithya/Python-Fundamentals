# ============================================================================
# FILENAME: 02_string_methods.py
# DESCRIPTION: Demonstrates common string methods in Python
# ============================================================================

# ----------------------------------------------------------------------------
# 1. Case Conversion Methods
# ----------------------------------------------------------------------------

print("CASE CONVERSION METHODS:")

text = "Python Programming"

# Convert to uppercase
upper_case = text.upper()
print(f"upper(): {upper_case}")

# Convert to lowercase
lower_case = text.lower()
print(f"lower(): {lower_case}")

# Capitalize first letter
capitalized = "python".capitalize()
print(f"capitalize(): {capitalized}")

# Title case (capitalize first letter of each word)
title_case = "python programming".title()
print(f"title(): {title_case}")

# Swap case (upper to lower and vice versa)
swapped = "Python Programming".swapcase()
print(f"swapcase(): {swapped}")

# ----------------------------------------------------------------------------
# 2. Search and Replace Methods
# ----------------------------------------------------------------------------

print("\nSEARCH AND REPLACE METHODS:")

text = "Python is powerful and Python is easy to learn"

# Check if string starts or ends with specific text
starts_with_py = text.startswith("Python")
ends_with_learn = text.endswith("learn")
print(f"startswith('Python'): {starts_with_py}")
print(f"endswith('learn'): {ends_with_learn}")

# Find the position of a substring
first_python = text.find("Python")
second_python = text.find("Python", first_python + 1)
print(f"find('Python') first occurrence: {first_python}")
print(f"find('Python') second occurrence: {second_python}")

# Count occurrences of a substring
python_count = text.count("Python")
print(f"count('Python'): {python_count}")

# Replace substrings
replaced = text.replace("Python", "Ruby")
print(f"replace('Python', 'Ruby'): {replaced}")

# Replace with limit
replaced_once = text.replace("Python", "Ruby", 1)
print(f"replace('Python', 'Ruby', 1): {replaced_once}")

# ----------------------------------------------------------------------------
# 3. Stripping Whitespace
# ----------------------------------------------------------------------------

print("\nSTRIPPING WHITESPACE:")

padded_text = "   Python Programming   "
print(f"Original: '{padded_text}'")

# Remove whitespace from both ends
stripped = padded_text.strip()
print(f"strip(): '{stripped}'")

# Remove whitespace from left end
left_stripped = padded_text.lstrip()
print(f"lstrip(): '{left_stripped}'")

# Remove whitespace from right end
right_stripped = padded_text.rstrip()
print(f"rstrip(): '{right_stripped}'")

# Strip specific characters
text_with_symbols = "###Python Programming###"
print(f"Original with symbols: '{text_with_symbols}'")
stripped_symbols = text_with_symbols.strip('#')
print(f"strip('#'): '{stripped_symbols}'")

# ----------------------------------------------------------------------------
# 4. String Splitting and Joining
# ----------------------------------------------------------------------------

print("\nSTRING SPLITTING AND JOINING:")

# Splitting a string into a list
text = "Python,Java,C++,JavaScript"
languages = text.split(",")
print(f"split(','): {languages}")

# Split with maximum splits
first_two = text.split(",", 2)
print(f"split(',', 2): {first_two}")

# Split by whitespace
sentence = "Python is a programming language"
words = sentence.split()
print(f"split() (default splits by whitespace): {words}")

# Splitting by lines
multi_line = """Line 1
Line 2
Line 3"""
lines = multi_line.splitlines()
print(f"splitlines(): {lines}")

# Joining a list into a string
joined = ", ".join(languages)
print(f"', '.join(languages): {joined}")

# Join with different separators
dash_joined = "-".join(languages)
print(f"'-'.join(languages): {dash_joined}")

# ----------------------------------------------------------------------------
# 5. String Testing Methods
# ----------------------------------------------------------------------------

print("\nSTRING TESTING METHODS:")

# Checking if string is alphanumeric
alphanumeric = "Python3"
print(f"'{alphanumeric}'.isalnum(): {alphanumeric.isalnum()}")

# Checking if string is alphabetic
alphabetic = "Python"
print(f"'{alphabetic}'.isalpha(): {alphabetic.isalpha()}")

# Checking if string is digit
digit = "12345"
print(f"'{digit}'.isdigit(): {digit.isdigit()}")

# Checking if string is numeric (more comprehensive than isdigit)
numeric = "12³"  # Superscript 3 is numeric but not a digit
print(f"'{numeric}'.isnumeric(): {numeric.isnumeric()}")
print(f"'{numeric}'.isdigit(): {numeric.isdigit()}")

# Checking if string is lowercase
lower = "python"
print(f"'{lower}'.islower(): {lower.islower()}")

# Checking if string is uppercase
upper = "PYTHON"
print(f"'{upper}'.isupper(): {upper.isupper()}")

# Checking if string is title case
title = "Python Programming"
print(f"'{title}'.istitle(): {title.istitle()}")

# Checking if string is space
space = "   "
print(f"'   '.isspace(): {space.isspace()}")

# ----------------------------------------------------------------------------
# 6. String Alignment and Filling
# ----------------------------------------------------------------------------

print("\nSTRING ALIGNMENT AND FILLING:")

text = "Python"

# Center alignment
centered = text.center(20)
print(f"center(20): '{centered}'")

# Center with custom fill character
centered_stars = text.center(20, '*')
print(f"center(20, '*'): '{centered_stars}'")

# Left alignment (ljust)
left_aligned = text.ljust(20)
print(f"ljust(20): '{left_aligned}'")

# Right alignment (rjust)
right_aligned = text.rjust(20)
print(f"rjust(20): '{right_aligned}'")

# Zero-padding numbers
number = "42"
zero_padded = number.zfill(5)
print(f"'42'.zfill(5): '{zero_padded}'")

# ----------------------------------------------------------------------------
# 7. String Formatting Methods
# ----------------------------------------------------------------------------

print("\nSTRING FORMATTING METHODS:")

# Old style formatting with %
old_style = "Name: %s, Age: %d" % ("Python", 30)
print(f"Old style (%): {old_style}")

# str.format() method
formatted = "Name: {}, Age: {}".format("Python", 30)
print(f"str.format(): {formatted}")

# str.format() with indexed parameters
indexed = "{1} was created by {0}".format("Guido van Rossum", "Python")
print(f"str.format() with index: {indexed}")

# str.format() with named parameters
named = "{name} is {age} years old".format(name="Python", age=30)
print(f"str.format() with named params: {named}")

# f-strings (Python 3.6+)
name = "Python"
age = 30
f_string = f"{name} is {age} years old"
print(f"f-string: {f_string}")

# f-string expressions
x = 10
y = 5
expression = f"{x} + {y} = {x + y}"
print(f"f-string with expression: {expression}")

# ----------------------------------------------------------------------------
# 8. Advanced Methods
# ----------------------------------------------------------------------------

print("\nADVANCED METHODS:")

# Translating characters
translation_table = str.maketrans("aeiou", "12345")
translated = "Python Programming".translate(translation_table)
print(f"translate(): {translated}")

# Partition - splits into before, separator, after
before, sep, after = "Python is fun".partition(" is ")
print(f"partition(' is '): {(before, sep, after)}")

# Expandtabs - replace tabs with spaces
tabbed = "Python\tProgramming\tLanguage"
expanded = tabbed.expandtabs(16)
print(f"Original with tabs: '{tabbed}'")
print(f"expandtabs(16): '{expanded}'")

# ----------------------------------------------------------------------------
# SUMMARY:
# - Python provides a rich set of string methods for various operations
# - Case conversion: upper(), lower(), capitalize(), title(), swapcase()
# - Searching: find(), rfind(), index(), count(), startswith(), endswith()
# - Stripping: strip(), lstrip(), rstrip()
# - Splitting/Joining: split(), splitlines(), join()
# - Testing: isalnum(), isalpha(), isdigit(), islower(), isupper(), etc.
# - Alignment: center(), ljust(), rjust(), zfill()
# - Formatting: % operator, str.format(), f-strings
# - All string methods return new strings (because strings are immutable)
# ============================================================================ 