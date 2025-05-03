# ============================================================================
# FILENAME: 07_membership_operators.py
# DESCRIPTION: Demonstrates the use of membership operators in Python (in, not in)
# ============================================================================

# ----------------------------------------------------------------------------
# 1. Basic Membership Operators (in, not in)
# ----------------------------------------------------------------------------

print("BASIC MEMBERSHIP OPERATORS:")
print("-" * 50)

# The 'in' operator checks if a value exists in a sequence (returns True/False)
# The 'not in' operator checks if a value does not exist in a sequence

# Example with a list
fruits = ["apple", "banana", "cherry", "orange", "kiwi"]

# Check if an item exists in a list
has_apple = "apple" in fruits
print(f"Is 'apple' in fruits? {has_apple}")  # True

# Check if an item does not exist in a list
no_grape = "grape" not in fruits
print(f"Is 'grape' not in fruits? {no_grape}")  # True

# Example with a string
greeting = "Hello, World!"

# Check if a substring exists in a string
has_hello = "Hello" in greeting
print(f"Is 'Hello' in '{greeting}'? {has_hello}")  # True

# Check if a character exists in a string
has_z = "z" in greeting
print(f"Is 'z' in '{greeting}'? {has_z}")  # False

# Case sensitivity matters
has_hello_lower = "hello" in greeting
print(f"Is 'hello' in '{greeting}'? {has_hello_lower}")  # False (case sensitive)

print("\n" + "-" * 50 + "\n")

# ----------------------------------------------------------------------------
# 2. Membership Operators with Different Data Types
# ----------------------------------------------------------------------------

print("MEMBERSHIP OPERATORS WITH DIFFERENT DATA TYPES:")
print("-" * 50)

# With lists
numbers = [1, 2, 3, 4, 5]
print(f"Is 3 in {numbers}? {3 in numbers}")  # True
print(f"Is 6 in {numbers}? {6 in numbers}")  # False

# With tuples
colors = ("red", "green", "blue")
print(f"Is 'green' in {colors}? {'green' in colors}")  # True
print(f"Is 'yellow' not in {colors}? {'yellow' not in colors}")  # True

# With sets
vowels = {"a", "e", "i", "o", "u"}
print(f"Is 'a' in {vowels}? {'a' in vowels}")  # True
print(f"Is 'y' not in {vowels}? {'y' not in vowels}")  # True

# With dictionaries (checks only keys, not values)
person = {"name": "John", "age": 30, "city": "New York"}
print(f"Is 'name' in {person}? {'name' in person}")  # True (checks keys)
print(f"Is 'John' in {person}? {'John' in person}")  # False (not a key)

# To check dictionary values
print(f"Is 'John' in person.values()? {'John' in person.values()}")  # True

# With ranges
number_range = range(1, 10)
print(f"Is 5 in range(1, 10)? {5 in number_range}")  # True
print(f"Is 10 in range(1, 10)? {10 in number_range}")  # False (range exclusive)

print("\n" + "-" * 50 + "\n")

# ----------------------------------------------------------------------------
# 3. Performance Considerations
# ----------------------------------------------------------------------------

print("PERFORMANCE CONSIDERATIONS:")
print("-" * 50)

# Different data structures have different performance characteristics
# when using membership operators

import time

# Helper function to measure execution time
def measure_time(func, iterations=1000):
    start_time = time.time()
    for _ in range(iterations):
        func()
    end_time = time.time()
    return end_time - start_time

# Create test data structures with the same elements
test_list = list(range(10000))
test_tuple = tuple(range(10000))
test_set = set(range(10000))
test_dict = {x: x for x in range(10000)}

# The element we'll search for (exists)
target_exists = 9000

# The element we'll search for (doesn't exist)
target_missing = 20000

# Define test functions
def test_list_exists():
    return target_exists in test_list

def test_tuple_exists():
    return target_exists in test_tuple

def test_set_exists():
    return target_exists in test_set

def test_dict_exists():
    return target_exists in test_dict

def test_list_missing():
    return target_missing in test_list

def test_tuple_missing():
    return target_missing in test_tuple

def test_set_missing():
    return target_missing in test_set

def test_dict_missing():
    return target_missing in test_dict

