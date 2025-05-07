# ============================================================================
# FILENAME: 01_list_basics.py
# DESCRIPTION: Demonstrates basic list creation and operations in Python
# ============================================================================

# ----------------------------------------------------------------------------
# 1. Creating Lists
# ----------------------------------------------------------------------------

print("CREATING LISTS:")

# Empty list
empty_list = []
print(f"Empty list: {empty_list}")

# List of numbers
numbers = [1, 2, 3, 4, 5]
print(f"Numbers: {numbers}")

# List with mixed data types
mixed = [1, "Hello", 3.14, True]
print(f"Mixed data types: {mixed}")

# Create a list using the list() constructor
from_constructor = list("Python")  # Creates a list of characters
print(f"From constructor: {from_constructor}")

# Create a list with repeated elements
repeated = [0] * 5
print(f"Repeated: {repeated}")

# List of lists (nested list)
nested = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"Nested list: {nested}")

# ----------------------------------------------------------------------------
# 2. Accessing List Elements
# ----------------------------------------------------------------------------

print("\nACCESSING ELEMENTS:")

fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Access by positive index (0-based)
print(f"First fruit: {fruits[0]}")
print(f"Third fruit: {fruits[2]}")

# Access by negative index (counts from the end)
print(f"Last fruit: {fruits[-1]}")
print(f"Second-to-last fruit: {fruits[-2]}")

# Get the length of a list
print(f"Number of fruits: {len(fruits)}")

# Access elements in a nested list
print(f"Element at row 1, column 2 in nested list: {nested[1][2]}")

# ----------------------------------------------------------------------------
# 3. List Slicing
# ----------------------------------------------------------------------------

print("\nLIST SLICING:")

# Basic slicing [start:end] (end is exclusive)
print(f"First three fruits: {fruits[0:3]}")
print(f"Same with implicit start: {fruits[:3]}")

# Slicing from an index to the end
print(f"From third fruit to end: {fruits[2:]}")

# Slicing with negative indices
print(f"Last three fruits: {fruits[-3:]}")
print(f"All except last two: {fruits[:-2]}")

# Slicing with step [start:end:step]
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Every second number: {numbers[::2]}")
print(f"Every third number starting from 1: {numbers[1::3]}")

# Reversing a list with slicing
print(f"Reversed list: {numbers[::-1]}")

# ----------------------------------------------------------------------------
# 4. Modifying Lists
# ----------------------------------------------------------------------------

print("\nMODIFYING LISTS:")

colors = ["red", "green", "blue"]
print(f"Original colors: {colors}")

# Change an element
colors[0] = "dark red"
print(f"After changing first element: {colors}")

# Add element to the end
colors.append("yellow")
print(f"After append: {colors}")

# Insert at specific position
colors.insert(2, "purple")
print(f"After insert: {colors}")

# Extend with another list
colors.extend(["pink", "orange"])
print(f"After extend: {colors}")

# Remove by value (first occurrence)
colors.remove("blue")
print(f"After removing 'blue': {colors}")

# Remove by index and get value
popped = colors.pop(1)
print(f"Popped '{popped}' from index 1: {colors}")

# Remove last element
last = colors.pop()
print(f"Popped last element '{last}': {colors}")

# Delete an element by index
del colors[0]
print(f"After deleting first element: {colors}")

# Clear the list
colors.clear()
print(f"After clearing: {colors}")

# ----------------------------------------------------------------------------
# 5. List Operations
# ----------------------------------------------------------------------------

print("\nLIST OPERATIONS:")

list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Concatenation
combined = list1 + list2
print(f"Concatenated: {combined}")

# Repetition
repeated = list1 * 3
print(f"Repeated: {repeated}")

# Membership (in operator)
print(f"Is 3 in list1? {3 in list1}")
print(f"Is 7 in list1? {7 in list1}")

# List comparison
list3 = [1, 2, 3]
print(f"Is list1 equal to list3? {list1 == list3}")
print(f"Is list1 equal to list2? {list1 == list2}")

# ----------------------------------------------------------------------------
# SUMMARY:
# - Lists store ordered collections of items and can be modified
# - Elements can be accessed by index, starting from 0
# - Negative indices count from the end of the list
# - Slicing creates sublists with [start:end:step] syntax
# - Lists can be modified using various methods like append, insert, remove, pop
# ============================================================================ 