# ============================================================================
# FILENAME: 01_set_basics.py
# DESCRIPTION: Demonstrating set creation, modification, and properties
# ============================================================================

# ----------------------------------------------------------------------------
# 1. Creating Sets
# ----------------------------------------------------------------------------

# Creating a set with curly braces
fruits = {"apple", "banana", "orange"}
print("Fruits set:", fruits)

# Creating a set with mixed data types
mixed_set = {42, "hello", True, 3.14}
print("Mixed data types set:", mixed_set)

# Creating an empty set (cannot use {}, as that creates an empty dictionary)
empty_set = set()
print("Empty set:", empty_set)
print("Type of empty_set:", type(empty_set))
print("Type of {}: ", type({}))  # This is a dictionary, not a set

# Creating sets from other iterables
set_from_list = set([1, 2, 3, 4, 5])
print("Set from list:", set_from_list)

set_from_string = set("hello")  # Each character becomes an element
print("Set from string:", set_from_string)  # Note: order is not preserved

set_from_tuple = set((1, 2, 3, 2, 1))  # Duplicates are removed
print("Set from tuple:", set_from_tuple)

print()

# ----------------------------------------------------------------------------
# 2. Set Characteristics
# ----------------------------------------------------------------------------

# 1. Sets are unordered
colors = {"red", "green", "blue"}
print("Set of colors:", colors)
print("Order may change each time you run the program")

# 2. Sets contain unique elements (duplicates are automatically removed)
numbers_with_duplicates = {1, 2, 3, 2, 1, 4, 5, 4}
print("\nSet with duplicates:", numbers_with_duplicates)
print("Duplicates are automatically removed")

# 3. Sets are mutable (can be changed)
fruits = {"apple", "banana", "orange"}
print("\nOriginal fruits set:", fruits)

# 4. Set elements must be immutable (hashable)
# This works:
valid_set = {1, 2, "hello", (1, 2, 3)}
print("\nValid set with immutable elements:", valid_set)

# This would cause an error (lists are mutable):
try:
    invalid_set = {1, 2, [3, 4]}  # TypeError: unhashable type: 'list'
except TypeError as e:
    print(f"\nError when creating a set with mutable elements: {e}")

print()

# ----------------------------------------------------------------------------
# 3. Basic Set Operations
# ----------------------------------------------------------------------------

# Create a sample set
numbers = {1, 2, 3, 4, 5}
print("Numbers set:", numbers)

# Add an element
numbers.add(6)
print("After adding 6:", numbers)

# Add an element that already exists (has no effect)
numbers.add(5)
print("After adding 5 again:", numbers)

# Remove an element
numbers.remove(3)
print("After removing 3:", numbers)

# Remove an element that doesn't exist
try:
    numbers.remove(10)  # This will raise a KeyError
except KeyError as e:
    print(f"Error when removing non-existent element: {e}")

# Alternative: discard() - removes if present, does nothing if not
numbers.discard(4)
print("After discarding 4:", numbers)
numbers.discard(10)  # No error
print("After discarding non-existent 10:", numbers)

# Pop - removes and returns an arbitrary element
popped = numbers.pop()
print(f"Popped element: {popped}")
print("After pop:", numbers)

# Clear - removes all elements
numbers.clear()
print("After clear:", numbers)

# Update - add elements from another iterable
numbers = {1, 2, 3}
numbers.update([3, 4, 5])
print("\nAfter update with [3, 4, 5]:", numbers)

# Update with multiple iterables
numbers.update([6, 7], {8, 9})
print("After update with multiple iterables:", numbers)

print()

# ----------------------------------------------------------------------------
# 4. Membership Testing
# ----------------------------------------------------------------------------

fruits = {"apple", "banana", "orange", "mango"}
print("Fruits set:", fruits)

print("Is 'apple' in fruits?", "apple" in fruits)
print("Is 'pear' in fruits?", "pear" in fruits)
print("Is 'pear' not in fruits?", "pear" not in fruits)

print()

# ----------------------------------------------------------------------------
# 5. Set Size and Iteration
# ----------------------------------------------------------------------------

colors = {"red", "green", "blue", "yellow", "purple"}
print("Colors set:", colors)
print("Number of colors:", len(colors))

print("\nIterating through the set:")
for color in colors:
    print(f"- {color}")

# Sort the set elements during iteration
print("\nIterating through the set in sorted order:")
for color in sorted(colors):
    print(f"- {color}")

print()

# ----------------------------------------------------------------------------
# 6. Set Comprehensions
# ----------------------------------------------------------------------------

# Create a set of squares of numbers from 1 to 5
squares = {x**2 for x in range(1, 6)}
print("Set of squares:", squares)

# Create a set of even numbers from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = {x for x in numbers if x % 2 == 0}
print("Set of even numbers:", even_numbers)

# Create a set of uppercase characters from a string
word = "hello"
uppercase_chars = {char.upper() for char in word}
print("Set of uppercase characters:", uppercase_chars)

# ----------------------------------------------------------------------------
# SUMMARY:
# - Sets are unordered collections of unique immutable objects
# - Created using curly braces {} or the set() constructor
# - Cannot contain mutable objects like lists or dictionaries
# - Automatically eliminate duplicates
# - Provide fast membership testing (is element in set?)
# - Common operations: add, remove, discard, update, pop, clear
# - Can be iterated through, but order is not guaranteed
# - Set comprehensions provide a concise way to create sets
# ============================================================================ 