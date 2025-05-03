# ============================================================================
# FILENAME: 05_assignment_operators.py
# DESCRIPTION: Demonstrates the use of assignment operators in Python
# ============================================================================

# ----------------------------------------------------------------------------
# 1. Basic Assignment Operator (=)
# ----------------------------------------------------------------------------

# The most basic assignment operator (=) assigns a value to a variable
x = 10
print(f"Basic assignment: x = 10, x = {x}")

# Sequential assignment
a, b, c = 1, 2, 3
print(f"Sequential assignment: a = {a}, b = {b}, c = {c}")

# Swapping values using tuple unpacking
a, b = 5, 10
print(f"Before swap: a = {a}, b = {b}")
a, b = b, a  # Swapping without a temporary variable
print(f"After swap: a = {a}, b = {b}")

# Assignment unpacking with collections
numbers = [1, 2, 3]
x, y, z = numbers
print(f"Unpacking list: x = {x}, y = {y}, z = {z}")

# Extended unpacking (Python 3.x)
first, *middle, last = [1, 2, 3, 4, 5]
print(f"Extended unpacking: first = {first}, middle = {middle}, last = {last}")

# Assignment to multiple variables
same_value = all_equal = 100
print(f"Multiple assignment: same_value = {same_value}, all_equal = {all_equal}")

print("\n" + "-" * 50 + "\n")

# ----------------------------------------------------------------------------
# 2. Augmented Assignment Operators
# ----------------------------------------------------------------------------

print("Augmented Assignment Operators:")

# These operators combine an arithmetic or bitwise operation with assignment.
# They're more concise versions of operations like x = x + y.

# Original assignment
counter = 10

# Addition assignment (+=)
counter += 5  # Same as: counter = counter + 5
print(f"After counter += 5: {counter}")  # 15

# Subtraction assignment (-=)
counter -= 3  # Same as: counter = counter - 3
print(f"After counter -= 3: {counter}")  # 12

# Multiplication assignment (*=)
counter *= 2  # Same as: counter = counter * 2
print(f"After counter *= 2: {counter}")  # 24

# Division assignment (/=)
counter /= 4  # Same as: counter = counter / 4
print(f"After counter /= 4: {counter}")  # 6.0 (note: now a float)

# Floor division assignment (//=)
number = 17
number //= 5  # Same as: number = number // 5
print(f"After number //= 5: {number}")  # 3

# Modulus assignment (%=)
number = 17
number %= 5  # Same as: number = number % 5
print(f"After number %= 5: {number}")  # 2

# Exponentiation assignment (**=)
number = 2
number **= 3  # Same as: number = number ** 3
print(f"After number **= 3: {number}")  # 8

print("\n" + "-" * 50 + "\n")

# ----------------------------------------------------------------------------
# 3. Bitwise Augmented Assignment Operators
# ----------------------------------------------------------------------------

print("Bitwise Augmented Assignment Operators:")

# These operators combine bitwise operations with assignment

# Binary AND assignment (&=)
a = 0b1010  # Binary 10
a &= 0b1100  # Binary 12
print(f"After a &= 0b1100: {a} (binary: {bin(a)[2:].zfill(4)})")  # Should be 8 (1000)

# Binary OR assignment (|=)
a = 0b1010  # Binary 10
a |= 0b1100  # Binary 12
print(f"After a |= 0b1100: {a} (binary: {bin(a)[2:].zfill(4)})")  # Should be 14 (1110)

# Binary XOR assignment (^=)
a = 0b1010  # Binary 10
a ^= 0b1100  # Binary 12
print(f"After a ^= 0b1100: {a} (binary: {bin(a)[2:].zfill(4)})")  # Should be 6 (0110)

# Binary right shift assignment (>>=)
a = 0b1000  # Binary 8
a >>= 2  # Shift right by 2 bits
print(f"After a >>= 2: {a} (binary: {bin(a)[2:]})")  # Should be 2 (10)

# Binary left shift assignment (<<=)
a = 0b0001  # Binary 1
a <<= 3  # Shift left by 3 bits
print(f"After a <<= 3: {a} (binary: {bin(a)[2:]})")  # Should be 8 (1000)

print("\n" + "-" * 50 + "\n")

# ----------------------------------------------------------------------------
# 4. Using Augmented Assignment with Strings and Collections
# ----------------------------------------------------------------------------

print("Augmented Assignment with Different Data Types:")

# With strings
greeting = "Hello"
greeting += ", World!"  # String concatenation
print(f"String concatenation: {greeting}")

# With lists
numbers = [1, 2, 3]
numbers += [4, 5]  # List concatenation
print(f"List concatenation: {numbers}")

# With tuples
coordinates = (10, 20)
coordinates += (30, 40)  # Tuple concatenation
print(f"Tuple concatenation: {coordinates}")

# Multiplication assignment with sequences
word = "abc"
word *= 3  # String repetition
print(f"String repetition: {word}")

nums = [1, 2]
nums *= 3  # List repetition
print(f"List repetition: {nums}")

