# ============================================================================
# FILENAME: 03_dictionary_comprehensions.py
# DESCRIPTION: Demonstrating dictionary comprehensions for concise dictionary creation
# ============================================================================

# ----------------------------------------------------------------------------
# 1. Basic Dictionary Comprehension
# ----------------------------------------------------------------------------

# Create a dictionary of squares (number: square) for numbers 1-10
squares = {x: x**2 for x in range(1, 11)}
print("Dictionary of squares:", squares)

# Create a dictionary of cubes
cubes = {x: x**3 for x in range(1, 6)}
print("Dictionary of cubes:", cubes)

# ----------------------------------------------------------------------------
# 2. Dictionary Comprehension with Conditional Filtering
# ----------------------------------------------------------------------------

# Create a dictionary of even number squares
even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print("\nEven number squares:", even_squares)

# Create a dictionary of numbers divisible by 3 and their squares
div_by_3 = {x: x**2 for x in range(1, 31) if x % 3 == 0}
print("Numbers divisible by 3 and their squares:", div_by_3)

# Filter both keys and values
filtered_items = {x: x**2 for x in range(1, 11) if x % 2 == 0 and x**2 > 20}
print("Even numbers with squares > 20:", filtered_items)

# ----------------------------------------------------------------------------
# 3. Dictionary Comprehension from Existing Dictionary
# ----------------------------------------------------------------------------

prices = {"apple": 0.99, "banana": 0.59, "orange": 0.79, "mango": 1.29, "grape": 2.49}

# Create new dictionary with prices in euros (converting from dollars)
exchange_rate = 0.85
euro_prices = {fruit: round(price * exchange_rate, 2) for fruit, price in prices.items()}
print("\nPrices in Euros:", euro_prices)

# Filter items by price
expensive_fruits = {fruit: price for fruit, price in prices.items() if price > 1.00}
print("Expensive fruits (>$1.00):", expensive_fruits)

# Transform keys to uppercase
uppercase_prices = {fruit.upper(): price for fruit, price in prices.items()}
print("Prices with uppercase fruit names:", uppercase_prices)

# ----------------------------------------------------------------------------
# 4. Dictionary Comprehension from Two Iterables
# ----------------------------------------------------------------------------

fruits = ["apple", "banana", "cherry", "date"]
counts = [10, 20, 15, 25]

# Create dictionary from two lists
fruit_inventory = {fruit: count for fruit, count in zip(fruits, counts)}
print("\nFruit inventory from lists:", fruit_inventory)

# With conditional filtering
filtered_inventory = {fruit: count for fruit, count in zip(fruits, counts) if count > 15}
print("Filtered inventory (count > 15):", filtered_inventory)

# Create dictionary with complex expressions
discounted_inventory = {fruit: (count, count * 0.9) for fruit, count in zip(fruits, counts)}
print("Inventory with discounted counts:", discounted_inventory)

# ----------------------------------------------------------------------------
# 5. Nested Dictionary Comprehension
# ----------------------------------------------------------------------------

# Create a multiplication table dictionary
table_size = a = 5
multiplication_table = {i: {j: i*j for j in range(1, table_size+1)} for i in range(1, table_size+1)}
print("\nMultiplication table dictionary:")
for i, row in multiplication_table.items():
    print(f"{i}: {row}")

# Create a nested dictionary of character positions in words
words = ["hello", "world", "python"]
char_positions = {word: {char: pos for pos, char in enumerate(word)} for word in words}
print("\nCharacter positions in words:")
for word, positions in char_positions.items():
    print(f"{word}: {positions}")

# ----------------------------------------------------------------------------
# 6. Real-world Examples
# ----------------------------------------------------------------------------

# Data processing example: Calculate temperatures in Celsius from Fahrenheit
fahrenheit_temps = {"New York": 75, "Los Angeles": 82, "Chicago": 68, "Houston": 90}
celsius_temps = {city: round((temp - 32) * 5/9, 1) for city, temp in fahrenheit_temps.items()}
print("\nTemperatures in Celsius:", celsius_temps)

# Data transformation example: Convert student grades
student_grades = {"Alice": 92, "Bob": 85, "Charlie": 78, "David": 96, "Eve": 64}
letter_grades = {
    student: "A" if grade >= 90 else
             "B" if grade >= 80 else
             "C" if grade >= 70 else
             "D" if grade >= 60 else "F"
    for student, grade in student_grades.items()
}
print("Student letter grades:", letter_grades)

# ----------------------------------------------------------------------------
# SUMMARY:
# - Dictionary comprehensions provide a concise way to create dictionaries
# - Basic syntax: {key_expr: value_expr for item in iterable}
# - Conditional syntax: {key_expr: value_expr for item in iterable if condition}
# - Can create dictionaries from other dictionaries, lists, or multiple iterables
# - Supports nested dictionary comprehensions for complex structures
# - Especially useful for data processing and transformation
# ============================================================================ 