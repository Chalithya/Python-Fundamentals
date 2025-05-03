# ============================================================================
# FILENAME: 08_identity_operators.py
# DESCRIPTION: Demonstrates the use of identity operators in Python (is, is not)
# ============================================================================

# ----------------------------------------------------------------------------
# 1. Basic Identity Operators (is, is not)
# ----------------------------------------------------------------------------

print("BASIC IDENTITY OPERATORS:")
print("-" * 50)

# 'is' checks if two variables reference the exact same object in memory
# 'is not' checks if two variables reference different objects in memory

# Create two variables with the same value
a = 10
b = 10

# Check identity
print(f"a = {a}, b = {b}")
print(f"a is b: {a is b}")  # Usually True for small integers (implementation specific)
print(f"a is not b: {a is not b}")
print(f"id(a) = {id(a)}, id(b) = {id(b)}")  # Python's internal object IDs

# Create two variables with the same content but different objects
list1 = [1, 2, 3]
list2 = [1, 2, 3]

print(f"\nlist1 = {list1}, list2 = {list2}")
print(f"list1 is list2: {list1 is list2}")  # False, different objects
print(f"list1 is not list2: {list1 is not list2}")
print(f"id(list1) = {id(list1)}, id(list2) = {id(list2)}")  # Different IDs

# Create a reference to the same object
list3 = list1

print(f"\nlist1 = {list1}, list3 = {list3}")
print(f"list1 is list3: {list1 is list3}")  # True, same object
print(f"id(list1) = {id(list1)}, id(list3) = {id(list3)}")  # Same IDs

print("\n" + "-" * 50 + "\n")

# ----------------------------------------------------------------------------
# 2. Identity vs Equality
# ----------------------------------------------------------------------------

print("IDENTITY VS EQUALITY:")
print("-" * 50)

# 'is' checks identity (same object)
# '==' checks equality (same value)

# Same value, likely same object (implementation specific for small integers)
x = 5
y = 5
print(f"x = {x}, y = {y}")
print(f"x == y: {x == y}")   # True (same value)
print(f"x is y: {x is y}")   # Usually True for small integers (Python implementation detail)

# Same value, different objects
dict1 = {"name": "John", "age": 30}
dict2 = {"name": "John", "age": 30}
print(f"\ndict1 = {dict1}")
print(f"dict2 = {dict2}")
print(f"dict1 == dict2: {dict1 == dict2}")  # True (same content)
print(f"dict1 is dict2: {dict1 is dict2}")  # False (different objects)

# Modified object reference
list_a = [1, 2, 3]
list_b = list_a  # list_b references the same object
print(f"\nlist_a = {list_a}, list_b = {list_b}")
print(f"list_a is list_b: {list_a is list_b}")  # True

list_a.append(4)  # Modify the object
print(f"After list_a.append(4):")
print(f"list_a = {list_a}, list_b = {list_b}")  # Both change
print(f"list_a is list_b: {list_a is list_b}")  # Still True

print("\n" + "-" * 50 + "\n")

# ----------------------------------------------------------------------------
# 3. Common Use Cases for Identity Operators
# ----------------------------------------------------------------------------

print("COMMON USE CASES:")
print("-" * 50)

# 1. Checking for None
var = None
print(f"var = {var}")
print(f"var is None: {var is None}")  # Proper way to check for None

# Comparison with equality
print(f"var == None: {var == None}")  # Works but not recommended

# 2. Singleton comparison
print("\nSingleton comparison:")
# Built-in constants like None, True, and False are singletons
print(f"True is True: {True is True}")
print(f"False is False: {False is False}")
print(f"True is not False: {True is not False}")

# 3. Function returning an existing object or None
def find_item(items, target):
    """Find target in items or return None"""
    for item in items:
        if item == target:
            return item
    return None

result = find_item([1, 2, 3], 5)
print(f"\nResult of find_item([1, 2, 3], 5): {result}")
print(f"result is None: {result is None}")  # Checking if nothing was found

print("\n" + "-" * 50 + "\n")

# ----------------------------------------------------------------------------
# 4. Object Interning in Python
# ----------------------------------------------------------------------------

print("OBJECT INTERNING IN PYTHON:")
print("-" * 50)

# Python "interns" (reuses) certain objects for efficiency:
# - Small integers (typically -5 to 256, implementation-dependent)
# - Short strings (implementation-dependent)
# - None, True, False (singletons)

# Interned integers
small_a = 5
small_b = 5
print(f"small_a = {small_a}, small_b = {small_b}")
print(f"small_a is small_b: {small_a is small_b}")  # True, likely interned

# Non-interned integers (typically)
large_a = 1000
large_b = 1000
print(f"\nlarge_a = {large_a}, large_b = {large_b}")
print(f"large_a is large_b: {large_a is large_b}")  # May be False, implementation specific

# Interned strings (often short strings without spaces)
short_str_a = "hello"
short_str_b = "hello"
print(f"\nshort_str_a = '{short_str_a}', short_str_b = '{short_str_b}'")
print(f"short_str_a is short_str_b: {short_str_a is short_str_b}")  # Usually True

# Non-interned strings (typically longer strings)
long_str_a = "This is a longer string that might not be interned automatically"
long_str_b = "This is a longer string that might not be interned automatically"
print(f"\nlong_str_a and long_str_b are identical long strings")
print(f"long_str_a is long_str_b: {long_str_a is long_str_b}")  # May vary by implementation

# Force string interning
interned_a = sys.intern("a relatively long string")
interned_b = sys.intern("a relatively long string")
print(f"\nAfter using sys.intern() on identical strings:")
print(f"interned_a is interned_b: {interned_a is interned_b}")  # True

print("\n" + "-" * 50 + "\n")