print("\n" + "-" * 50 + "\n")

# ----------------------------------------------------------------------------
# 5. Chained Augmented Assignment
# ----------------------------------------------------------------------------

print("Chained Augmented Assignment:")

# You can chain multiple augmented assignments
x = 5
x += 3 - 2  # First evaluates 3-2=1, then x += 1
print(f"After x += 3 - 2: {x}")  # 6

x = 10
x *= 2 + 3  # First evaluates 2+3=5, then x *= 5
print(f"After x *= 2 + 3: {x}")  # 50

print("\n" + "-" * 50 + "\n")

# ----------------------------------------------------------------------------
# 6. Comparison of Normal Assignment vs. Augmented Assignment
# ----------------------------------------------------------------------------

print("Comparison of Normal vs. Augmented Assignment:")

# Performance-wise, augmented assignments can be more efficient
# Especially with more complex objects, since they may be able to modify in-place

import time

# With strings
start_time = time.time()
s = ""
for i in range(1000):
    s = s + str(i)
normal_time = time.time() - start_time

start_time = time.time()
s = ""
for i in range(1000):
    s += str(i)
augmented_time = time.time() - start_time

print(f"String concatenation - normal: {normal_time:.6f}s, augmented: {augmented_time:.6f}s")

# With lists
start_time = time.time()
my_list = []
for i in range(1000):
    my_list = my_list + [i]
normal_time = time.time() - start_time

start_time = time.time()
my_list = []
for i in range(1000):
    my_list += [i]
augmented_time = time.time() - start_time

print(f"List concatenation - normal: {normal_time:.6f}s, augmented: {augmented_time:.6f}s")

print("\n" + "-" * 50 + "\n")

# ----------------------------------------------------------------------------
# 7. Notes and Best Practices for Assignment Operators
# ----------------------------------------------------------------------------

print("Notes and Best Practices:")

# 1. Readability
print("- Use augmented assignment when it makes code more readable")
print("- For complex expressions, break them down into separate statements")

# 2. Type conversion
print("\n- Beware of type conversion with division")
x = 10
x /= 3  # Converts to float
print(f"  After x /= 3: {x} (type: {type(x).__name__})")

# 3. Mutable vs Immutable types
print("\n- With mutable objects, augmented assignment may modify in-place")
print("  or create a new object depending on the operation:")

# Example with lists (mutable)
original_list = [1, 2, 3]
alias = original_list  # Both variables refer to the same list
original_list += [4]
print(f"  After +=: original_list = {original_list}, alias = {alias}")
print(f"  Are they the same object? {original_list is alias}")  # True, modified in-place

# Example with immutable objects
x = 5
y = x  # Both variables hold the same value, but are separate objects
x += 5
print(f"  After x += 5: x = {x}, y = {y}")  # x is modified, y is not

# 4. Avoid side effects
print("\n- Be cautious of side effects with method calls")

class Counter:
    def __init__(self, value):
        self.value = value
    
    def __iadd__(self, other):
        self.value += other
        print("  __iadd__ method called")
        return self

counter = Counter(5)
counter += 3  # This calls counter.__iadd__(3) and assigns the result back to counter
print(f"  Final counter value: {counter.value}")

print("\n" + "-" * 50 + "\n")

# ----------------------------------------------------------------------------
# 8. Assignment with Walrus Operator (:=) - Python 3.8+
# ----------------------------------------------------------------------------

# The walrus operator allows assignment as part of an expression

try:
    # Check Python version (will work in Python 3.8+)
    import sys
    if sys.version_info >= (3, 8):
        print("Walrus Operator (:=) Examples:")
        
        # Example 1: Assign in a condition
        if (n := len([1, 2, 3])) > 2:
            print(f"List has {n} items")
        
        # Example 2: Assign in a loop condition
        numbers = [1, 2, 3, 4, 5]
        total = 0
        while (num := numbers.pop(0)) <= 3:
            total += num
            print(f"Processing {num}, total so far: {total}")
            if not numbers:
                break
        
        # Example 3: Assign in a list comprehension
        print([result := i * 2 for i in range(5)][-1], f"Last result: {result}")
    else:
        print("Walrus Operator Examples (Python 3.8+ only):")
        print("Your Python version does not support the walrus operator.")
except:
    print("Walrus Operator Examples (Python 3.8+ only):")
    print("Your Python version does not support the walrus operator.")

# ----------------------------------------------------------------------------
# SUMMARY:
# - Basic assignment (=) assigns a value to a variable
# - Python supports multiple assignments in a single line
# - Augmented assignment operators combine an operation with assignment (+=, -=, etc.)
# - Augmented assignment with strings and collections concatenates or repeats
# - Bitwise augmented assignments perform binary operations on integers
# - Augmented assignments can be more efficient for complex operations
# - Mutable objects may be modified in-place with augmented assignments
# - The walrus operator (:=) allows assignment within expressions (Python 3.8+)
# ============================================================================ 