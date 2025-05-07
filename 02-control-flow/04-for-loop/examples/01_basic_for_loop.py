# ============================================================================
# FILENAME: 01_basic_for_loop.py
# DESCRIPTION: Demonstrates basic for loop usage in Python
# ============================================================================

# ----------------------------------------------------------------------------
# 1. Iterating Over a List
# ----------------------------------------------------------------------------

print("ITERATING OVER A LIST:")

# A simple list of fruits
fruits = ["apple", "banana", "cherry", "orange", "kiwi"]

# Iterate through each item in the list
for fruit in fruits:
    print(f"I like {fruit}s")

# ----------------------------------------------------------------------------
# 2. Iterating Over a String
# ----------------------------------------------------------------------------

print("\nITERATING OVER A STRING:")

# Iterate through each character in a string
word = "Python"
for letter in word:
    print(letter)

# ----------------------------------------------------------------------------
# 3. Iterating with Range
# ----------------------------------------------------------------------------

print("\nITERATING WITH RANGE:")

# range(stop) - generates numbers from 0 to stop-1
print("\nrange(5):")
for i in range(5):
    print(f"Number: {i}")

# range(start, stop) - generates numbers from start to stop-1
print("\nrange(2, 7):")
for i in range(2, 7):
    print(f"Number: {i}")

# range(start, stop, step) - generates numbers with a specified step
print("\nrange(1, 10, 2):")
for i in range(1, 10, 2):
    print(f"Number: {i}")

# Negative step for counting down
print("\nrange(10, 0, -1):")
for i in range(10, 0, -1):
    print(f"Countdown: {i}")

# ----------------------------------------------------------------------------
# 4. Iterating Over a Tuple
# ----------------------------------------------------------------------------

print("\nITERATING OVER A TUPLE:")

# A tuple of colors
colors = ("red", "green", "blue", "yellow")

for color in colors:
    print(f"Color: {color}")

# ----------------------------------------------------------------------------
# 5. Iterating Over a Dictionary
# ----------------------------------------------------------------------------

print("\nITERATING OVER A DICTIONARY:")

# A simple dictionary
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "job": "Developer"
}

# Iterate through keys (default)
print("\nIterate through keys:")
for key in person:
    print(f"Key: {key}")

# Iterate through values
print("\nIterate through values:")
for value in person.values():
    print(f"Value: {value}")

# Iterate through key-value pairs
print("\nIterate through key-value pairs:")
for key, value in person.items():
    print(f"{key}: {value}")

# ----------------------------------------------------------------------------
# 6. Using For Loops with Conditional Statements
# ----------------------------------------------------------------------------

print("\nFOR LOOPS WITH CONDITIONALS:")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Find even numbers
print("\nEven numbers:")
for num in numbers:
    if num % 2 == 0:
        print(f"{num} is even")

# Find numbers greater than 5
print("\nNumbers greater than 5:")
for num in numbers:
    if num > 5:
        print(f"{num} is greater than 5")

# ----------------------------------------------------------------------------
# 7. Calculating Sums and Other Aggregations
# ----------------------------------------------------------------------------

print("\nCALCULATING SUMS AND AGGREGATIONS:")

# Sum numbers with a for loop
total = 0
for num in numbers:
    total += num
print(f"Sum of numbers: {total}")

# Find the maximum value
max_value = numbers[0]  # Start with the first number
for num in numbers:
    if num > max_value:
        max_value = num
print(f"Maximum value: {max_value}")

# Find the minimum value
min_value = numbers[0]  # Start with the first number
for num in numbers:
    if num < min_value:
        min_value = num
print(f"Minimum value: {min_value}")

# ----------------------------------------------------------------------------
# 8. For Loop with else Clause
# ----------------------------------------------------------------------------

print("\nFOR LOOP WITH ELSE CLAUSE:")

# The else block executes after the loop completes normally
for i in range(1, 4):
    print(f"Loop iteration {i}")
else:
    print("Loop completed successfully!")

# Comparison with a loop that breaks
print("\nLoop with break:")
for i in range(1, 4):
    print(f"Loop iteration {i}")
    if i == 2:
        print("Breaking the loop!")
        break
else:
    print("This won't be printed because the loop was broken")

# ----------------------------------------------------------------------------
# SUMMARY:
# - For loops can iterate over any sequence: lists, strings, tuples, etc.
# - The range() function generates numerical sequences for for loops
# - Dictionary iteration can be done with keys(), values(), or items()
# - Conditions can be used inside for loops to filter or process data
# - The else clause is executed only if the loop completes without a break
# - For loops are the preferred way to iterate when you know the sequence
# ============================================================================ 