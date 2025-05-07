# ============================================================================
# FILENAME: 02_tuple_unpacking.py
# DESCRIPTION: Demonstrating tuple unpacking and multiple assignments
# ============================================================================

# ----------------------------------------------------------------------------
# 1. Basic Tuple Unpacking
# ----------------------------------------------------------------------------

# Create a tuple
person = ("Alice", 30, "Engineer")

# Unpack the tuple into variables
name, age, occupation = person

print("Person tuple:", person)
print("Unpacked values:")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Occupation: {occupation}")

print()

# ----------------------------------------------------------------------------
# 2. Swapping Variables with Tuple Unpacking
# ----------------------------------------------------------------------------

a = 5
b = 10

print(f"Before swapping: a = {a}, b = {b}")

# Swap values using tuple unpacking
a, b = b, a

print(f"After swapping: a = {a}, b = {b}")

print()

# ----------------------------------------------------------------------------
# 3. Ignoring Values with _ (underscore)
# ----------------------------------------------------------------------------

# Create a tuple with unnecessary values
data = ("Alice", 30, "123-456-7890", "alice@example.com")

# Only unpack the values we need, ignoring others with _
name, age, _, email = data

print("Data tuple:", data)
print(f"Only unpacked name: {name}, age: {age}, and email: {email}")

print()

# ----------------------------------------------------------------------------
# 4. Extended Unpacking with * (star operator)
# ----------------------------------------------------------------------------

# Create a longer sequence
numbers = (1, 2, 3, 4, 5, 6)

# Unpack first, last, and middle elements
first, *middle, last = numbers

print("Numbers tuple:", numbers)
print(f"First: {first}")
print(f"Middle values: {middle}")  # This becomes a list
print(f"Last: {last}")

# Only unpacking first and rest
first, *rest = numbers
print(f"First: {first}")
print(f"Rest of values: {rest}")

# Only unpacking the rest and last
*rest, last = numbers
print(f"Rest of values: {rest}")
print(f"Last: {last}")

print()

# ----------------------------------------------------------------------------
# 5. Nested Tuple Unpacking
# ----------------------------------------------------------------------------

# Nested tuple
person_details = ("Alice", ("New York", "USA"), (123, 456, 789))

# Unpack into variables including nested unpacking
name, (city, country), (id_num, passport_num, _) = person_details

print("Nested tuple:", person_details)
print(f"Name: {name}")
print(f"Location: {city}, {country}")
print(f"ID: {id_num}, Passport: {passport_num}")

print()

# ----------------------------------------------------------------------------
# 6. Return Multiple Values from Functions
# ----------------------------------------------------------------------------

def get_person_details():
    """Return multiple values as a tuple"""
    name = "Bob"
    age = 25
    occupation = "Developer"
    return name, age, occupation  # Implicitly returns a tuple

# Call function and unpack the returned tuple
person_name, person_age, person_job = get_person_details()

print("Values returned from function:")
print(f"Name: {person_name}")
print(f"Age: {person_age}")
print(f"Job: {person_job}")

# Alternative: capture the tuple first, then unpack
result = get_person_details()
print("\nReturned tuple:", result)
print("Type of returned value:", type(result))

def get_statistics(numbers):
    """Return multiple statistics about a sequence of numbers"""
    total = sum(numbers)
    average = total / len(numbers)
    minimum = min(numbers)
    maximum = max(numbers)
    return minimum, maximum, average, total

# Using a list of numbers
data_points = [4, 7, 2, 9, 5, 3, 8, 1, 6]

# Unpack returned tuple directly
min_val, max_val, avg_val, sum_val = get_statistics(data_points)

print("\nData points:", data_points)
print(f"Minimum: {min_val}")
print(f"Maximum: {max_val}")
print(f"Average: {avg_val:.2f}")
print(f"Sum: {sum_val}")

print()

# ----------------------------------------------------------------------------
# 7. Unpacking for Multiple Loop Variables
# ----------------------------------------------------------------------------

# List of coordinates
coordinates = [(1, 2), (3, 4), (5, 6), (7, 8)]

print("List of coordinate tuples:", coordinates)
print("Unpacking in a loop:")

# Unpacking in a for loop
for x, y in coordinates:
    print(f"x: {x}, y: {y}")

# List of student data
students = [
    ("Alice", 21, "Computer Science"),
    ("Bob", 19, "Engineering"),
    ("Charlie", 20, "Mathematics")
]

print("\nStudent data:")
for name, age, major in students:
    print(f"{name} is {age} years old, majoring in {major}")

# Dictionary items() returns tuples of (key, value)
person_info = {
    "name": "Dave",
    "age": 35,
    "country": "Canada",
    "language": "Python"
}

print("\nDictionary items unpacking:")
for key, value in person_info.items():
    print(f"{key}: {value}")

# ----------------------------------------------------------------------------
# SUMMARY:
# - Tuple unpacking assigns elements of a tuple to multiple variables
# - It's a clean and readable way to handle multiple return values
# - The _ convention helps ignore values you don't need
# - Extended unpacking with * collects multiple elements into a list
# - Unpacking works with nested data structures
# - Functions implicitly return tuples when returning multiple values
# - Unpacking is commonly used in loops to process paired data
# ============================================================================ 