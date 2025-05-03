# ============================================================================
# FILENAME: 01_arithmetic_operators.py
# DESCRIPTION: Demonstrates the use of arithmetic operators in Python
# ============================================================================

# ----------------------------------------------------------------------------
# 1. Basic Arithmetic Operations
# ----------------------------------------------------------------------------

a = 10
b = 3

# Addition (+)
addition_result = a + b
print(f"Addition: {a} + {b} = {addition_result}")  # Output: 13

# Subtraction (-)
subtraction_result = a - b
print(f"Subtraction: {a} - {b} = {subtraction_result}")  # Output: 7

# Multiplication (*)
multiplication_result = a * b
print(f"Multiplication: {a} * {b} = {multiplication_result}")  # Output: 30

# Division (/) - always returns a float in Python 3.x
division_result = a / b
print(f"Division: {a} / {b} = {division_result}")  # Output: 3.3333...

# Floor Division (//) - returns the integer part of the division
floor_division_result = a // b
print(f"Floor Division: {a} // {b} = {floor_division_result}")  # Output: 3

# Modulus (%) - returns the remainder of the division
modulus_result = a % b
print(f"Modulus: {a} % {b} = {modulus_result}")  # Output: 1

# Exponentiation (**)
exponentiation_result = a ** b
print(f"Exponentiation: {a} ** {b} = {exponentiation_result}")  # Output: 1000

print("\n" + "-" * 50 + "\n")

# ----------------------------------------------------------------------------
# 2. Operator Behavior with Different Data Types
# ----------------------------------------------------------------------------

# Integer arithmetic
int_result = 5 + 3
print(f"Integer addition: 5 + 3 = {int_result} ({type(int_result).__name__})")

# Float arithmetic
float_result = 5.0 + 3.0
print(f"Float addition: 5.0 + 3.0 = {float_result} ({type(float_result).__name__})")

# Mixed type arithmetic (int and float)
mixed_result = 5 + 3.0
print(f"Mixed addition: 5 + 3.0 = {mixed_result} ({type(mixed_result).__name__})")

# String "addition" (concatenation)
str_result = "Hello" + " " + "World"
print(f"String concatenation: \"Hello\" + \" \" + \"World\" = \"{str_result}\"")

# String multiplication (repeats the string)
str_mult_result = "Python " * 3
print(f"String multiplication: \"Python \" * 3 = \"{str_mult_result}\"")

# List "addition" (concatenation)
list_result = [1, 2, 3] + [4, 5, 6]
print(f"List concatenation: [1, 2, 3] + [4, 5, 6] = {list_result}")

# List multiplication (repeats the list)
list_mult_result = [1, 2, 3] * 3
print(f"List multiplication: [1, 2, 3] * 3 = {list_mult_result}")

print("\n" + "-" * 50 + "\n")

# ----------------------------------------------------------------------------
# 3. Type Conversion in Arithmetic Operations
# ----------------------------------------------------------------------------

# Integer ÷ Integer = Float (in Python 3.x)
print(f"10 / 3 = {10 / 3} ({type(10 / 3).__name__})")

# Floor division truncates towards negative infinity
print(f"10 // 3 = {10 // 3} ({type(10 // 3).__name__})")
print(f"10 // -3 = {10 // -3} ({type(10 // 3).__name__})")
print(f"-10 // 3 = {-10 // 3} ({type(-10 // 3).__name__})")  # Note the result

# Using modulo with negative numbers
print(f"10 % 3 = {10 % 3}")
print(f"-10 % 3 = {-10 % 3}")  # Note: (a % b) has the same sign as b in Python
print(f"10 % -3 = {10 % -3}")  # Result has the same sign as divisor

print("\n" + "-" * 50 + "\n")

# ----------------------------------------------------------------------------
# 4. Division by Zero and Other Arithmetic Errors
# ----------------------------------------------------------------------------

# Handling potential runtime errors with try/except
try:
    result = 10 / 0
    print(f"10 / 0 = {result}")  # This line never executes
except ZeroDivisionError as e:
    print(f"Error: {e}")  # Output: Error: division by zero

# Floor division and modulo with zero also cause errors
try:
    result = 10 // 0
    print(f"10 // 0 = {result}")
except ZeroDivisionError as e:
    print(f"Error: {e}")

try:
    result = 10 % 0
    print(f"10 % 0 = {result}")
except ZeroDivisionError as e:
    print(f"Error: {e}")

print("\n" + "-" * 50 + "\n")