# Measure time for each (for existing element)
print("Time taken to check for an EXISTING element (seconds):")
list_time = measure_time(test_list_exists, 100)
tuple_time = measure_time(test_tuple_exists, 100)
set_time = measure_time(test_set_exists, 100)
dict_time = measure_time(test_dict_exists, 100)

print(f"List:   {list_time:.6f}s")
print(f"Tuple:  {tuple_time:.6f}s")
print(f"Set:    {set_time:.6f}s")
print(f"Dict:   {dict_time:.6f}s")

print("\nTime taken to check for a MISSING element (seconds):")
list_time = measure_time(test_list_missing, 100)
tuple_time = measure_time(test_tuple_missing, 100)
set_time = measure_time(test_set_missing, 100)
dict_time = measure_time(test_dict_missing, 100)

print(f"List:   {list_time:.6f}s")
print(f"Tuple:  {tuple_time:.6f}s")
print(f"Set:    {set_time:.6f}s")
print(f"Dict:   {dict_time:.6f}s")

print("\nConclusion:")
print("- Sets and dictionaries have O(1) average time complexity for membership testing")
print("- Lists and tuples have O(n) time complexity for membership testing")
print("- Use sets or dictionaries when you need frequent membership testing")

print("\n" + "-" * 50 + "\n")

# ----------------------------------------------------------------------------
# 4. Common Use Cases
# ----------------------------------------------------------------------------

print("COMMON USE CASES:")
print("-" * 50)

# 1. Filtering lists
print("Example 1: Filtering lists")
all_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [num for num in all_numbers if num % 2 == 0]
print(f"All numbers: {all_numbers}")
print(f"Even numbers: {even_numbers}")

# 2. Validating user input
print("\nExample 2: Validating user input")
valid_responses = ["yes", "no", "maybe"]
user_input = "yes"  # In a real app, this would come from input()
if user_input.lower() in valid_responses:
    print(f"'{user_input}' is a valid response")
else:
    print(f"'{user_input}' is not a valid response")

# 3. Checking permissions
print("\nExample 3: Checking user permissions")
user_roles = ["viewer", "editor"]
required_role = "admin"
if required_role in user_roles:
    print("User has permission to perform this action")
else:
    print("User does not have permission to perform this action")

# 4. Checking for substring
print("\nExample 4: Email validation (simplified)")
email = "user@example.com"
if "@" in email and "." in email:
    print(f"'{email}' appears to be a valid email format")
else:
    print(f"'{email}' is missing required characters")

# 5. Avoiding KeyError in dictionaries
print("\nExample 5: Safe dictionary access")
user_data = {"name": "Alice", "age": 30}

# Safe way to access a dictionary
if "email" in user_data:
    email = user_data["email"]
    print(f"User email: {email}")
else:
    print("Email not found in user data")
    
# Using .get() method as an alternative
email = user_data.get("email", "Not provided")
print(f"User email (using .get()): {email}")

print("\n" + "-" * 50 + "\n")

# ----------------------------------------------------------------------------
# 5. Advanced Techniques with Membership Operators
# ----------------------------------------------------------------------------

print("ADVANCED TECHNIQUES:")
print("-" * 50)

# 1. Checking multiple memberships
print("Example 1: Checking if any items from one list are in another")
list1 = [1, 2, 3, 4, 5]
list2 = [5, 6, 7, 8, 9]

# Check if any element in list2 is also in list1
any_common = any(item in list1 for item in list2)
print(f"Do list1 and list2 have any elements in common? {any_common}")

# Find common elements
common_elements = [item for item in list2 if item in list1]
print(f"Common elements: {common_elements}")

# 2. Set operations as an alternative
print("\nExample 2: Using set operations")
set1 = set(list1)
set2 = set(list2)

# Intersection gives common elements
intersection = set1 & set2
print(f"Intersection using sets: {intersection}")

# Difference gives elements in set1 but not in set2
difference = set1 - set2
print(f"Elements in list1 but not in list2: {difference}")

# 3. Nested membership testing
print("\nExample 3: Nested membership testing")
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Check if a value exists in a nested structure
target = 5
found = any(target in row for row in matrix)
print(f"Is {target} found in the matrix? {found}")

