# ============================================================================
# FILENAME: 03_list_comprehensions.py
# DESCRIPTION: Demonstrates list comprehensions in Python
# ============================================================================

# ----------------------------------------------------------------------------
# 1. Basic List Comprehension
# ----------------------------------------------------------------------------

print("BASIC LIST COMPREHENSIONS:")

# Traditional way using a for loop
squares_traditional = []
for i in range(1, 11):
    squares_traditional.append(i**2)
print(f"Squares (traditional): {squares_traditional}")

# Equivalent list comprehension
squares_comprehension = [i**2 for i in range(1, 11)]
print(f"Squares (comprehension): {squares_comprehension}")

# Compute cube roots
cube_roots = [round(i**(1/3), 2) for i in range(1, 30)]
print(f"Cube roots: {cube_roots}")

# Create a list from another list
original = [10, 20, 30, 40, 50]
doubled = [x * 2 for x in original]
print(f"Original: {original}")
print(f"Doubled: {doubled}")

# ----------------------------------------------------------------------------
# 2. List Comprehensions with Conditionals
# ----------------------------------------------------------------------------

print("\nLIST COMPREHENSIONS WITH CONDITIONALS:")

# Traditional way
even_traditional = []
for i in range(1, 21):
    if i % 2 == 0:
        even_traditional.append(i)
print(f"Even numbers (traditional): {even_traditional}")

# Equivalent list comprehension with conditional
even_comprehension = [i for i in range(1, 21) if i % 2 == 0]
print(f"Even numbers (comprehension): {even_comprehension}")

# Numbers divisible by 3 and 5
divisible_by_3_and_5 = [i for i in range(1, 101) if i % 3 == 0 and i % 5 == 0]
print(f"Numbers divisible by both 3 and 5: {divisible_by_3_and_5}")

# Filter out strings with less than 4 characters
words = ["the", "quick", "brown", "fox", "jumps", "over", "lazy", "dog"]
long_words = [word for word in words if len(word) >= 4]
print(f"Words with 4+ characters: {long_words}")

# ----------------------------------------------------------------------------
# 3. Nested If Conditions in List Comprehensions
# ----------------------------------------------------------------------------

print("\nNESTED IF CONDITIONS:")

# Multiple conditions
numbers = list(range(1, 21))
filtered = [x for x in numbers if x % 2 == 0 if x % 3 == 0]
print(f"Numbers divisible by both 2 and 3: {filtered}")

# This is equivalent to:
filtered_traditional = []
for x in numbers:
    if x % 2 == 0:
        if x % 3 == 0:
            filtered_traditional.append(x)
print(f"Same result with traditional loops: {filtered_traditional}")

# ----------------------------------------------------------------------------
# 4. If-Else in List Comprehensions
# ----------------------------------------------------------------------------

print("\nIF-ELSE IN LIST COMPREHENSIONS:")

# Using if-else (ternary expression)
# This replaces values instead of filtering
result = ["even" if x % 2 == 0 else "odd" for x in range(1, 11)]
print(f"Even/odd labels: {result}")

# Traditional equivalent
traditional_result = []
for x in range(1, 11):
    if x % 2 == 0:
        traditional_result.append("even")
    else:
        traditional_result.append("odd")
print(f"Same result with traditional approach: {traditional_result}")

# Categorize numbers
numbers = list(range(1, 21))
categorized = ["Multiple of 3" if x % 3 == 0 else 
               "Multiple of 2" if x % 2 == 0 else 
               "Other" for x in numbers]
print(f"Numbers: {numbers}")
print(f"Categorized: {categorized}")

# ----------------------------------------------------------------------------
# 5. Nested List Comprehensions
# ----------------------------------------------------------------------------

print("\nNESTED LIST COMPREHENSIONS:")

# Create a matrix (list of lists)
matrix = [[j for j in range(5)] for i in range(3)]
print("Matrix:")
for row in matrix:
    print(row)

# Flatten a matrix with a list comprehension
flattened = [item for row in matrix for item in row]
print(f"Flattened matrix: {flattened}")

# Traditional equivalent of flattening
flattened_traditional = []
for row in matrix:
    for item in row:
        flattened_traditional.append(item)
print(f"Same result with traditional approach: {flattened_traditional}")

# Creating a multiplication table
mult_table = [[i*j for j in range(1, 6)] for i in range(1, 6)]
print("\nMultiplication table:")
for row in mult_table:
    print(row)

# ----------------------------------------------------------------------------
# 6. Practical Applications
# ----------------------------------------------------------------------------

print("\nPRACTICAL APPLICATIONS:")

# Converting Celsius to Fahrenheit
celsius = [0, 10, 20, 30, 40, 50]
fahrenheit = [(9/5) * c + 32 for c in celsius]
print(f"Celsius: {celsius}")
print(f"Fahrenheit: {fahrenheit}")

# Extracting info from objects
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

people = [
    Person("Alice", 25),
    Person("Bob", 30),
    Person("Charlie", 35),
    Person("Diana", 40)
]

# Extract names of people over 30
names_over_30 = [person.name for person in people if person.age > 30]
print(f"People over 30: {names_over_30}")

# Parsing data
data = "1, 2, 3, 4, 5"
parsed = [int(x.strip()) for x in data.split(",")]
print(f"Parsed data: {parsed}")

# ----------------------------------------------------------------------------
# SUMMARY:
# - List comprehensions provide a concise way to create lists
# - They can replace many for loops with a single line of code
# - The basic syntax is [expression for item in iterable]
# - Add conditions with [expression for item in iterable if condition]
# - If-else can be used in the expression part: [X if condition else Y for item in iterable]
# - Nested list comprehensions allow creating complex data structures
# - They improve readability for simple operations but can be hard to read for complex ones
# ============================================================================ 