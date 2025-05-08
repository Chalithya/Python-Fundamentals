# ============================================================================
# FILENAME: 01_functions_as_objects.py
# DESCRIPTION: Demonstrates the concept of functions as first-class objects in Python
# ============================================================================

# ----------------------------------------------------------------------------
# 1. Assigning Functions to Variables
# ----------------------------------------------------------------------------

def greet(name):
    """Return a greeting message"""
    return f"Hello, {name}!"

# Assign the function to a variable (without calling it)
greeting_function = greet

# Now we can call the function using the variable
print(greeting_function("Alice"))  # Output: Hello, Alice!

# The function object is the same
print(f"Original function: {greet}")
print(f"Function variable: {greeting_function}")
print(f"Are they the same object? {greet is greeting_function}")  # True

# ----------------------------------------------------------------------------
# 2. Passing Functions as Arguments
# ----------------------------------------------------------------------------

def apply_operation(x, y, operation):
    """Apply a mathematical operation to two numbers"""
    return operation(x, y)

def add(a, b):
    """Add two numbers"""
    return a + b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def power(a, b):
    """Raise a to the power of b"""
    return a ** b

# Pass different functions as arguments
result1 = apply_operation(5, 3, add)
result2 = apply_operation(5, 3, multiply)
result3 = apply_operation(5, 3, power)

print(f"5 + 3 = {result1}")  # Output: 5 + 3 = 8
print(f"5 * 3 = {result2}")  # Output: 5 * 3 = 15
print(f"5 ^ 3 = {result3}")  # Output: 5 ^ 3 = 125

# ----------------------------------------------------------------------------
# 3. Returning Functions from Functions
# ----------------------------------------------------------------------------

def create_multiplier(factor):
    """Return a function that multiplies its argument by factor"""
    def multiplier(x):
        return x * factor
    return multiplier

# Create specific multiplier functions
double = create_multiplier(2)
triple = create_multiplier(3)

print(f"Double 5: {double(5)}")  # Output: Double 5: 10
print(f"Triple 5: {triple(5)}")  # Output: Triple 5: 15

# Check that these are indeed function objects
print(f"Type of double: {type(double)}")  # Output: <class 'function'>

# ----------------------------------------------------------------------------
# 4. Storing Functions in Data Structures
# ----------------------------------------------------------------------------

# Store functions in a dictionary
operations = {
    'add': add,
    'multiply': multiply,
    'power': power,
    'double': create_multiplier(2)
}

# Use functions from the dictionary
print(f"Dictionary add: {operations['add'](10, 5)}")  # Output: 15
print(f"Dictionary multiply: {operations['multiply'](10, 5)}")  # Output: 50
print(f"Dictionary double: {operations['double'](10)}")  # Output: 20

# Store functions in a list
math_operations = [add, multiply, power]

# Apply all operations in the list to the same inputs
for operation in math_operations:
    print(f"Result of {operation.__name__}: {operation(10, 2)}")

# ----------------------------------------------------------------------------
# 5. Function Attributes
# ----------------------------------------------------------------------------

# Functions are objects and can have attributes
def analyze_data(data, method='mean'):
    """Analyze data using the specified method"""
    if method == 'mean':
        return sum(data) / len(data)
    elif method == 'max':
        return max(data)
    elif method == 'min':
        return min(data)
    else:
        raise ValueError(f"Unknown method: {method}")

# Add attributes to the function
analyze_data.version = '1.0'
analyze_data.author = 'Python Fundamentals'
analyze_data.supported_methods = ['mean', 'max', 'min']

# Use the function
data = [1, 5, 3, 7, 2]
print(f"Mean: {analyze_data(data)}")  # Output: Mean: 3.6

# Access the function's attributes
print(f"Function version: {analyze_data.version}")
print(f"Function author: {analyze_data.author}")
print(f"Supported methods: {', '.join(analyze_data.supported_methods)}")

# ----------------------------------------------------------------------------
# 6. Function Introspection
# ----------------------------------------------------------------------------

# Function attributes that are available by default
print(f"Function name: {analyze_data.__name__}")
print(f"Function docstring: {analyze_data.__doc__}")
print(f"Function module: {analyze_data.__module__}")
print(f"Function default arguments: {analyze_data.__defaults__}")

# Get information about function parameters
import inspect

# Get the signature
signature = inspect.signature(analyze_data)
print(f"Function signature: {signature}")

# Get parameter information
for name, param in signature.parameters.items():
    print(f"Parameter: {name}, default: {param.default if param.default is not inspect.Parameter.empty else 'No default'}")

# ----------------------------------------------------------------------------
# 7. Practical Example: Function Registry
# ----------------------------------------------------------------------------

# Create a function registry for data transformations
transformation_registry = {}

def register_transformation(func):
    """Register a transformation function in the registry"""
    transformation_registry[func.__name__] = func
    return func  # Return the function unchanged

# Register some transformation functions
@register_transformation
def uppercase(text):
    """Convert text to uppercase"""
    return text.upper()

@register_transformation
def reverse(text):
    """Reverse the text"""
    return text[::-1]

@register_transformation
def capitalize_words(text):
    """Capitalize each word in the text"""
    return ' '.join(word.capitalize() for word in text.split())

# Now we can use the registry to apply transformations
text = "hello python world"
print(f"Original text: {text}")

for name, func in transformation_registry.items():
    transformed = func(text)
    print(f"After {name}: {transformed}")

# ----------------------------------------------------------------------------
# SUMMARY:
# - Functions in Python are first-class objects
# - They can be assigned to variables
# - They can be passed as arguments to other functions
# - They can be returned from functions
# - They can be stored in data structures like lists and dictionaries
# - They can have arbitrary attributes
# - They provide introspection capabilities
# - This flexibility enables powerful programming patterns
# ============================================================================ 