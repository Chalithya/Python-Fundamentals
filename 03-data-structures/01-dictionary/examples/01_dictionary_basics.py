# ============================================================================
# FILENAME: 01_dictionary_basics.py
# DESCRIPTION: Demonstrating dictionary creation, access, modification and deletion
# ============================================================================

# ----------------------------------------------------------------------------
# 1. Creating Dictionaries
# ----------------------------------------------------------------------------

# Creating a dictionary with key-value pairs
student = {
    "name": "Alice",
    "age": 21,
    "major": "Computer Science",
    "gpa": 3.8
}
print("Student dictionary:", student)

# Empty dictionary
empty_dict = {}
print("Empty dictionary:", empty_dict)

# Using dict() constructor
contact = dict(name="John", email="john@example.com", phone="555-1234")
print("Contact dictionary:", contact)

# Creating a dictionary from a list of tuples
items = [("apple", 0.99), ("banana", 0.59), ("orange", 0.79)]
prices = dict(items)
print("Prices dictionary:", prices)

# ----------------------------------------------------------------------------
# 2. Accessing Dictionary Values
# ----------------------------------------------------------------------------

# Accessing values using keys
print("\nStudent name:", student["name"])
print("Student age:", student["age"])

# Using get() method (safer - returns None or default if key doesn't exist)
print("Student major:", student.get("major"))
print("Student address:", student.get("address"))  # Key doesn't exist
print("Student address:", student.get("address", "Not provided"))  # With default value

# Checking if a key exists
if "gpa" in student:
    print("GPA is available:", student["gpa"])

# Getting all keys, values, and items
print("\nKeys:", list(student.keys()))
print("Values:", list(student.values()))
print("Items:", list(student.items()))

# ----------------------------------------------------------------------------
# 3. Modifying Dictionaries
# ----------------------------------------------------------------------------

print("\n--- Modifying dictionaries ---")

# Adding new key-value pairs
student["year"] = "Junior"
print("After adding year:", student)

# Updating existing values
student["age"] = 22
print("After updating age:", student)

# Updating multiple values at once
student.update({"age": 23, "gpa": 3.9, "graduation_year": 2024})
print("After update() method:", student)

# ----------------------------------------------------------------------------
# 4. Removing Items from Dictionaries
# ----------------------------------------------------------------------------

print("\n--- Removing items ---")

# Remove a specific key-value pair and return the value
major = student.pop("major")
print(f"Removed major: {major}")
print("Dictionary after pop():", student)

# Remove and return the last inserted key-value pair (Python 3.7+)
last_item = student.popitem()
print(f"Removed last item: {last_item}")
print("Dictionary after popitem():", student)

# Delete a key-value pair
del student["gpa"]
print("Dictionary after del:", student)

# Clear all items
student.clear()
print("Dictionary after clear():", student)

# ----------------------------------------------------------------------------
# 5. Dictionary Iteration
# ----------------------------------------------------------------------------

# Recreate the student dictionary
student = {
    "name": "Alice",
    "age": 21,
    "major": "Computer Science",
    "gpa": 3.8
}

print("\n--- Dictionary iteration ---")

# Iterate through keys (default)
print("Keys:")
for key in student:
    print(key)

# Iterate through values
print("\nValues:")
for value in student.values():
    print(value)

# Iterate through key-value pairs
print("\nKey-value pairs:")
for key, value in student.items():
    print(f"{key}: {value}")

# ----------------------------------------------------------------------------
# SUMMARY:
# - Dictionaries store data as key-value pairs
# - Keys must be immutable (strings, numbers, tuples)
# - Values can be any data type
# - Dictionaries are mutable (can be changed)
# - Common operations: adding, accessing, updating, and removing items
# - Methods include: get(), keys(), values(), items(), update(), pop(), popitem(), clear()
# ============================================================================ 