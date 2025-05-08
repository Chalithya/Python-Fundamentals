# ============================================================================
# FILENAME: 03_return_values.py
# DESCRIPTION: Demonstrates returning values from functions in Python
# ============================================================================

# ----------------------------------------------------------------------------
# 1. Returning a Single Value
# ----------------------------------------------------------------------------

# Define a function that returns a single value
def square(x):
    """Calculate the square of a number"""
    return x * x

# Call the function and use the return value
result = square(5)
print(f"The square of 5 is {result}")  # Output: The square of 5 is 25

# Direct use of the return value
print(f"The square of 10 is {square(10)}")  # Output: The square of 10 is 100

# ----------------------------------------------------------------------------
# 2. Returning Multiple Values
# ----------------------------------------------------------------------------

# Define a function that returns multiple values
def get_dimensions(width, height, depth):
    """Calculate various dimensions of a rectangular prism"""
    area = width * height
    volume = width * height * depth
    perimeter = 2 * (width + height)
    
    # Return multiple values (Python packs them into a tuple)
    return area, volume, perimeter

# Receive all returned values
box_area, box_volume, box_perimeter = get_dimensions(3, 4, 5)
print(f"Box area: {box_area}")         # Output: Box area: 12
print(f"Box volume: {box_volume}")     # Output: Box volume: 60
print(f"Box perimeter: {box_perimeter}")  # Output: Box perimeter: 14

# Receive as a tuple
dimensions = get_dimensions(2, 3, 4)
print(f"Dimensions tuple: {dimensions}")  # Output: Dimensions tuple: (6, 24, 10)
print(f"Volume from tuple: {dimensions[1]}")  # Output: Volume from tuple: 24

# ----------------------------------------------------------------------------
# 3. Returning None
# ----------------------------------------------------------------------------

# Function that doesn't explicitly return anything
def greet(name):
    """Greet someone without returning anything"""
    print(f"Hello, {name}!")
    # No return statement

# Call the function and try to capture the return value
result = greet("Alice")  # Prints: Hello, Alice!
print(f"Return value: {result}")  # Output: Return value: None

# Function with an explicit return of None
def check_age(age):
    """Check if someone is an adult, but don't return a result"""
    if age >= 18:
        print("You are an adult")
    else:
        print("You are a minor")
    return None  # Explicit return of None

result = check_age(20)  # Prints: You are an adult
print(f"Return value: {result}")  # Output: Return value: None

# ----------------------------------------------------------------------------
# 4. Early Returns and Conditional Returns
# ----------------------------------------------------------------------------

# Function with early returns based on conditions
def divide_safely(a, b):
    """Safely divide a by b, handling zero division"""
    # Early return for error case
    if b == 0:
        print("Error: Division by zero!")
        return None
    
    # Return for success case
    return a / b

# Try different cases
print(f"10 / 2 = {divide_safely(10, 2)}")  # Output: 10 / 2 = 5.0
print(f"10 / 0 = {divide_safely(10, 0)}")  # Prints error, Output: 10 / 0 = None

# Function with different return values based on conditions
def classify_grade(score):
    """Return a letter grade based on a numerical score"""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

print(f"Score 95: {classify_grade(95)}")  # Output: Score 95: A
print(f"Score 82: {classify_grade(82)}")  # Output: Score 82: B
print(f"Score 55: {classify_grade(55)}")  # Output: Score 55: F

# ----------------------------------------------------------------------------
# 5. Returning Complex Data Structures
# ----------------------------------------------------------------------------

# Function that returns a list
def get_factors(n):
    """Return a list of all factors of n"""
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors

print(f"Factors of 12: {get_factors(12)}")  # Output: Factors of 12: [1, 2, 3, 4, 6, 12]

# Function that returns a dictionary
def get_person_details(name, age, job):
    """Return a person's details as a dictionary"""
    return {
        "name": name,
        "age": age,
        "job": job,
        "is_adult": age >= 18,
        "can_retire": age >= 65
    }

person = get_person_details("Alice", 30, "Developer")
print(f"Person details: {person}")
# Output: Person details: {'name': 'Alice', 'age': 30, 'job': 'Developer', 'is_adult': True, 'can_retire': False}

# ----------------------------------------------------------------------------
# 6. Returning Functions (Higher-order Functions)
# ----------------------------------------------------------------------------

# Function that returns another function
def get_multiplier(factor):
    """Return a function that multiplies by the given factor"""
    def multiplier(x):
        return x * factor
    return multiplier

# Get specific multiplier functions
double = get_multiplier(2)
triple = get_multiplier(3)

# Use the returned functions
print(f"Double 5: {double(5)}")  # Output: Double 5: 10
print(f"Triple 5: {triple(5)}")  # Output: Triple 5: 15

# ----------------------------------------------------------------------------
# SUMMARY:
# - Functions can return values using the 'return' statement
# - Without a return statement, functions return None
# - Functions can return multiple values (as a tuple)
# - Early returns can be used for error handling
# - Functions can return different values based on conditions
# - Functions can return complex data structures like lists and dictionaries
# - Functions can even return other functions (higher-order functions)
# ============================================================================ 