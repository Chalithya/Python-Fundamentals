# ============================================================================
# FILENAME: 03_map_filter_reduce.py
# DESCRIPTION: Demonstrates map(), filter(), and reduce() functions in Python
# ============================================================================

# Import reduce from functools module
from functools import reduce

# ----------------------------------------------------------------------------
# 1. The map() Function
# ----------------------------------------------------------------------------

# map(function, iterable, ...)
# Applies the function to each item in the iterable and returns an iterator

# Example 1: Convert temperatures from Celsius to Fahrenheit
celsius_temps = [0, 10, 20, 30, 40]

# Using a regular function with map
def celsius_to_fahrenheit(c):
    """Convert Celsius to Fahrenheit"""
    return (c * 9/5) + 32

fahrenheit_temps = list(map(celsius_to_fahrenheit, celsius_temps))
print("Celsius temps:", celsius_temps)
print("Fahrenheit temps (using named function):", fahrenheit_temps)

# Same operation using a lambda function
fahrenheit_temps_lambda = list(map(lambda c: (c * 9/5) + 32, celsius_temps))
print("Fahrenheit temps (using lambda):", fahrenheit_temps_lambda)

# Example 2: Apply a function to multiple iterables
numbers1 = [1, 2, 3, 4]
numbers2 = [5, 6, 7, 8]

# Add corresponding elements from both lists
sums = list(map(lambda x, y: x + y, numbers1, numbers2))
print("Sums of corresponding elements:", sums)  # Output: [6, 8, 10, 12]

# Example 3: Convert strings to their lengths
words = ["apple", "banana", "cherry", "date", "elderberry"]
word_lengths = list(map(len, words))  # Note: len is a built-in function
print("Word lengths:", word_lengths)  # Output: [5, 6, 6, 4, 10]

# ----------------------------------------------------------------------------
# 2. The filter() Function
# ----------------------------------------------------------------------------

# filter(function, iterable)
# Constructs an iterator from elements of iterable for which function returns True

# Example 1: Filter out odd numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using a regular function with filter
def is_even(n):
    """Check if a number is even"""
    return n % 2 == 0

even_numbers = list(filter(is_even, numbers))
print("Even numbers (using named function):", even_numbers)

# Same operation using a lambda function
even_numbers_lambda = list(filter(lambda n: n % 2 == 0, numbers))
print("Even numbers (using lambda):", even_numbers_lambda)

# Example 2: Filter strings by length
words = ["apple", "banana", "cherry", "date", "elderberry", "fig"]
long_words = list(filter(lambda word: len(word) > 5, words))
print("Words with more than 5 characters:", long_words)  # Output: ['banana', 'elderberry']

# Example 3: Filter out None and empty values
mixed_data = [0, 1, "", None, False, True, [], "hello", [1, 2, 3]]
non_empty = list(filter(None, mixed_data))  # None as function filters out "falsy" values
print("Non-empty values:", non_empty)  # Output: [1, True, 'hello', [1, 2, 3]]

# ----------------------------------------------------------------------------
# 3. The reduce() Function
# ----------------------------------------------------------------------------

# reduce(function, iterable[, initializer])
# Apply function cumulatively to the items of iterable, reducing to a single value

# Example 1: Calculate the sum of a list of numbers
numbers = [1, 2, 3, 4, 5]

# Using a regular function with reduce
def add(x, y):
    """Add two numbers"""
    return x + y

sum_result = reduce(add, numbers)
print("Sum of numbers (using named function):", sum_result)  # Output: 15

# Same operation using a lambda function
sum_result_lambda = reduce(lambda x, y: x + y, numbers)
print("Sum of numbers (using lambda):", sum_result_lambda)  # Output: 15

# Example 2: Find the maximum value in a list
max_value = reduce(lambda x, y: x if x > y else y, numbers)
print("Maximum value:", max_value)  # Output: 5

# Example 3: Using an initializer
# Calculate the product of numbers starting with 10 as the initial value
product = reduce(lambda x, y: x * y, numbers, 10)
print("Product with initializer 10:", product)  # Output: 1200 (10*1*2*3*4*5)

# ----------------------------------------------------------------------------
# 4. Combining map(), filter(), and reduce()
# ----------------------------------------------------------------------------

# Let's solve a complex problem by chaining these functions

# Problem: Calculate the sum of squares of even numbers in a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Step 1: Filter the even numbers
even_numbers = filter(lambda x: x % 2 == 0, numbers)

# Step 2: Square each of the even numbers
squared_even_numbers = map(lambda x: x**2, even_numbers)

