# ============================================================================
# FILENAME: 02_list_methods.py
# DESCRIPTION: Demonstrates common list methods in Python
# ============================================================================

# ----------------------------------------------------------------------------
# 1. List Sorting Methods
# ----------------------------------------------------------------------------

print("LIST SORTING METHODS:")

# Original unsorted list
numbers = [5, 2, 8, 1, 9, 3, 7, 4, 6]
print(f"Original list: {numbers}")

# sort() method - sorts in-place (modifies the original list)
numbers.sort()
print(f"After sort(): {numbers}")

# sort() with reverse parameter
numbers.sort(reverse=True)
print(f"After sort(reverse=True): {numbers}")

# sorted() function - returns a new sorted list, original remains unchanged
unsorted = [5, 2, 8, 1, 9, 3, 7, 4, 6]
sorted_list = sorted(unsorted)
print(f"Original list: {unsorted}")
print(f"After sorted(): {sorted_list}")

# Sorting strings
fruits = ["orange", "apple", "pear", "banana", "kiwi"]
fruits.sort()
print(f"Sorted fruits: {fruits}")

# Sorting with custom functions (sort by length)
fruits.sort(key=len)
print(f"Fruits sorted by length: {fruits}")

# ----------------------------------------------------------------------------
# 2. Adding and Removing Elements
# ----------------------------------------------------------------------------

print("\nADDING AND REMOVING ELEMENTS:")

# Create a list to work with
colors = ["red", "green", "blue"]
print(f"Original list: {colors}")

# append() - adds an element to the end
colors.append("yellow")
print(f"After append('yellow'): {colors}")

# insert() - adds an element at the specified position
colors.insert(1, "orange")
print(f"After insert(1, 'orange'): {colors}")

# extend() - adds all elements from another iterable
colors.extend(["purple", "pink"])
print(f"After extend(): {colors}")

# remove() - removes the first occurrence of a value
colors.remove("green")
print(f"After remove('green'): {colors}")

# pop() - removes and returns element at given index (or last element)
popped = colors.pop(2)
print(f"Element popped from index 2: {popped}")
print(f"After pop(2): {colors}")

last = colors.pop()  # No index - removes last element
print(f"Last element popped: {last}")
print(f"After pop(): {colors}")

# clear() - removes all elements
colors_copy = colors.copy()  # Save a copy to show clear()
colors_copy.clear()
print(f"After clear(): {colors_copy}")

# del - removes an element or slice
del colors[0]
print(f"After del colors[0]: {colors}")

# ----------------------------------------------------------------------------
# 3. Finding Information in Lists
# ----------------------------------------------------------------------------

print("\nFINDING INFORMATION IN LISTS:")

data = [5, 3, 5, 2, 1, 5, 6, 2, 3, 5]
print(f"Data list: {data}")

# count() - counts occurrences of a value
count_5 = data.count(5)
print(f"Number of 5s in the list: {count_5}")

# index() - finds the first occurrence of a value
idx_3 = data.index(3)
print(f"First occurrence of 3 is at index: {idx_3}")

# index() with start and end parameters
idx_3_after_first = data.index(3, idx_3 + 1)  # Start after first occurrence
print(f"Second occurrence of 3 is at index: {idx_3_after_first}")

# in operator - checks if value exists
exists = 7 in data
print(f"Is 7 in the list? {exists}")

# Finding minimum and maximum values
min_val = min(data)
max_val = max(data)
print(f"Minimum value: {min_val}")
print(f"Maximum value: {max_val}")

# Calculate sum
total = sum(data)
print(f"Sum of all values: {total}")

# ----------------------------------------------------------------------------
# 4. Copying and Referencing Lists
# ----------------------------------------------------------------------------

print("\nCOPYING AND REFERENCING LISTS:")

original = [1, 2, 3, 4]
print(f"Original list: {original}")

# Reference (not a copy) - changes to one affect the other
reference = original
reference.append(5)
print(f"Original after modifying reference: {original}")
print(f"Reference: {reference}")

# Shallow copy methods
copy1 = original.copy()  # Using copy() method
copy2 = list(original)   # Using list() constructor
copy3 = original[:]      # Using slicing

# Modify copies to show they're independent
copy1.append(6)
copy2.append(7)
copy3.append(8)

print(f"Original: {original}")
print(f"copy1: {copy1}")
print(f"copy2: {copy2}")
print(f"copy3: {copy3}")

# With nested lists, shallow copies don't copy nested objects
nested = [[1, 2], [3, 4]]
shallow = nested.copy()
shallow[0][0] = 99  # This will affect the original too

print(f"Nested original: {nested}")
print(f"Shallow copy: {shallow}")

# Deep copy
import copy
deep = copy.deepcopy(nested)
deep[1][0] = 88  # This won't affect the original

print(f"Original after deep copy modified: {nested}")
print(f"Deep copy: {deep}")

# ----------------------------------------------------------------------------
# 5. Other Useful List Methods
# ----------------------------------------------------------------------------

print("\nOTHER USEFUL LIST METHODS:")

items = [3, 1, 4, 1, 5]
print(f"Original list: {items}")

# reverse() - reverses the elements in-place
items.reverse()
print(f"After reverse(): {items}")

# reversed() - returns an iterator that accesses the list in reverse order
rev_iterator = reversed(items)
rev_list = list(rev_iterator)  # Convert iterator to list
print(f"Using reversed(): {rev_list}")

# list comprehension with methods
squared = [x**2 for x in items]
print(f"Squared values using comprehension: {squared}")

# ----------------------------------------------------------------------------
# SUMMARY:
# - Lists have many built-in methods for common operations
# - sort() and reverse() modify the list in-place
# - sorted() and reversed() return new objects without changing the original
# - append(), insert(), extend() add elements to a list
# - remove(), pop(), clear() remove elements from a list
# - count(), index() help with finding information
# - To truly copy a list, use copy() or slicing [:]
# - For nested lists, use copy.deepcopy() for a true independent copy
# ============================================================================ 