# 4. Membership with custom objects
print("\nExample 4: Custom objects and membership")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __eq__(self, other):
        if isinstance(other, Person):
            return self.name == other.name and self.age == other.age
        return False
    
    def __str__(self):
        return f"Person({self.name}, {self.age})"

# Create a list of Person objects
people = [
    Person("Alice", 30),
    Person("Bob", 25),
    Person("Charlie", 35)
]

# Check if a Person object exists in the list
new_person = Person("Bob", 25)
exists = new_person in people  # This works because we defined __eq__
print(f"Is {new_person} in the people list? {exists}")

# 5. Membership with custom container
print("\nExample 5: Custom container with membership test")

class Team:
    def __init__(self, name, members):
        self.name = name
        self.members = members
    
    def __contains__(self, member):
        """This special method enables the 'in' operator"""
        return member in self.members
    
    def __str__(self):
        return f"Team {self.name} with {len(self.members)} members"

# Create a team
dev_team = Team("Developers", ["Alice", "Bob", "Charlie"])

# Check if someone is in the team
print(f"{dev_team}")
print(f"Is 'Alice' in the dev team? {'Alice' in dev_team}")  # Uses __contains__
print(f"Is 'Dave' in the dev team? {'Dave' in dev_team}")    # Uses __contains__

print("\n" + "-" * 50 + "\n")

# ----------------------------------------------------------------------------
# 6. Common Mistakes and Gotchas
# ----------------------------------------------------------------------------

print("COMMON MISTAKES AND GOTCHAS:")
print("-" * 50)

# 1. Case sensitivity
print("Example 1: Case sensitivity")
fruits = ["Apple", "Banana", "Cherry"]
print(f"Is 'apple' in {fruits}? {'apple' in fruits}")  # False due to case!

# Better approach for case-insensitive search:
has_apple = any(fruit.lower() == "apple" for fruit in fruits)
print(f"Case-insensitive check: Is 'apple' in fruits? {has_apple}")

# 2. Confusing 'in' for substring vs list membership
print("\nExample 2: Substring vs list membership")
letters = ["A", "B", "C"]
word = "ABC"

print(f"Is 'A' in {letters}? {'A' in letters}")  # True, list membership
print(f"Is 'A' in '{word}'? {'A' in word}")      # True, substring check
print(f"Is 'AB' in {letters}? {'AB' in letters}")  # False, not a list element
print(f"Is 'AB' in '{word}'? {'AB' in word}")      # True, is a substring

# 3. Forgetting that dictionary membership checks keys
print("\nExample 3: Dictionary membership")
person = {"name": "John", "age": 30}
print(f"Is 'age' in {person}? {'age' in person}")       # True, checking key
print(f"Is 30 in {person}? {30 in person}")            # False, not a key

# 4. Using 'in' with unhashable types as keys
print("\nExample 4: Unhashable types")
try:
    # This will fail because lists are mutable (unhashable)
    test_set = {[1, 2, 3], [4, 5, 6]}
    print("Created a set with lists as elements")
except TypeError as e:
    print(f"Error: {e}")

# 5. Nested structures
print("\nExample 5: Checking membership in nested structures")
nested_list = [[1, 2], [3, 4], [5, 6]]
print(f"Is [1, 2] in {nested_list}? {[1, 2] in nested_list}")  # True
print(f"Is 1 in {nested_list}? {1 in nested_list}")  # False, not a top-level element

# To check if a value exists in a nested list, you need to search each sublist:
value = 4
found_in_nested = any(value in sublist for sublist in nested_list)
print(f"Is {value} in any sublist? {found_in_nested}")

print("\n" + "-" * 50 + "\n")

# ----------------------------------------------------------------------------
# SUMMARY:
# - Membership operators (in, not in) check if a value exists in a sequence
# - They work with many data types: strings, lists, tuples, sets, dictionaries
# - When used with dictionaries, 'in' checks only keys by default
# - Performance varies by data structure (sets/dicts are much faster than lists)
# - Common use cases include validation, filtering, and safe dictionary access
# - Advanced techniques include checking multiple lists and nested structures
# - Custom objects can support membership tests by implementing __eq__ or __contains__
# - Watch out for case sensitivity, nested structures, and other common gotchas
# ============================================================================ 