# ----------------------------------------------------------------------------
# 5. Precedence and Order of Operations
# ----------------------------------------------------------------------------

# Python follows the standard mathematical order of operations (PEMDAS)
# Parentheses, Exponents, Multiplication/Division, Addition/Subtraction

# Example without parentheses
result_without_parentheses = 2 + 3 * 4
print(f"2 + 3 * 4 = {result_without_parentheses}")  # Output: 14 (3*4 is calculated first)

# Same example with parentheses
result_with_parentheses = (2 + 3) * 4
print(f"(2 + 3) * 4 = {result_with_parentheses}")  # Output: 20

# Complex expression
complex_expr = 2 ** 3 * 4 + 5 // 2 - 7
print(f"2 ** 3 * 4 + 5 // 2 - 7 = {complex_expr}")  # Output: 26

# Breakdown of the complex expression:
# 2 ** 3 = 8
# 8 * 4 = 32
# 5 // 2 = 2
# 32 + 2 = 34
# 34 - 7 = 27
print("Breakdown of 2 ** 3 * 4 + 5 // 2 - 7:")
print("1. 2 ** 3 = 8 (exponentiation has highest precedence)")
print("2. 8 * 4 = 32 (multiplication is next)")
print("3. 5 // 2 = 2 (floor division has same precedence as multiplication)")
print("4. 32 + 2 = 34 (addition is next)")
print("5. 34 - 7 = 27 (subtraction has same precedence as addition)")

print("\n" + "-" * 50 + "\n")

# ----------------------------------------------------------------------------
# 6. Practical Applications
# ----------------------------------------------------------------------------

# Calculate average
scores = [85, 92, 78, 95, 88]
total = sum(scores)
average = total / len(scores)
print(f"Scores: {scores}")
print(f"Total: {total}")
print(f"Average: {average:.2f}")  # Formatted to 2 decimal places

# Calculate compound interest
principal = 1000  # Initial investment
rate = 0.05       # 5% annual interest rate
years = 5         # Investment period
compound_frequency = 12  # Monthly compounding

# Formula: A = P(1 + r/n)^(nt)
amount = principal * (1 + rate/compound_frequency)**(compound_frequency * years)
profit = amount - principal

print(f"\nInvestment Calculator:")
print(f"Principal: ${principal}")
print(f"Annual Rate: {rate*100}%")
print(f"Time: {years} years")
print(f"Compounding: {compound_frequency} times per year")
print(f"Final Amount: ${amount:.2f}")
print(f"Profit: ${profit:.2f}")

# Calculate time estimation
distance = 150  # km
speed = 65      # km/h
time_hours = distance / speed
time_minutes = (time_hours - int(time_hours)) * 60

print(f"\nTravel Time Estimation:")
print(f"Distance: {distance} km")
print(f"Speed: {speed} km/h")
print(f"Estimated Time: {int(time_hours)} hours and {int(time_minutes)} minutes")

# Area and perimeter calculations
length = 10
width = 6
area = length * width
perimeter = 2 * (length + width)

print(f"\nRectangle Dimensions:")
print(f"Length: {length} units")
print(f"Width: {width} units")
print(f"Area: {area} square units")
print(f"Perimeter: {perimeter} units")

print("\n" + "-" * 50 + "\n")

# ----------------------------------------------------------------------------
# 7. Performance Considerations
# ----------------------------------------------------------------------------

# Integer arithmetic is generally faster than floating-point
import time

# Integer multiplication performance
start_time = time.time()
result = 0
for i in range(50000000):
    result = 5 * 7
int_time = time.time() - start_time

# Float multiplication performance
start_time = time.time()
result = 0
for i in range(50000000):
    result = 5.0 * 7.0
float_time = time.time() - start_time

print("Performance Comparison:")
print(f"Integer Multiplication Time: {int_time:.6f} seconds")
print(f"Float Multiplication Time: {float_time:.6f} seconds")
print(f"Ratio (Float/Int): {float_time/int_time:.2f}x")

# Note: the actual ratio and timing will vary between systems and Python implementations

# ----------------------------------------------------------------------------
# SUMMARY:
# - Python provides all standard arithmetic operators: +, -, *, /, //, %, **
# - Division (/) always returns a float in Python 3.x
# - Floor division (//) returns the integer quotient
# - Modulus (%) returns the remainder of division
# - Operators may behave differently with different data types
# - The standard mathematical order of operations (PEMDAS) applies
# - Arithmetic operations may raise exceptions like ZeroDivisionError
# - Integer arithmetic is generally faster than floating-point arithmetic
# ============================================================================ 