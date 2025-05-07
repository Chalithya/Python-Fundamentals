# ============================================================================
# FILENAME: 03_range_function.py
# DESCRIPTION: Demonstrates the range function in Python for loops
# ============================================================================

# ----------------------------------------------------------------------------
# 1. Basic Range Usage
# ----------------------------------------------------------------------------

print("BASIC RANGE USAGE:")

# range with one argument - creates numbers from 0 to n-1
print("\nrange(5) - Numbers from 0 to 4:")
for i in range(5):
    print(i, end=" ")
print()  # newline

# range with two arguments - creates numbers from start to stop-1
print("\nrange(2, 8) - Numbers from 2 to 7:")
for i in range(2, 8):
    print(i, end=" ")
print()  # newline

# range with three arguments - creates numbers from start to stop-1 with step
print("\nrange(1, 10, 2) - Odd numbers from 1 to 9:")
for i in range(1, 10, 2):
    print(i, end=" ")
print()  # newline

# ----------------------------------------------------------------------------
# 2. Range with Negative Step
# ----------------------------------------------------------------------------

print("\nRANGE WITH NEGATIVE STEP:")

# Counting down
print("\nrange(10, 0, -1) - Countdown from 10 to 1:")
for i in range(10, 0, -1):
    print(i, end=" ")
print()  # newline

# Counting down with larger step
print("\nrange(20, 0, -5) - Counting down by 5:")
for i in range(20, 0, -5):
    print(i, end=" ")
print()  # newline

# ----------------------------------------------------------------------------
# 3. Common Patterns with Range
# ----------------------------------------------------------------------------

print("\nCOMMON PATTERNS WITH RANGE:")

# Iterating over indices of a sequence
fruits = ["apple", "banana", "cherry", "orange", "kiwi"]
print("\nIterating over indices of a list:")
for i in range(len(fruits)):
    print(f"Index {i}: {fruits[i]}")

# Comparing range and enumerate (enumerate is generally preferred)
print("\nUsing range vs. enumerate:")
print("Range method:")
for i in range(len(fruits)):
    print(f"Index {i}: {fruits[i]}")

print("\nEnumerate method (preferred):")
for i, fruit in enumerate(fruits):
    print(f"Index {i}: {fruit}")

# Creating a list of numbers
print("\nCreating a list of numbers with range:")
numbers_list = list(range(1, 11))
print(numbers_list)

# Summing numbers
print("\nSumming numbers with range:")
total = sum(range(1, 101))  # Sum of numbers from 1 to 100
print(f"Sum of numbers 1 to 100: {total}")

# ----------------------------------------------------------------------------
# 4. Using Range Efficiently
# ----------------------------------------------------------------------------

print("\nUSING RANGE EFFICIENTLY:")

# Memory efficiency - range objects don't store all values in memory
print("\nMemory Efficiency:")
large_range = range(1, 1000000)  # This doesn't create a million numbers in memory
print(f"Type: {type(large_range)}")
print(f"First few values: {large_range[0]}, {large_range[1]}, {large_range[2]}")
print(f"Range length: {len(large_range)}")
print(f"Contains 500000?: {500000 in large_range}")  # Membership test is efficient
print(f"Contains 1000001?: {1000001 in large_range}")

# Using range in list comprehensions
print("\nUsing range in list comprehensions:")
squares = [x**2 for x in range(1, 11)]
print(f"Squares of numbers 1 to 10: {squares}")

# Range vs. sequence slicing
numbers = list(range(0, 20))
print("\nOriginal list:", numbers)

print("\nUsing range to iterate over a subset:")
for i in range(5, 15):
    print(numbers[i], end=" ")
print()

print("\nUsing slice notation (more pythonic):")
for num in numbers[5:15]:
    print(num, end=" ")
print()

# ----------------------------------------------------------------------------
# 5. Range Edge Cases and Gotchas
# ----------------------------------------------------------------------------

print("\nRANGE EDGE CASES AND GOTCHAS:")

# Empty ranges
print("\nEmpty ranges:")
empty_range = range(0)
print(f"range(0) length: {len(empty_range)}")
print(f"range(5, 5) length: {len(range(5, 5))}")
print(f"range(10, 0) length: {len(range(10, 0))}")  # Step is positive by default

# Non-integer steps aren't allowed
print("\nRange requires integer arguments:")
try:
    range(0, 10, 0.5)  # This will raise a TypeError
except TypeError as e:
    print(f"Error: {e}")

# Converting float ranges to integers
print("\nWorkaround for non-integer steps:")
start, stop, step = 0, 5, 0.5
float_range = [start + step*i for i in range(int((stop-start)/step))]
print(float_range)

# Starting from specific values
print("\nStarting a range from a specific value:")
start_value = 100
count = 5
custom_range = range(start_value, start_value + count)
print(list(custom_range))

# ----------------------------------------------------------------------------
# 6. Range vs. NumPy Arrays (When Performance Matters)
# ----------------------------------------------------------------------------

print("\nRANGE VS. NUMPY ARRAYS:")
print("(Note: NumPy is a separate library that must be installed)")

# If NumPy is installed, this would demonstrate alternatives
# For high-performance numeric computation, NumPy arrays are often better
# Example (requires NumPy):
"""
import numpy as np
np_range = np.arange(0, 10, 0.5)  # Non-integer steps allowed
print(np_range)
"""

# The basic example works without NumPy
print("Basic example (without NumPy):")
for i in range(10):
    print(i**2, end=" ")
print()

# ----------------------------------------------------------------------------
# SUMMARY:
# - range() is a built-in function that generates a sequence of numbers
# - Common forms: range(stop), range(start, stop), range(start, stop, step) 
# - range objects are memory efficient as they don't store all values
# - range is ideal for traditional counting loops and list indices
# - For simple iteration through items, direct iteration is preferred over range
# - Use enumerate() when you need both index and value (more pythonic)
# - range requires integer arguments; for floating-point steps, other approaches
#   are needed (list comprehension or NumPy if available)
# ============================================================================ 