# Step 3: Calculate the sum of the squared even numbers
sum_of_squares = reduce(lambda x, y: x + y, squared_even_numbers)

print("Sum of squares of even numbers:", sum_of_squares)  # Output: 220 (4+16+36+64+100)

# We can also chain these operations in a single expression
result = reduce(
    lambda x, y: x + y,
    map(lambda x: x**2, 
        filter(lambda x: x % 2 == 0, numbers))
)
print("Same result with chained operations:", result)  # Output: 220

# ----------------------------------------------------------------------------
# 5. Comparison with List Comprehensions
# ----------------------------------------------------------------------------

# List comprehensions often provide a more readable alternative to map and filter

# map alternative
squared_numbers_map = list(map(lambda x: x**2, numbers))
squared_numbers_comp = [x**2 for x in numbers]
print("Squared numbers (map):", squared_numbers_map)
print("Squared numbers (list comprehension):", squared_numbers_comp)

# filter alternative
even_numbers_filter = list(filter(lambda x: x % 2 == 0, numbers))
even_numbers_comp = [x for x in numbers if x % 2 == 0]
print("Even numbers (filter):", even_numbers_filter)
print("Even numbers (list comprehension):", even_numbers_comp)

# Combined map and filter alternative
squared_evens_map_filter = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers)))
squared_evens_comp = [x**2 for x in numbers if x % 2 == 0]
print("Squared even numbers (map & filter):", squared_evens_map_filter)
print("Squared even numbers (list comprehension):", squared_evens_comp)

# reduce alternative for sum
sum_reduce = reduce(lambda x, y: x + y, numbers)
sum_builtin = sum(numbers)
print("Sum (reduce):", sum_reduce)
print("Sum (built-in):", sum_builtin)

# ----------------------------------------------------------------------------
# 6. Performance Considerations
# ----------------------------------------------------------------------------

# Compare the performance of these approaches for a larger dataset
import time

# Generate a list of 1 million numbers
large_numbers = list(range(1000000))

# Time the sum using reduce
start_time = time.time()
reduce_sum = reduce(lambda x, y: x + y, large_numbers)
reduce_time = time.time() - start_time
print(f"Sum using reduce: {reduce_sum} (took {reduce_time:.6f} seconds)")

# Time the sum using the built-in sum function
start_time = time.time()
builtin_sum = sum(large_numbers)
builtin_time = time.time() - start_time
print(f"Sum using built-in: {builtin_sum} (took {builtin_time:.6f} seconds)")

print(f"Built-in sum is {reduce_time/builtin_time:.1f}x faster than reduce")

# ----------------------------------------------------------------------------
# 7. Practical Examples
# ----------------------------------------------------------------------------

# Example 1: Data processing pipeline
people = [
    {"name": "Alice", "age": 25, "salary": 80000},
    {"name": "Bob", "age": 30, "salary": 70000},
    {"name": "Charlie", "age": 35, "salary": 90000},
    {"name": "David", "age": 28, "salary": 65000},
    {"name": "Eve", "age": 22, "salary": 75000}
]

# Find the average salary of people older than 25
total_salary = reduce(
    lambda acc, person: acc + person["salary"],
    filter(lambda person: person["age"] > 25, people),
    0
)
count = len(list(filter(lambda person: person["age"] > 25, people)))
average_salary = total_salary / count if count > 0 else 0

print(f"Average salary of people older than 25: ${average_salary:.2f}")

# Example 2: Flattening a list of lists
nested_lists = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
flattened = reduce(lambda acc, curr: acc + curr, nested_lists, [])
print("Flattened list:", flattened)

# Example 3: Transform and aggregate data
# Calculate the total character count of capitalized words
words = ["apple", "BANANA", "Cherry", "DATE", "elderberry", "FIG"]
total_uppercase_chars = reduce(
    lambda acc, word: acc + len(word),
    filter(lambda word: word.isupper(), words),
    0
)
print("Total characters in uppercase words:", total_uppercase_chars)

# ----------------------------------------------------------------------------
# SUMMARY:
# - map() applies a function to each item in an iterable and returns a map object
# - filter() constructs an iterator from elements for which a function returns True
# - reduce() applies a function cumulatively to the items of an iterable, reducing to a single value
# - These functions are powerful tools for data transformation and functional programming
# - List comprehensions often provide a more readable alternative to map() and filter()
# - Built-in functions like sum() are usually more efficient than equivalent reduce() operations
# ============================================================================ 