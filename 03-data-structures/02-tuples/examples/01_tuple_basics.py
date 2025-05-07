# ============================================================================
# FILENAME: 01_tuple_basics.py
# DESCRIPTION: Demonstrating tuple creation, access, and properties
# ============================================================================

# ----------------------------------------------------------------------------
# 1. Creating Tuples
# ----------------------------------------------------------------------------

# Creating a tuple with parentheses
coordinates = (10, 20)
print("Coordinates:", coordinates)

# Tuple with mixed data types
person = ("Alice", 30, "Engineer", True)
print("Person info:", person)

# Creating a tuple without parentheses (using comma separation)
days = "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"
print("Weekdays:", days)

# Single element tuple (note the comma)
single_item = (42,)  # Without comma, it would be an integer
print("Single item tuple:", single_item)
print("Type:", type(single_item))
print("Not a tuple:", type((42)))  # This is just an integer in parentheses

# Empty tuple
empty_tuple = ()
print("Empty tuple:", empty_tuple)

# Creating tuples from other iterables
tuple_from_list = tuple([1, 2, 3, 4, 5])
print("Tuple from list:", tuple_from_list)

tuple_from_string = tuple("Python")
print("Tuple from string:", tuple_from_string)

tuple_from_range = tuple(range(5))
print("Tuple from range:", tuple_from_range)

# Nested tuples
nested_tuple = (1, 2, ("a", "b"), [3, 4])
print("Nested tuple:", nested_tuple)

print()

# ----------------------------------------------------------------------------
# 2. Accessing Tuple Elements
# ----------------------------------------------------------------------------

# Accessing elements using indices (0-based)
print("First element of coordinates:", coordinates[0])
print("Second element of coordinates:", coordinates[1])

# Accessing elements from the end using negative indices
print("Last element of person:", person[-1])
print("Second-to-last element of person:", person[-2])

# Slicing tuples [start:stop:step]
numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print("\nOriginal numbers tuple:", numbers)

# Basic slicing
print("First three elements:", numbers[:3])  # From start to index 3 (exclusive)
print("Elements from index 4 onwards:", numbers[4:])  # From index 4 to end
print("Elements from index 2 to 6:", numbers[2:7])  # From index 2 to 7 (exclusive)

# Slicing with step
print("Every second element:", numbers[::2])  # Step of 2
print("Every third element, starting from index 1:", numbers[1::3])

# Negative step (reverse)
print("Elements in reverse:", numbers[::-1])
print("Every second element in reverse:", numbers[::-2])

# Accessing nested tuple elements
print("\nThird element of nested_tuple:", nested_tuple[2])
print("First element of the nested tuple within nested_tuple:", nested_tuple[2][0])

print()

# ----------------------------------------------------------------------------
# 3. Tuple Immutability
# ----------------------------------------------------------------------------

print("Demonstrating tuple immutability:")

# Trying to modify a tuple
try:
    coordinates[0] = 100  # This will raise a TypeError
except TypeError as e:
    print(f"Error when trying to modify tuple: {e}")

# Tuples containing mutable objects
mixed_tuple = (1, 2, [3, 4])
print("\nOriginal mixed tuple:", mixed_tuple)

# The list inside the tuple can be modified
mixed_tuple[2][0] = 30
mixed_tuple[2][1] = 40
print("After modifying the list inside the tuple:", mixed_tuple)
print("The tuple itself hasn't changed, only the mutable object it references")

print()

# ----------------------------------------------------------------------------
# 4. Tuple Operations
# ----------------------------------------------------------------------------

# Concatenation
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined = tuple1 + tuple2
print("Concatenation result:", combined)

# Repetition
repeated = tuple1 * 3
print("Repetition result:", repeated)

# Checking membership
print("\nIs 3 in tuple1?", 3 in tuple1)
print("Is 7 in tuple1?", 7 in tuple1)

# Finding the length of a tuple
print("Length of tuple1:", len(tuple1))

# Finding min and max values
numeric_tuple = (5, 2, 8, 1, 9)
print("\nNumeric tuple:", numeric_tuple)
print("Minimum value:", min(numeric_tuple))
print("Maximum value:", max(numeric_tuple))

# Sum of tuple elements
print("Sum of elements:", sum(numeric_tuple))

# Count occurrences of an element
repeated_elements = (1, 2, 3, 1, 4, 1, 5)
print("\nRepeated elements tuple:", repeated_elements)
print("Count of 1:", repeated_elements.count(1))

# Find the index of an element (first occurrence)
print("Index of 4:", repeated_elements.index(4))

# Comparing tuples
tuple_a = (1, 2, 3)
tuple_b = (1, 2, 4)
tuple_c = (1, 2, 3)

print("\nComparing tuples:")
print("tuple_a == tuple_c:", tuple_a == tuple_c)  # True - same elements
print("tuple_a == tuple_b:", tuple_a == tuple_b)  # False - different elements
print("tuple_a < tuple_b:", tuple_a < tuple_b)    # True - compared lexicographically

# Sorting tuples
jumbled = (5, 2, 8, 1, 9)
print("\nJumbled tuple:", jumbled)
print("Sorted tuple (creates a new list):", sorted(jumbled))

# ----------------------------------------------------------------------------
# SUMMARY:
# - Tuples are immutable ordered sequences of elements
# - Created using parentheses () or comma separation
# - Accessed using zero-based indexing and slicing
# - Support operations like concatenation, repetition, and membership testing
# - Common methods include count() and index()
# - Cannot be modified after creation, but mutable elements within can change
# - Often used for representing fixed collections or multiple return values
# ============================================================================ 