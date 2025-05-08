# ============================================================================
# FILENAME: 02_lambda_functions.py
# DESCRIPTION: Demonstrates lambda functions (anonymous functions) in Python
# ============================================================================

# ----------------------------------------------------------------------------
# 1. Basic Lambda Function Syntax
# ----------------------------------------------------------------------------

# A lambda function is a small anonymous function defined with the lambda keyword
# Syntax: lambda arguments: expression

# Regular function vs Lambda function
def square(x):
    return x * x

# Equivalent lambda function
square_lambda = lambda x: x * x

# Using both functions
print(f"Regular function: {square(5)}")  # Output: 25
print(f"Lambda function: {square_lambda(5)}")  # Output: 25

# Multiple arguments in a lambda function
add = lambda x, y: x + y
print(f"Adding 3 and 4: {add(3, 4)}")  # Output: 7

# No arguments
say_hello = lambda: "Hello, World!"
print(say_hello())  # Output: Hello, World!

# ----------------------------------------------------------------------------
# 2. Lambda Functions with Built-in Functions
# ----------------------------------------------------------------------------

# Lambda functions are often used with built-in functions like sorted(), filter(), map()

# sorted() with lambda - sort a list of tuples by the second element
people = [('Alice', 25), ('Bob', 20), ('Charlie', 30), ('David', 22)]
sorted_by_age = sorted(people, key=lambda person: person[1])
print("People sorted by age:", sorted_by_age)

# filter() with lambda - filter numbers greater than 10
numbers = [5, 15, 3, 20, 8, 12, 7, 18]
filtered_numbers = list(filter(lambda x: x > 10, numbers))
print("Numbers greater than 10:", filtered_numbers)  # Output: [15, 20, 12, 18]

# map() with lambda - multiply each number by 2
doubled_numbers = list(map(lambda x: x * 2, numbers))
print("Numbers doubled:", doubled_numbers)  # Output: [10, 30, 6, 40, 16, 24, 14, 36]

# ----------------------------------------------------------------------------
# 3. Using Lambda Functions in List Comprehensions (Alternative)
# ----------------------------------------------------------------------------

# While you typically wouldn't use lambda inside a list comprehension,
# it's good to know both approaches

# Using map with lambda
cubes_lambda = list(map(lambda x: x**3, range(1, 6)))
print("Cubes using map/lambda:", cubes_lambda)  # Output: [1, 8, 27, 64, 125]

# Equivalent list comprehension (generally preferred)
cubes_comprehension = [x**3 for x in range(1, 6)]
print("Cubes using list comprehension:", cubes_comprehension)  # Output: [1, 8, 27, 64, 125]

# Using filter with lambda
even_lambda = list(filter(lambda x: x % 2 == 0, range(10)))
print("Even numbers using filter/lambda:", even_lambda)  # Output: [0, 2, 4, 6, 8]

# Equivalent list comprehension (generally preferred)
even_comprehension = [x for x in range(10) if x % 2 == 0]
print("Even numbers using list comprehension:", even_comprehension)  # Output: [0, 2, 4, 6, 8]

# ----------------------------------------------------------------------------
# 4. Practical Examples of Lambda Functions
# ----------------------------------------------------------------------------

# Example 1: Sort a dictionary by value
scores = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'David': 95}
sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
print("Scores sorted by value (highest first):", sorted_scores)

# Example 2: Custom sorting - sort strings by their length
words = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig']
sorted_by_length = sorted(words, key=lambda word: len(word))
print("Words sorted by length:", sorted_by_length)

# Example 3: Sort a list of dictionaries
students = [
    {'name': 'Alice', 'grade': 'A', 'age': 22},
    {'name': 'Bob', 'grade': 'B', 'age': 20},
    {'name': 'Charlie', 'grade': 'A', 'age': 25}
]
# Sort by age
sorted_by_age = sorted(students, key=lambda student: student['age'])
print("Students sorted by age:", sorted_by_age)

# Sort by grade, then by age
sorted_by_grade_and_age = sorted(students, key=lambda student: (student['grade'], student['age']))
print("Students sorted by grade, then age:", sorted_by_grade_and_age)

# Example 4: Apply multiple operations with map and lambda
numbers = [1, 2, 3, 4, 5]
# Square each number and then add 10
results = list(map(lambda x: x**2 + 10, numbers))
print("Numbers squared then added 10:", results)  # Output: [11, 14, 19, 26, 35]

# ----------------------------------------------------------------------------
# 5. Lambda Functions in Functional Programming
# ----------------------------------------------------------------------------

# Combining multiple operations with functional programming style
from functools import reduce

# Calculate the sum of squares of even numbers in a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = reduce(
    lambda x, y: x + y,  # Sum operation
    map(lambda x: x**2,  # Square operation
        filter(lambda x: x % 2 == 0, numbers))  # Filter for even numbers
)
print("Sum of squares of even numbers:", result)  # Output: 220 (4+16+36+64+100)

# The same operation using list comprehension (often more readable)
result_comprehension = sum(x**2 for x in numbers if x % 2 == 0)
print("Same result using comprehension:", result_comprehension)  # Output: 220

# ----------------------------------------------------------------------------
# 6. When to Use Lambda Functions
# ----------------------------------------------------------------------------

# Lambda functions are best for simple, one-time use functions
# Good uses:

# 1. As an argument to higher-order functions
numbers = [4, 2, 7, 5, 1, 3]
sorted_numbers = sorted(numbers, key=lambda x: abs(x - 5))
print("Numbers sorted by distance from 5:", sorted_numbers)  # Output: [5, 4, 7, 3, 2, 1]

# 2. For simple data transformations
data = [{'value': 10}, {'value': 20}, {'value': 30}]
values = list(map(lambda item: item['value'], data))
print("Extracted values:", values)  # Output: [10, 20, 30]

# 3. For quick callbacks
# (simulating a button click handler in a GUI application)
def button_clicked(callback):
    # Simulating a button click
    value = 42
    # Call the provided callback
    result = callback(value)
    print(f"Button clicked! Callback returned: {result}")

# Using a lambda as a callback
button_clicked(lambda x: f"Processed value: {x * 2}")

# ----------------------------------------------------------------------------
# 7. Limitations of Lambda Functions
# ----------------------------------------------------------------------------

# Lambda functions are restricted to a single expression
# They cannot contain multiple statements or annotations

# This works
add_and_double = lambda x, y: (x + y) * 2
print(f"Add and double: {add_and_double(3, 4)}")  # Output: 14

# For more complex operations, use regular functions
def complex_operation(x, y):
    # Multiple statements
    temp = x + y
    result = temp * 2
    return result

# Print function information (more difficult with lambdas)
print(f"Function name: {complex_operation.__name__}")
print(f"Lambda's generic name: {add_and_double.__name__}")

# ----------------------------------------------------------------------------
# SUMMARY:
# - Lambda functions are small anonymous functions created with the lambda keyword
# - They can take any number of arguments but can only have one expression
# - They are most useful in combination with higher-order functions like map(), filter(), and sorted()
# - They're ideal for simple, one-time use functions
# - For more complex functions, regular function definitions are more appropriate and readable
# ============================================================================ 