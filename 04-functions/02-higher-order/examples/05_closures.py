# ============================================================================
# FILENAME: 05_closures.py
# DESCRIPTION: Demonstrates closures in Python (functions that remember their enclosing scope)
# ============================================================================

# ----------------------------------------------------------------------------
# 1. Basic Closure Concept
# ----------------------------------------------------------------------------

# A closure is a function that remembers values in the enclosing scope
# even when the enclosing scope is no longer available for execution.

def outer_function(x):
    """An outer function that defines a variable x"""
    
    # Define an inner function that uses the variable from the outer scope
    def inner_function(y):
        # This inner function has access to the 'x' variable from the outer scope
        return x + y
    
    # Return the inner function
    return inner_function

# Create closures with different values of x
add_5 = outer_function(5)  # Creates a closure where x is 5
add_10 = outer_function(10)  # Creates a closure where x is 10

# Use the closures
print(f"add_5(3) = {add_5(3)}")  # Output: 8 (5 + 3)
print(f"add_10(3) = {add_10(3)}")  # Output: 13 (10 + 3)

# The inner_function "remembers" the value of x from when it was created
print(f"Type of add_5: {type(add_5)}")  # It's a function object

# We can see the closure's value using the __closure__ attribute
print(f"add_5's closure cells: {add_5.__closure__}")
print(f"add_5's closure value: {add_5.__closure__[0].cell_contents}")  # Output: 5
print()

# ----------------------------------------------------------------------------
# 2. Why Closures are Useful
# ----------------------------------------------------------------------------

# Example 1: Creating function factories
def power_function(exponent):
    """Create a function that raises a number to the given exponent."""
    def power(base):
        return base ** exponent
    return power

# Create specific power functions
square = power_function(2)
cube = power_function(3)
square_root = power_function(0.5)

# Use the specific functions
print(f"square(4) = {square(4)}")  # Output: 16
print(f"cube(3) = {cube(3)}")  # Output: 27
print(f"square_root(16) = {square_root(16)}")  # Output: 4.0
print()

# Example 2: Creating a counter with state
def create_counter(start=0):
    """Create a counter function that keeps its state."""
    count = [start]  # Using a list to make the variable mutable in the closure
    
    def increment(step=1):
        count[0] += step
        return count[0]
    
    return increment

# Create counter instances
counter1 = create_counter()
counter2 = create_counter(10)

# Use the counters
print("Counter 1:")
print(counter1())  # Output: 1
print(counter1())  # Output: 2
print(counter1(5))  # Output: 7

print("\nCounter 2:")
print(counter2())  # Output: 11
print(counter2())  # Output: 12
print()

# ----------------------------------------------------------------------------
# 3. Closures vs Classes
# ----------------------------------------------------------------------------

# Sometimes closures can replace simple classes:

# Example using a class
class Counter:
    def __init__(self, start=0):
        self.count = start
    
    def increment(self, step=1):
        self.count += step
        return self.count

# Create object instance
counter_obj = Counter()

# Example using a closure
counter_closure = create_counter()

# Compare the two
print("Class vs Closure:")
print(f"Class: {counter_obj.increment()}")  # Output: 1
print(f"Closure: {counter_closure()}")  # Output: 1 (continuing from above)
print()

# Advantages of closures:
# - More lightweight (no need for class definition)
# - Suitable for simple cases with limited functionality
# - Follows functional programming paradigm

# Advantages of classes:
# - Better for complex data with multiple attributes
# - More explicit interface (methods are named)
# - Better for inheritance and complex behaviors

# ----------------------------------------------------------------------------
# 4. Closures with Multiple Variables
# ----------------------------------------------------------------------------

def create_adder(x, y):
    """Create a function that adds x and y to its argument."""
    def add(z):
        return x + y + z
    return add

# Create a closure with multiple variables
add_8_10 = create_adder(8, 10)
print(f"add_8_10(5) = {add_8_10(5)}")  # Output: 23 (8 + 10 + 5)

# We can inspect all cell contents
print("Multiple closure values:")
for i, cell in enumerate(add_8_10.__closure__):
    print(f"Cell {i}: {cell.cell_contents}")
print()

# ----------------------------------------------------------------------------
# 5. Modifying Variables in Closures
# ----------------------------------------------------------------------------

# In Python 3, nonlocal keyword allows modifying enclosed scope variables

def create_accumulator(initial_value=0):
    """Create a function that accumulates values."""
    total = initial_value
    
    def accumulate(value):
        nonlocal total  # This tells Python we want to modify the outer variable
        total += value
        return total
    
    return accumulate

# Create an accumulator
accumulator = create_accumulator()

# Use the accumulator
print("Accumulator:")
print(accumulator(5))  # Output: 5
print(accumulator(10))  # Output: 15
print(accumulator(2))  # Output: 17
print()

# Without nonlocal, we'd need to use a mutable object like a list
def create_accumulator_without_nonlocal(initial_value=0):
    """Create an accumulator without using nonlocal."""
    total = [initial_value]  # Using a list to make it mutable
    
    def accumulate(value):
        total[0] += value
        return total[0]
    
    return accumulate

# Create another accumulator
old_accumulator = create_accumulator_without_nonlocal()