# ----------------------------------------------------------------------------
# 5. Common Pitfalls with Identity Operators
# ----------------------------------------------------------------------------

print("COMMON PITFALLS:")
print("-" * 50)

# 1. Relying on interning behavior for comparison
a = 256
b = 256
print(f"a = {a}, b = {b}")
print(f"a is b: {a is b}")  # Usually True (typically interned)

c = 257
d = 257
print(f"\nc = {c}, d = {d}")
print(f"c is d: {c is d}")  # May be False, depends on implementation
print(f"c == d: {c == d}")  # Always True

# 2. Comparing floating-point numbers
float_a = 1.5
float_b = 1.5
print(f"\nfloat_a = {float_a}, float_b = {float_b}")
print(f"float_a is float_b: {float_a is float_b}")  # Implementation specific
print(f"float_a == float_b: {float_a == float_b}")  # True

# 3. Mutable vs immutable objects
# Immutable objects (int, float, str, tuple) can't be changed after creation
# Mutable objects (list, dict, set) can be modified

immutable_a = (1, 2, 3)  # Tuple (immutable)
immutable_b = (1, 2, 3)
print(f"\nimmutable_a = {immutable_a}, immutable_b = {immutable_b}")
print(f"immutable_a is immutable_b: {immutable_a is immutable_b}")  # May vary
print(f"immutable_a == immutable_b: {immutable_a == immutable_b}")  # True

mutable_a = [1, 2, 3]  # List (mutable)
mutable_b = [1, 2, 3]
print(f"\nmutable_a = {mutable_a}, mutable_b = {mutable_b}")
print(f"mutable_a is mutable_b: {mutable_a is mutable_b}")  # False
print(f"mutable_a == mutable_b: {mutable_a == mutable_b}")  # True

print("\n" + "-" * 50 + "\n")

# ----------------------------------------------------------------------------
# 6. Best Practices
# ----------------------------------------------------------------------------

print("BEST PRACTICES:")
print("-" * 50)

# 1. Use 'is' for None, True, False comparisons
value = None
print("For None comparisons:")
print(f"value is None: {value is None}")  # Good
print(f"value == None: {value == None}")  # Works but less explicit

# 2. Use '==' for value comparisons
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print("\nFor value comparisons:")
print(f"list1 == list2: {list1 == list2}")  # Good
print(f"list1 is list2: {list1 is list2}")  # Almost always False and not intended

# 3. Be cautious with object interning
a = 5
b = 5
print("\nBe cautious with interning:")
print(f"Small integers like {a} may be interned: a is b = {a is b}")
print("Don't rely on this behavior for integers, especially larger ones.")

# 4. Making copies
original = [1, 2, 3]
reference = original        # Creates a reference, not a copy
shallow_copy = original[:]  # Creates a shallow copy
import copy
deep_copy = copy.deepcopy(original)  # Creates a deep copy

print("\nDifferent ways to copy:")
print(f"original = {original}")
print(f"reference is original: {reference is original}")  # True, same object
print(f"shallow_copy is original: {shallow_copy is original}")  # False, different object
print(f"deep_copy is original: {deep_copy is original}")  # False, different object

# Modify the original list
original.append(4)
print("\nAfter original.append(4):")
print(f"original = {original}")
print(f"reference = {reference}")      # Also changed (same object)
print(f"shallow_copy = {shallow_copy}")  # Not changed (different object)
print(f"deep_copy = {deep_copy}")        # Not changed (different object)

print("\n" + "-" * 50 + "\n")

# ----------------------------------------------------------------------------
# 7. Advanced Example: Identity with Custom Objects
# ----------------------------------------------------------------------------

print("ADVANCED EXAMPLE: CUSTOM OBJECTS")
print("-" * 50)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __eq__(self, other):
        """Override equality (==) to compare based on name and age"""
        if isinstance(other, Person):
            return self.name == other.name and self.age == other.age
        return False
    
    def __str__(self):
        return f"Person(name='{self.name}', age={self.age})"

# Create two Person objects with the same values
person1 = Person("Alice", 30)
person2 = Person("Alice", 30)
person3 = person1  # Reference to person1

print(f"person1: {person1}")
print(f"person2: {person2}")
print(f"person3: {person3}")

print("\nIdentity comparison:")
print(f"person1 is person2: {person1 is person2}")  # False, different objects
print(f"person1 is person3: {person1 is person3}")  # True, same object

print("\nEquality comparison:")
print(f"person1 == person2: {person1 == person2}")  # True, because of __eq__
print(f"person1 == person3: {person1 == person3}")  # True

# Modify person1
print("\nModifying person1's age to 31")
person1.age = 31

# Check the effect
print(f"person1: {person1}")
print(f"person2: {person2}")  # Unaffected (different object)
print(f"person3: {person3}")  # Also changed (same object as person1)

print("\nComparisons after modification:")
print(f"person1 is person2: {person1 is person2}")  # Still False
print(f"person1 is person3: {person1 is person3}")  # Still True
print(f"person1 == person2: {person1 == person2}")  # Now False (different age)
print(f"person1 == person3: {person1 == person3}")  # Still True (same object)

print("\n" + "-" * 50 + "\n")

# Don't forget to import sys for using sys.intern()
import sys

# ----------------------------------------------------------------------------
# SUMMARY:
# - 'is' and 'is not' check if variables reference the same object (identity)
# - '==' and '!=' check if variables have the same value (equality)
# - Use 'is' for comparing with None, True, False
# - Use '==' for value comparisons
# - Python interns some objects (small integers, some strings), but don't rely on this
# - Reference vs copy: references share the same object, copies are independent
# - For custom objects, __eq__ determines equality behavior, but identity
#   still compares if two variables reference the exact same object
# ============================================================================ 