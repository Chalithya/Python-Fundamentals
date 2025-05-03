# ============================================================================
# FILENAME: 06_compound_operators.py
# DESCRIPTION: Demonstrates the use of compound operations with multiple operators
# ============================================================================

# ----------------------------------------------------------------------------
# 1. Operator Precedence in Python
# ----------------------------------------------------------------------------

print("OPERATOR PRECEDENCE EXAMPLES:")
print("-" * 50)

# Python follows operator precedence rules similar to mathematics
# The following is a simplified precedence order (from highest to lowest):
# 1. Parentheses ()
# 2. Exponentiation **
# 3. Unary operators +x, -x, ~x
# 4. Multiplication, Division, Floor Division, Modulus *, /, //, %
# 5. Addition, Subtraction +, -
# 6. Bitwise shifts << >>
# 7. Bitwise AND &
# 8. Bitwise XOR ^
# 9. Bitwise OR |
# 10. Comparisons ==, !=, >, >=, <, <=, is, is not, in, not in
# 11. Boolean NOT not
# 12. Boolean AND and
# 13. Boolean OR or

# Examples demonstrating precedence:

# Example 1: Arithmetic precedence
result = 2 + 3 * 4
print(f"2 + 3 * 4 = {result}")  # 14 (multiplication before addition)

# Using parentheses to override precedence
result = (2 + 3) * 4
print(f"(2 + 3) * 4 = {result}")  # 20 (parentheses force addition first)

# Example 2: Exponentiation has higher precedence than multiplication
result = 2 * 3 ** 2
print(f"2 * 3 ** 2 = {result}")  # 18 (3 ** 2 = 9, then 2 * 9 = 18)

# Example 3: Multiple operations follow precedence
result = 10 + 20 * 3 - 40 / 5
print(f"10 + 20 * 3 - 40 / 5 = {result}")  # 10 + 60 - 8 = 62

# Example 4: Complex expression with different operators
result = 4 + 3 * 2 ** 2 - 6 / 2
print(f"4 + 3 * 2 ** 2 - 6 / 2 = {result}")  # 4 + 3 * 4 - 3 = 4 + 12 - 3 = 13

print("\n" + "-" * 50 + "\n")

# ----------------------------------------------------------------------------
# 2. Mixing Different Types of Operators
# ----------------------------------------------------------------------------

print("MIXING DIFFERENT TYPES OF OPERATORS:")
print("-" * 50)

# Example 1: Arithmetic and comparison operators
x = 10
y = 5

# Comparison with arithmetic
result = x + y > x - y
print(f"x + y > x - y: {x} + {y} > {x} - {y} is {result}")  # 15 > 5 is True

# Example 2: Logical and comparison operators
a = 5
b = 10
c = 15

# Logical AND with comparisons
result = a < b and b < c
print(f"a < b and b < c: {a} < {b} and {b} < {c} is {result}")  # True AND True = True

# Logical OR with comparisons
result = a > b or b < c
print(f"a > b or b < c: {a} > {b} or {b} < {c} is {result}")  # False OR True = True

# Example 3: Combining arithmetic, comparison, and logical operators
result = (a + b == c) and (b * 2 > a)
print(f"(a + b == c) and (b * 2 > a): ({a} + {b} == {c}) and ({b} * 2 > {a}) is {result}")  # True AND True = True

# Example 4: Arithmetic with bitwise operators
m = 0b1010  # Binary 10
n = 0b1100  # Binary 12

# Arithmetic after bitwise
result = (m & n) + (m | n)
print(f"(m & n) + (m | n): ({bin(m)} & {bin(n)}) + ({bin(m)} | {bin(n)}) = {result}")
# (1000) + (1110) = 8 + 14 = 22

print("\n" + "-" * 50 + "\n")

# ----------------------------------------------------------------------------
# 3. Compound Assignment with Precedence
# ----------------------------------------------------------------------------

print("COMPOUND ASSIGNMENT WITH PRECEDENCE:")
print("-" * 50)

# How compound assignments handle precedence
x = 10

# Addition assignment with multiplication
x += 2 * 3  # Equivalent to x = x + (2 * 3)
print(f"After x += 2 * 3: {x}")  # 16