# Test it
print("Old-style accumulator (using list):")
print(old_accumulator(5))  # Output: 5
print(old_accumulator(10))  # Output: 15
print()

# ----------------------------------------------------------------------------
# 6. Practical Applications
# ----------------------------------------------------------------------------

# Example 1: Memoization (remembering previously computed values)
def create_fibonacci_with_memo():
    """Create a memoized Fibonacci function."""
    # Cache to store already computed values
    memo = {}
    
    def fibonacci(n):
        if n in memo:
            return memo[n]
        
        if n <= 1:
            result = n
        else:
            result = fibonacci(n-1) + fibonacci(n-2)
        
        # Store the result in the cache
        memo[n] = result
        return result
    
    return fibonacci

# Create the memoized function
fib = create_fibonacci_with_memo()

# Test it with a large value
import time
start = time.time()
result = fib(35)
end = time.time()

print(f"Fibonacci(35) = {result}")
print(f"Calculated in {end - start:.6f} seconds (with memoization)")
print()

# Example 2: Configuration functions
def create_formatter(prefix="", suffix="", separator=", "):
    """Create a custom formatter function."""
    def format_list(items):
        formatted = separator.join(str(item) for item in items)
        return f"{prefix}{formatted}{suffix}"
    
    return format_list

# Create different formatters
bullet_list = create_formatter("• ", "", "\n• ")
bracket_list = create_formatter("[", "]", ", ")
quoted_list = create_formatter('"', '"', '", "')

# Test the formatters
items = ["apple", "banana", "cherry"]
print("Bullet list format:")
print(bullet_list(items))

print("\nBracket list format:")
print(bracket_list(items))

print("\nQuoted list format:")
print(quoted_list(items))
print()

# Example 3: Event handlers and callbacks
def create_event_handler(event_type):
    """Create an event handler that remembers its event type."""
    def handler(payload):
        print(f"Handling {event_type} event with payload: {payload}")
        # Process the event based on its type
        if event_type == "click":
            return f"Clicked at coordinates: {payload}"
        elif event_type == "submit":
            return f"Form submitted with data: {payload}"
        else:
            return f"Unknown event with data: {payload}"
    
    return handler

# Create specific event handlers
click_handler = create_event_handler("click")
submit_handler = create_event_handler("submit")

# Simulate events
print("Event handlers:")
print(click_handler({"x": 100, "y": 200}))
print(submit_handler({"name": "John", "email": "john@example.com"}))
print()

# ----------------------------------------------------------------------------
# 7. Closures in Decorators
# ----------------------------------------------------------------------------

# Decorators use closures to wrap functions
def logged(func):
    """A decorator that logs function calls."""
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    
    # The wrapper is a closure that "remembers" the func parameter
    return wrapper

@logged
def add_numbers(a, b):
    """Add two numbers."""
    return a + b

# Test the decorated function
print("Decorator using closures:")
result = add_numbers(3, 5)
print()

# ----------------------------------------------------------------------------
# 8. Potential Issues with Closures
# ----------------------------------------------------------------------------

# Late binding closure - a common issue
def create_multipliers():
    """Create a list of multiplier functions."""
    multipliers = []
    
    # This has a subtle bug due to late binding
    for i in range(1, 4):
        multipliers.append(lambda x: i * x)  # 'i' will be the final value in all functions
    
    return multipliers

# Create the multipliers
multiply_funcs = create_multipliers()

# Test them - they all use the last value of i (3)
print("Late binding issue:")
for multiplier in multiply_funcs:
    print(multiplier(10))  # All will output 30, not 10, 20, 30 as might be expected
print()

# Solution: Use default arguments for immediate binding
def create_multipliers_fixed():
    """Create a list of multiplier functions with correct binding."""
    multipliers = []
    
    for i in range(1, 4):
        # Default argument i=i captures the current value of i
        multipliers.append(lambda x, i=i: i * x)
    
    return multipliers

# Create the fixed multipliers
fixed_multiply_funcs = create_multipliers_fixed()

# Test them - now they work correctly
print("Fixed with immediate binding:")
for multiplier in fixed_multiply_funcs:
    print(multiplier(10))  # Will correctly output 10, 20, 30
print()

# ----------------------------------------------------------------------------
# 9. Memory Management with Closures
# ----------------------------------------------------------------------------

# Closures can lead to memory issues if not used carefully
def create_large_data_processor():
    """Create a function that processes a large dataset."""
    # This large data is kept in memory as long as the returned function exists
    large_data = [i for i in range(1000000)]  # Simulate large data
    
    def process(index):
        if 0 <= index < len(large_data):
            return large_data[index]
        return None
    
    return process

# This will keep the large_data in memory
processor = create_large_data_processor()
print(f"Processor result for index 500: {processor(500)}")

# If memory is a concern, consider other approaches:
# 1. Use classes with __del__ method for cleanup
# 2. Use weakref for weak references
# 3. Explicitly delete references when done

# ----------------------------------------------------------------------------
# SUMMARY:
# - Closures are functions that remember their enclosing scope
# - They're created when a nested function references variables from its containing function
# - Closures are useful for:
#   * Function factories
#   * Maintaining state without classes
#   * Callback functions and event handlers
#   * Implementation of decorators
# - Use nonlocal to modify enclosed variables
# - Be careful of late binding and memory management with closures
# ============================================================================ 