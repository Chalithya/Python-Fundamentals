# ============================================================================
# FILENAME: 02_dictionary_methods.py
# DESCRIPTION: Demonstrating built-in methods for working with dictionaries
# ============================================================================

# ----------------------------------------------------------------------------
# 1. Create a sample dictionary
# ----------------------------------------------------------------------------

inventory = {
    "apple": 25,
    "banana": 40,
    "orange": 15,
    "mango": 20
}

print("Original inventory:", inventory)
print()

# ----------------------------------------------------------------------------
# 2. Basic methods
# ----------------------------------------------------------------------------

# Length of a dictionary
print("Number of items in inventory:", len(inventory))

# Copy a dictionary
inventory_copy = inventory.copy()
print("Copied inventory:", inventory_copy)

# Get all keys as a view object
keys = inventory.keys()
print("Keys view:", keys)
print("Keys list:", list(keys))

# Get all values as a view object
values = inventory.values()
print("Values view:", values)
print("Values list:", list(values))

# Get all key-value pairs as a view object (tuple pairs)
items = inventory.items()
print("Items view:", items)
print("Items list:", list(items))

print()

# ----------------------------------------------------------------------------
# 3. Dictionary access and retrieval methods
# ----------------------------------------------------------------------------

# get() - retrieve a value with a default if key doesn't exist
print("Number of apples:", inventory.get("apple"))
print("Number of grapes:", inventory.get("grape"))  # returns None
print("Number of grapes:", inventory.get("grape", 0))  # returns default value

# setdefault() - get value or set and return default if key doesn't exist
# It also adds the key with default value if key doesn't exist
count = inventory.setdefault("apple", 0)
print("Apple count using setdefault():", count)

count = inventory.setdefault("grape", 0)  # key doesn't exist, adds key with default value
print("Grape count using setdefault():", count)
print("Inventory after setdefault():", inventory)

print()

# ----------------------------------------------------------------------------
# 4. Modifying dictionaries with methods
# ----------------------------------------------------------------------------

# update() - update the dictionary with another dictionary or iterable of key-value pairs
inventory.update({"apple": 30, "pear": 10})
print("Inventory after update():", inventory)

# update with keyword arguments
inventory.update(banana=45, orange=25)
print("Inventory after keyword update():", inventory)

# pop() - remove specified key and return the value
removed_value = inventory.pop("mango")
print(f"Removed mango, quantity was: {removed_value}")
print("Inventory after pop():", inventory)

# Try to pop a non-existent key with a default value
try:
    removed_value = inventory.pop("kiwi")
    print(f"Removed kiwi, quantity was: {removed_value}")
except KeyError:
    print("KeyError: 'kiwi' not found in dictionary")

# With default value
removed_value = inventory.pop("kiwi", 0)
print(f"Removed kiwi, quantity was: {removed_value}")

# popitem() - remove and return the last inserted key-value pair (Python 3.7+)
last_item = inventory.popitem()
print(f"Last item removed: {last_item}")
print("Inventory after popitem():", inventory)

# clear() - remove all items from dictionary
inventory_copy.clear()
print("Inventory copy after clear():", inventory_copy)

print()

# ----------------------------------------------------------------------------
# 5. Dictionary views and their properties
# ----------------------------------------------------------------------------

# Dictionary views remain linked to the original dictionary
fruits = {"apple": 1, "banana": 2, "cherry": 3}
fruit_keys = fruits.keys()
fruit_values = fruits.values()
fruit_items = fruits.items()

print("Original dictionary:", fruits)
print("Keys view:", fruit_keys)
print("Values view:", fruit_values)
print("Items view:", fruit_items)

# Modifying the dictionary updates the views
fruits["orange"] = 4
fruits["apple"] = 10

print("\nAfter modifications:")
print("Dictionary:", fruits)
print("Keys view:", fruit_keys)  # Updated with new key
print("Values view:", fruit_values)  # Updated with new value
print("Items view:", fruit_items)  # Updated with new key-value pair

# Views support set-like operations such as union, intersection, difference
other_fruits = {"cherry": 5, "grape": 6, "kiwi": 7}
other_keys = other_fruits.keys()

print("\nSet operations on dictionary views:")
print("Keys intersection:", fruit_keys & other_keys)  # Only common keys
print("Keys union:", fruit_keys | other_keys)  # All keys from both
print("Keys difference:", fruit_keys - other_keys)  # Keys in fruits but not other_fruits

# ----------------------------------------------------------------------------
# SUMMARY:
# - Dictionary methods provide powerful tools for working with dictionaries
# - Common methods: get(), setdefault(), update(), pop(), popitem(), clear()
# - Dictionary views (keys(), values(), items()) provide dynamic references
# - Dictionary views support set-like operations when used with other views
# - Most methods have efficient implementations for performance
# ============================================================================ 