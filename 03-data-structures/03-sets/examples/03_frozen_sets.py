# ============================================================================
# FILENAME: 03_frozen_sets.py
# DESCRIPTION: Demonstrating frozen sets - immutable versions of sets
# ============================================================================

# ----------------------------------------------------------------------------
# 1. Creating Frozen Sets
# ----------------------------------------------------------------------------

# Create a regular set
regular_set = {1, 2, 3, 4, 5}
print("Regular set:", regular_set)

# Create a frozen set using frozenset()
frozen_set = frozenset([1, 2, 3, 4, 5])
print("Frozen set:", frozen_set)

# Create a frozen set from a regular set
another_frozen_set = frozenset(regular_set)
print("Another frozen set:", another_frozen_set)

# Create an empty frozen set
empty_frozen_set = frozenset()
print("Empty frozen set:", empty_frozen_set)

# Frozen set from a string
chars_frozen_set = frozenset("hello")
print("Frozen set from string:", chars_frozen_set)

print()

# ----------------------------------------------------------------------------
# 2. Immutability of Frozen Sets
# ----------------------------------------------------------------------------

print("Demonstrating immutability of frozen sets:")

# This all works with regular sets:
print("\nWith regular sets:")
try:
    regular_set.add(6)
    print("Added 6 to regular set:", regular_set)
    
    regular_set.remove(3)
    print("Removed 3 from regular set:", regular_set)
    
    regular_set.clear()
    print("Cleared regular set:", regular_set)
except Exception as e:
    print(f"Error with regular set: {e}")

# Now let's try with frozen sets - these will fail
print("\nWith frozen sets:")

# Try to add an element
try:
    frozen_set.add(6)
    print("This will not be executed")
except AttributeError as e:
    print(f"Cannot add to frozen set: {e}")

# Try to remove an element
try:
    frozen_set.remove(3)
    print("This will not be executed")
except AttributeError as e:
    print(f"Cannot remove from frozen set: {e}")

# Try to clear the set
try:
    frozen_set.clear()
    print("This will not be executed")
except AttributeError as e:
    print(f"Cannot clear frozen set: {e}")

# Try to update the set
try:
    frozen_set.update([6, 7, 8])
    print("This will not be executed")
except AttributeError as e:
    print(f"Cannot update frozen set: {e}")

print()

# ----------------------------------------------------------------------------
# 3. Operations That Work with Frozen Sets
# ----------------------------------------------------------------------------

# Define some frozen sets for operations
fs1 = frozenset([1, 2, 3, 4, 5])
fs2 = frozenset([4, 5, 6, 7, 8])

print("Frozen set 1:", fs1)
print("Frozen set 2:", fs2)

# Membership testing
print("\nIs 3 in fs1?", 3 in fs1)
print("Is 6 in fs1?", 6 in fs1)

# Size
print("\nSize of fs1:", len(fs1))

# Iteration
print("\nIterating through fs1:")
for item in fs1:
    print(f"- {item}")

# Union (returns a new frozen set)
union_result = fs1.union(fs2)
print("\nUnion result:", union_result)
print("Type of union result:", type(union_result))

# Intersection
intersection_result = fs1.intersection(fs2)
print("\nIntersection result:", intersection_result)

# Difference
difference_result = fs1.difference(fs2)
print("\nDifference result:", difference_result)

# Symmetric difference
symmetric_difference_result = fs1.symmetric_difference(fs2)
print("\nSymmetric difference result:", symmetric_difference_result)

# Using operators with frozen sets
print("\nUsing operators:")
print("fs1 | fs2:", fs1 | fs2)
print("fs1 & fs2:", fs1 & fs2)
print("fs1 - fs2:", fs1 - fs2)
print("fs1 ^ fs2:", fs1 ^ fs2)

print()

# ----------------------------------------------------------------------------
# 4. Comparing Sets and Frozen Sets
# ----------------------------------------------------------------------------

ordinary_set = {1, 2, 3}
frozen_version = frozenset(ordinary_set)

print("Ordinary set:", ordinary_set)
print("Frozen version:", frozen_version)

# Equality check
print("\nAre they equal?", ordinary_set == frozen_version)  # True - same elements

# You can convert back from frozen to regular set
back_to_regular = set(frozen_version)
print("\nConverted back to regular set:", back_to_regular)
print("Type:", type(back_to_regular))

print()

# ----------------------------------------------------------------------------
# 5. Use Cases for Frozen Sets
# ----------------------------------------------------------------------------

# 1. As dictionary keys (regular sets can't be used as keys)
print("Using frozen sets as dictionary keys:")

# This works
city_temps = {
    frozenset(["New York", "NYC", "Big Apple"]): 75,
    frozenset(["Los Angeles", "LA", "City of Angels"]): 85,
    frozenset(["Chicago", "Windy City"]): 68
}

print("\nCity temperatures dictionary:", city_temps)

# Look up temperature using a frozen set key
nyc_key = frozenset(["NYC", "New York", "Big Apple"])
print(f"Temperature in New York: {city_temps[nyc_key]}°F")

# This would fail with regular sets
try:
    bad_dict = {
        {"New York", "NYC"}: 75  # TypeError: unhashable type: 'set'
    }
except TypeError as e:
    print(f"\nError using regular set as dict key: {e}")

# 2. In nested sets
print("\nUsing frozen sets in nested sets:")

# This works: a set containing frozensets
languages_by_type = {
    frozenset(["Python", "Ruby", "Perl"]): "Scripting",
    frozenset(["Java", "C#", "C++"]): "Compiled",
    frozenset(["JavaScript", "TypeScript"]): "Web"
}

print("\nLanguages by type:", languages_by_type)

# 3. As elements in regular sets
print("\nUsing frozen sets as elements in regular sets:")

# This works
set_of_frozensets = {
    frozenset([1, 2, 3]),
    frozenset([4, 5, 6]),
    frozenset([1, 2])
}

print("Set of frozen sets:", set_of_frozensets)

# This would fail
try:
    set_of_sets = {
        {1, 2, 3},  # TypeError: unhashable type: 'set'
        {4, 5, 6}
    }
except TypeError as e:
    print(f"\nError using regular sets inside a set: {e}")

print()

# ----------------------------------------------------------------------------
# 6. Practical Example
# ----------------------------------------------------------------------------

# Using frozen sets to model groups of students
class_a = frozenset(["Alice", "Bob", "Charlie", "David"])
class_b = frozenset(["Eve", "Frank", "Grace", "Heidi"])
class_c = frozenset(["Charlie", "David", "Ivan", "Judy"])

# Create a dictionary using these immutable groups as keys
performance = {
    class_a: "Excellent",
    class_b: "Good",
    class_c: "Average"
}

print("Class A students:", class_a)
print("Class B students:", class_b)
print("Class C students:", class_c)

print("\nPerformance by class:")
for students, rating in performance.items():
    print(f"Group of {len(students)} students: {rating}")

# Find students in both class A and class C
common_students = class_a.intersection(class_c)
print("\nStudents in both Class A and Class C:", common_students)

# Find all unique students across all classes
all_students = class_a.union(class_b, class_c)
print("\nAll students:", all_students)
print("Total number of students:", len(all_students))

# ----------------------------------------------------------------------------
# SUMMARY:
# - Frozen sets are immutable versions of sets in Python
# - Created using the frozenset() constructor
# - Cannot be modified after creation (no add, remove, update, clear, etc.)
# - Support all non-modifying set operations (union, intersection, etc.)
# - Can be used as dictionary keys and elements in other sets
# - Useful when you need hashable set-like objects
# - Perfect for representing data that shouldn't change
# ============================================================================ 