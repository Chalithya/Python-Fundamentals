# ============================================================================
# FILENAME: 03_print_function.py
# DESCRIPTION: Demonstrating the versatility of Python's print function
# ============================================================================

# ----------------------------------------------------------------------------
# 1. Basic Print Function Usage
# ----------------------------------------------------------------------------

# Print a simple string
print("Hello, Python!")  # Output: Hello, Python!

# Print multiple values separated by commas
print("Name:", "Alice", "Age:", 30)  # Output: Name: Alice Age: 30

# Print numbers and expressions
print(42)                # Output: 42
print(10 + 5)           # Output: 15
print(2 * 3)            # Output: 6

# ----------------------------------------------------------------------------
# 2. Print Formatting Options
# ----------------------------------------------------------------------------

name = "Bob"
age = 25
height = 1.75

# Method 1: Using string concatenation (not recommended)
print("Name: " + name + ", Age: " + str(age))  # Output: Name: Bob, Age: 25

# Method 2: Using the comma separator (automatically adds spaces)
print("Name:", name, "Age:", age, "Height:", height)  # Output: Name: Bob Age: 25 Height: 1.75

# Method 3: Using f-strings (Python 3.6+) - recommended
print(f"Name: {name}, Age: {age}, Height: {height}m")  # Output: Name: Bob, Age: 25, Height: 1.75m

# Method 4: Using the format() method
print("Name: {}, Age: {}, Height: {}m".format(name, age, height))  # Output: Name: Bob, Age: 25, Height: 1.75m

# With format() you can rearrange the order
print("{2}, {0}, {1}".format("one", "two", "three"))  # Output: three, one, two

# Method 5: Using the % operator (older style)
print("Name: %s, Age: %d, Height: %.2fm" % (name, age, height))  # Output: Name: Bob, Age: 25, Height: 1.75m

# ----------------------------------------------------------------------------
# 3. Print Function Parameters
# ----------------------------------------------------------------------------

# The sep parameter changes the separator between items (default is space)
print("Apple", "Banana", "Cherry", sep=", ")  # Output: Apple, Banana, Cherry
print("Apple", "Banana", "Cherry", sep=" | ")  # Output: Apple | Banana | Cherry
print("Apple", "Banana", "Cherry", sep="")  # Output: AppleBananaCherry

# The end parameter changes what's printed at the end (default is newline)
print("Hello", end=" ")
print("World")  # Output: Hello World

# Combining sep and end
print("First", "Second", sep="-", end="...\n")
print("Third")  # Output: First-Second...
                # Third

# ----------------------------------------------------------------------------
# 4. Printing Special Characters
# ----------------------------------------------------------------------------

# Escape sequences for special characters
print("Line 1\nLine 2")  # \n creates a new line
# Output:
# Line 1
# Line 2

print("Column 1\tColumn 2")  # \t creates a tab
# Output: Column 1	Column 2

print("Quotes: \"Double\" and \'Single\'")  # Escaping quotes
# Output: Quotes: "Double" and 'Single'

print("Backslash: \\")  # Escaping a backslash
# Output: Backslash: \

# ----------------------------------------------------------------------------
# 5. Advanced Formatting with f-strings (Python 3.6+)
# ----------------------------------------------------------------------------

name = "Alice"
age = 30
pi = 3.14159265359

# Format numbers
print(f"Age: {age:d}")  # Output: Age: 30 (as decimal)
print(f"Pi: {pi:.2f}")  # Output: Pi: 3.14 (2 decimal places)
print(f"Pi: {pi:.5f}")  # Output: Pi: 3.14159 (5 decimal places)

# Format with padding
print(f"Name: {name:10}")  # Output: Name: Alice     (right-padded to 10 chars)
print(f"Name: {name:>10}")  # Output: Name:      Alice (left-padded to 10 chars)
print(f"Name: {name:^10}")  # Output: Name:   Alice   (centered in 10 chars)

# Format with separators for large numbers
population = 1000000
print(f"Population: {population:,}")  # Output: Population: 1,000,000

# Format as percentage
ratio = 0.75
print(f"Completion: {ratio:.1%}")  # Output: Completion: 75.0%

# Format as binary, octal, or hexadecimal
num = 42
print(f"Decimal: {num:d}, Binary: {num:b}, Octal: {num:o}, Hex: {num:x}")
# Output: Decimal: 42, Binary: 101010, Octal: 52, Hex: 2a

# ----------------------------------------------------------------------------
# 6. Printing to Files
# ----------------------------------------------------------------------------

# Print to a file (uncommenting these will create files in your working directory)
# with open("output.txt", "w") as file:
#     print("This will be written to a file", file=file)
#     print("Multiple lines can be written", file=file)

# ----------------------------------------------------------------------------
# SUMMARY:
# - The print() function displays output to the console
# - Multiple values can be printed by separating them with commas
# - Modern formatting uses f-strings (Python 3.6+) for readability
# - The sep parameter changes the separator between items
# - The end parameter changes what prints at the end of the line
# - Escape sequences (\n, \t, etc.) create special characters
# - Advanced formatting options control number display, padding, alignment
# - print() can output to files using the file parameter
# ============================================================================ 