# Reset x
x = 10

# What if we want to do (x + 2) * 3?
# We need to use parentheses or separate statements
x = (x + 2) * 3
print(f"After x = (x + 2) * 3: {x}")  # 36

# Using multiple statements for clarity
x = 10
x += 2  # First add 2 to x
x *= 3  # Then multiply x by 3
print(f"After separate statements (x += 2, then x *= 3): {x}")  # 36

print("\n" + "-" * 50 + "\n")

# ----------------------------------------------------------------------------
# 4. Chain Comparisons
# ----------------------------------------------------------------------------

print("CHAIN COMPARISONS:")
print("-" * 50)

# Python allows chaining comparison operators
x = 5

# This is equivalent to: x > 0 and x < 10
result = 0 < x < 10
print(f"0 < x < 10: 0 < {x} < 10 is {result}")  # True

# Multiple chain comparisons
a = 3
b = 7
c = 10

# This is equivalent to: a < b and b < c and c != 15
result = a < b < c != 15
print(f"a < b < c != 15: {a} < {b} < {c} != 15 is {result}")  # True

# Beware of unexpected behavior in complex chains
# This checks: a < b > a, which is: a < b AND b > a
result = a < b > a
print(f"a < b > a: {a} < {b} > {a} is {result}")  # True

# But this could be confusing with different operators
x = 5
y = 10
z = 20

# This is: x == y or y == z
result = x == y == z
print(f"x == y == z: {x} == {y} == {z} is {result}")  # False

# More complex example
result = 1 <= x + y <= 20
print(f"1 <= x + y <= 20: 1 <= {x} + {y} <= 20 is {result}")  # True

print("\n" + "-" * 50 + "\n")

# ----------------------------------------------------------------------------
# 5. Short-Circuit Evaluation
# ----------------------------------------------------------------------------

print("SHORT-CIRCUIT EVALUATION:")
print("-" * 50)

# Logical operators in Python use short-circuit evaluation

def check_positive(x):
    print(f"Checking if {x} is positive...")
    return x > 0

# With logical AND: stops at the first False
print("Example with AND:")
result = check_positive(5) and check_positive(-3) and check_positive(10)
print(f"Result: {result}")  # Stops after checking -3
print()

# With logical OR: stops at the first True
print("Example with OR:")
result = check_positive(-5) or check_positive(3) or check_positive(-10)
print(f"Result: {result}")  # Stops after checking 3
print()

# Combining AND and OR
print("Example with combined AND and OR:")
result = (check_positive(-5) or check_positive(3)) and check_positive(10)
print(f"Result: {result}")  # True OR True = True, then True AND True = True

print("\n" + "-" * 50 + "\n")

# ----------------------------------------------------------------------------
# 6. Operator Overloading
# ----------------------------------------------------------------------------

print("OPERATOR OVERLOADING EXAMPLES:")
print("-" * 50)

# In Python, operators behave differently based on the type of operands

# String concatenation with + operator
s1 = "Hello"
s2 = "World"
result = s1 + " " + s2
print(f"String concatenation: {s1} + ' ' + {s2} = {result}")

# List concatenation with + operator
list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = list1 + list2
print(f"List concatenation: {list1} + {list2} = {result}")

# Repetition with * operator
text = "Ha"
result = text * 3
print(f"String repetition: {text} * 3 = {result}")

# List repetition with * operator
numbers = [1, 2]
result = numbers * 3
print(f"List repetition: {numbers} * 3 = {result}")

# Comparison operators with different types
print(f"String comparison: 'apple' < 'banana' is {'apple' < 'banana'}")  # Lexicographic comparison
print(f"List comparison: [1, 2] < [1, 3] is {[1, 2] < [1, 3]}")  # Element-by-element comparison

print("\n" + "-" * 50 + "\n")

# ----------------------------------------------------------------------------
# 7. Creating Custom Compound Operators
# ----------------------------------------------------------------------------

print("CUSTOM COMPOUND OPERATORS:")
print("-" * 50)

