# ============================================================================
# FILENAME: 02_advanced_for_loop.py
# DESCRIPTION: Demonstrates advanced techniques with for loops in Python
# ============================================================================

# ----------------------------------------------------------------------------
# 1. Using enumerate() to Get Index and Value
# ----------------------------------------------------------------------------

print("USING ENUMERATE:")

fruits = ["apple", "banana", "cherry", "orange", "kiwi"]

# Basic enumeration
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

# Enumeration with a custom start index
print("\nCustom start index:")
for index, fruit in enumerate(fruits, start=1):
    print(f"Item #{index}: {fruit}")

# ----------------------------------------------------------------------------
# 2. Using zip() to Iterate Multiple Sequences
# ----------------------------------------------------------------------------

print("\nUSING ZIP:")

names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["New York", "Boston", "Chicago"]

# Zip two lists together
print("\nZipping names and ages:")
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

# Zip three lists together
print("\nZipping names, ages, and cities:")
for name, age, city in zip(names, ages, cities):
    print(f"{name} is {age} years old and lives in {city}")

# What happens with uneven lists
print("\nUneven lists:")
names_extra = ["Alice", "Bob", "Charlie", "David", "Eve"]
ages_extra = [25, 30, 35]
for name, age in zip(names_extra, ages_extra):
    print(f"{name} is {age} years old")  # Only processes the first 3 items

# Using zip_longest from itertools
from itertools import zip_longest
print("\nUsing zip_longest:")
for name, age in zip_longest(names_extra, ages_extra, fillvalue="Unknown"):
    print(f"{name} is {age}")

# ----------------------------------------------------------------------------
# 3. Nested For Loops
# ----------------------------------------------------------------------------

print("\nNESTED FOR LOOPS:")

# Basic nested loop - Multiplication table
print("\nMultiplication table (1-5):")
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} × {j} = {i * j}", end="\t")
    print()  # New line after each row

# Nested loops with list comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("\nIterating through a matrix:")
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()

# Flatten a nested list
print("\nFlattening a nested list:")
flattened = [element for row in matrix for element in row]
print(f"Flattened: {flattened}")

# ----------------------------------------------------------------------------
# 4. For Loops with break and continue
# ----------------------------------------------------------------------------

print("\nFOR LOOPS WITH BREAK AND CONTINUE:")

# Using break to exit the loop
print("\nUsing break:")
for i in range(1, 10):
    if i == 5:
        print(f"Found {i}! Breaking the loop.")
        break
    print(f"Current number: {i}")

# Using continue to skip iterations
print("\nUsing continue:")
for i in range(1, 10):
    if i % 2 == 0:
        print(f"Skipping even number {i}")
        continue
    print(f"Processing odd number: {i}")

# ----------------------------------------------------------------------------
# 5. For Loop Patterns
# ----------------------------------------------------------------------------

print("\nFOR LOOP PATTERNS:")

# Find the first matching item
print("\nFinding first match:")
numbers = [10, 25, 3, 45, 2, 9, 18, 5]
first_under_10 = None
for num in numbers:
    if num < 10:
        first_under_10 = num
        break
print(f"First number under 10: {first_under_10}")

# Filtering items into a new list
print("\nFiltering items:")
even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
print(f"Even numbers: {even_numbers}")

# The same with list comprehension
even_numbers_comp = [num for num in numbers if num % 2 == 0]
print(f"Even numbers (list comprehension): {even_numbers_comp}")

# Transforming items
print("\nTransforming items:")
squared = []
for num in numbers:
    squared.append(num ** 2)
print(f"Squared: {squared}")

# The same with list comprehension
squared_comp = [num ** 2 for num in numbers]
print(f"Squared (list comprehension): {squared_comp}")

# ----------------------------------------------------------------------------
# 6. Iterating with Itertools
# ----------------------------------------------------------------------------

print("\nITERATING WITH ITERTOOLS:")
import itertools

# Count indefinitely (with limit for demonstration)
print("\nitertools.count():")
for i in itertools.islice(itertools.count(1), 5):
    print(i)

# Cycle through items indefinitely
print("\nitertools.cycle():")
colors = ["red", "green", "blue"]
count = 0
for color in itertools.cycle(colors):
    if count >= 6:
        break
    print(color)
    count += 1

# Chain multiple iterables together
print("\nitertools.chain():")
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
for num in itertools.chain(numbers1, numbers2):
    print(num)

# Generate permutations
print("\nitertools.permutations():")
for p in itertools.permutations('ABC', 2):
    print(''.join(p))

# Generate combinations
print("\nitertools.combinations():")
for c in itertools.combinations('ABCD', 2):
    print(''.join(c))

# ----------------------------------------------------------------------------
# 7. Dictionary Comprehensions with For Loops
# ----------------------------------------------------------------------------

print("\nDICTIONARY COMPREHENSIONS:")

# Create dictionary of squares
numbers = range(1, 6)
squares_dict = {num: num**2 for num in numbers}
print(f"Squares dictionary: {squares_dict}")

# Create dictionary from two lists
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
name_to_age = {name: age for name, age in zip(names, ages)}
print(f"Name to age dictionary: {name_to_age}")

# Filter items in a dictionary comprehension
original_dict = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
filtered_dict = {k: v for k, v in original_dict.items() if v > 2}
print(f"Filtered dictionary: {filtered_dict}")

# Swap keys and values
swapped_dict = {v: k for k, v in original_dict.items()}
print(f"Swapped dictionary: {swapped_dict}")

# ----------------------------------------------------------------------------
# 8. Iterating Through Files with For Loops
# ----------------------------------------------------------------------------

print("\nITERATING THROUGH FILES:")

# Create a sample file for demonstration
with open("sample.txt", "w") as f:
    f.write("Line 1: Hello, world!\n")
    f.write("Line 2: Python for loops are powerful.\n")
    f.write("Line 3: Iteration is a key concept in programming.\n")
    f.write("Line 4: Files can be read line by line.\n")

# Read file line by line
print("\nReading file line by line:")
with open("sample.txt", "r") as f:
    for line in f:
        print(line.strip())  # strip() removes the trailing newline

# Read file and enumerate lines
print("\nEnumerating file lines:")
with open("sample.txt", "r") as f:
    for i, line in enumerate(f, 1):
        print(f"Line {i}: {line.strip()}")

# Clean up the sample file
import os
os.remove("sample.txt")

# ----------------------------------------------------------------------------
# SUMMARY:
# - enumerate() provides both index and value during iteration
# - zip() allows iterating over multiple sequences at once
# - zip_longest() handles sequences of different lengths
# - Nested loops allow multi-dimensional iteration
# - break and continue provide loop flow control
# - Comprehensions offer concise ways to create collections with loops
# - itertools provides powerful iteration utilities
# - For loops can efficiently process file contents line by line
# ============================================================================ 