# Python allows defining how operators work with custom classes
# This is called operator overloading

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
    # Overload the + operator
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    # Overload the * operator for scalar multiplication
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
    # Right multiplication (scalar * vector)
    def __rmul__(self, scalar):
        return self.__mul__(scalar)
    
    # Overload the += operator
    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self
    
    # Overload the *= operator
    def __imul__(self, scalar):
        self.x *= scalar
        self.y *= scalar
        return self

# Create vectors
v1 = Vector(1, 2)
v2 = Vector(3, 4)

# Use + operator (calls __add__)
v3 = v1 + v2
print(f"{v1} + {v2} = {v3}")

# Use * operator (calls __mul__)
v4 = v1 * 3
print(f"{v1} * 3 = {v4}")

# Use right multiplication (calls __rmul__)
v5 = 2 * v2
print(f"2 * {v2} = {v5}")

# Use += operator (calls __iadd__)
print(f"Before +=: v1 = {v1}")
v1 += v2
print(f"After v1 += {v2}: v1 = {v1}")

# Use *= operator (calls __imul__)
print(f"Before *=: v2 = {v2}")
v2 *= 2
print(f"After v2 *= 2: v2 = {v2}")

print("\n" + "-" * 50 + "\n")

# ----------------------------------------------------------------------------
# 8. Practical Tips for Compound Operations
# ----------------------------------------------------------------------------

print("PRACTICAL TIPS:")
print("-" * 50)

# Tip 1: Use parentheses for clarity
print("Tip 1: Use parentheses for clarity")
expression1 = 4 + 5 * 2
expression2 = 4 + (5 * 2)  # Same result but more readable
print(f"Without parentheses: 4 + 5 * 2 = {expression1}")
print(f"With parentheses: 4 + (5 * 2) = {expression2}")

# Tip 2: Break complex expressions into multiple lines
print("\nTip 2: Break complex expressions into multiple lines")
print("Instead of:")
complex_result = 10 + 5 * 3 - 8 / 4 + 7 % 3
print(f"10 + 5 * 3 - 8 / 4 + 7 % 3 = {complex_result}")

print("\nConsider:")
step1 = 5 * 3        # First compute multiplication
step2 = 8 / 4        # Compute division
step3 = 7 % 3        # Compute modulus
final_result = 10 + step1 - step2 + step3  # Combine results
print(f"Broken down into steps: 10 + {step1} - {step2} + {step3} = {final_result}")

# Tip 3: Be aware of floating-point precision issues
print("\nTip 3: Be aware of floating-point precision issues")
a = 0.1 + 0.2
print(f"0.1 + 0.2 = {a}")  # May not be exactly 0.3 due to floating-point representation
print(f"Is 0.1 + 0.2 == 0.3? {a == 0.3}")  # May be False!

# Better comparison with epsilon for floating point
import math
print(f"Better comparison: {math.isclose(0.1 + 0.2, 0.3)}")  # True

# Tip 4: Pay attention to short-circuit behavior
print("\nTip 4: Pay attention to short-circuit behavior")
print("Example: Check if a key exists in a dictionary before accessing it")

user = {"name": "Alice", "age": 30}
# key_exists = user.has_key("email")  # Would raise AttributeError in Python 3
# Safe way to check and use a key
if "email" in user and user["email"].startswith("a"):
    print("User's email starts with 'a'")
else:
    print("Either user has no email or it doesn't start with 'a'")

# Tip 5: Use specific functions for complex calculations
print("\nTip 5: Use specific functions for complex calculations")
import math

# Instead of complex compound operations
radius = 5
area1 = 3.14159 * radius * radius
print(f"Area calculation with manual math: {area1}")

# Use appropriate functions
area2 = math.pi * math.pow(radius, 2)
print(f"Area calculation with math module: {area2}")

print("\n" + "-" * 50 + "\n")

# ----------------------------------------------------------------------------
# SUMMARY:
# - Python follows a specific operator precedence order similar to mathematics
# - Parentheses can be used to override the default precedence
# - Chained comparisons (a < b < c) are a convenient Python feature
# - Logical operators use short-circuit evaluation for efficiency
# - Operators behave differently based on operand types (operator overloading)
# - Custom classes can define their own operator behavior
# - Use parentheses and break down complex expressions for readability
# - Be aware of floating-point precision issues in calculations
# ============================================================================ 