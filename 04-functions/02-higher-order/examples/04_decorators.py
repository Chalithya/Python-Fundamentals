# ============================================================================
# FILENAME: 04_decorators.py
# DESCRIPTION: Demonstrates the concept and usage of decorators in Python
# ============================================================================

import time
import functools

# ----------------------------------------------------------------------------
# 1. Basic Decorator Concept
# ----------------------------------------------------------------------------

# A decorator is a function that takes another function as an argument
# and extends its behavior without explicitly modifying it.

# Simple decorator that prints a message before and after function execution
def simple_decorator(func):
    """A simple decorator that adds messages before and after function execution."""
    
    def wrapper():
        print("Something is happening before the function is called.")
        func()  # Call the original function
        print("Something is happening after the function is called.")
    
    return wrapper

# Apply the decorator to a function
@simple_decorator
def say_hello():
    """A simple function that prints a greeting."""
    print("Hello!")

# Call the decorated function
print("Calling the decorated function:")
say_hello()
print()

# Note: The above is equivalent to:
# say_hello = simple_decorator(say_hello)

# ----------------------------------------------------------------------------
# 2. Decorators with Arguments
# ----------------------------------------------------------------------------

# Decorator for functions with arguments
def decorator_with_args(func):
    """A decorator that works with functions that have arguments."""
    
    def wrapper(*args, **kwargs):
        print(f"Function {func.__name__} called with args: {args} and kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} returned: {result}")
        return result
    
    return wrapper

@decorator_with_args
def add(a, b):
    """Add two numbers."""
    return a + b

# Call the decorated function with arguments
print("Calling a decorated function with arguments:")
result = add(3, 5)
print(f"Result: {result}")
print()

# ----------------------------------------------------------------------------
# 3. Preserving Function Metadata
# ----------------------------------------------------------------------------

# Problem: Decorators hide the original function's metadata
print("Metadata of decorated function without @functools.wraps:")
print(f"Name: {say_hello.__name__}")
print(f"Docstring: {say_hello.__doc__}")
print(f"Module: {say_hello.__module__}")
print()

# Solution: Use functools.wraps to preserve metadata
def better_decorator(func):
    """A decorator that preserves the function's metadata."""
    
    @functools.wraps(func)  # This preserves the metadata of the original function
    def wrapper(*args, **kwargs):
        print("Before function call")
        result = func(*args, **kwargs)
        print("After function call")
        return result
    
    return wrapper

@better_decorator
def multiply(a, b):
    """Multiply two numbers."""
    return a * b

# Check the metadata
print("Metadata of decorated function with @functools.wraps:")
print(f"Name: {multiply.__name__}")
print(f"Docstring: {multiply.__doc__}")
print(f"Module: {multiply.__module__}")
print()

# ----------------------------------------------------------------------------
# 4. Decorators with Parameters
# ----------------------------------------------------------------------------

# Creating a decorator that takes parameters
def repeat(n=1):
    """A decorator that repeats the function call n times."""
    
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(n):
                results.append(func(*args, **kwargs))
            return results
        return wrapper
    
    return decorator

@repeat(n=3)
def greet(name):
    """Greet someone."""
    return f"Hello, {name}!"

# Call the function with a parameter decorator
print("Function with parameterized decorator:")
result = greet("Alice")
print(result)
print()

# ----------------------------------------------------------------------------
# 5. Practical Examples
# ----------------------------------------------------------------------------

# Example 1: Timing Decorator
def timing_decorator(func):
    """Measure the execution time of a function."""
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time:.6f} seconds to run")
        return result
    
    return wrapper

@timing_decorator
def slow_function():
    """A deliberately slow function."""
    time.sleep(1)  # Simulate a slow operation
    return "Done!"

# Test the timing decorator
print("Testing timing decorator:")
slow_function()
print()

# Example 2: Caching Decorator (Memoization)
def memoize(func):
    """Cache the results of a function call to avoid redundant calculations."""
    
    cache = {}
    
    @functools.wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    
    return wrapper

@memoize
def fibonacci(n):
    """Calculate the nth Fibonacci number."""
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Test the memoize decorator
print("Testing memoization decorator:")
start_time = time.time()
result = fibonacci(35)  # This would be very slow without memoization
end_time = time.time()
print(f"Fibonacci(35) = {result}")
print(f"Calculated in {end_time - start_time:.6f} seconds")
print()

# Example 3: Access Control Decorator
def require_auth(func):
    """A decorator that simulates authentication check."""
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Simulate authentication (in a real app, you'd check session, token, etc.)
        is_authenticated = True  # This would come from your auth system
        
        if is_authenticated:
            return func(*args, **kwargs)
        else:
            return "Access denied: Authentication required"
    
    return wrapper

@require_auth
def get_sensitive_data():
    """Return some sensitive data that requires authentication."""
    return "This is sensitive data"

# Test the authentication decorator
print("Testing authentication decorator:")
print(get_sensitive_data())
print()

# ----------------------------------------------------------------------------
# 6. Multiple Decorators
# ----------------------------------------------------------------------------

# Applying multiple decorators to a single function
@timing_decorator
@require_auth
def sensitive_operation():
    """A sensitive operation that we want to time and authenticate."""
    time.sleep(0.5)  # Simulate some work
    return "Sensitive operation completed"

# Test multiple decorators
print("Testing multiple decorators:")
result = sensitive_operation()
print(f"Result: {result}")
print()

# Note: The decorators are applied from bottom to top
# @timing_decorator(@require_auth(sensitive_operation))

# ----------------------------------------------------------------------------
# 7. Class Decorators
# ----------------------------------------------------------------------------

# Using a class as a decorator
class CountCalls:
    """A decorator class that counts the number of times a function is called."""
    
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.count = 0
    
    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"Call #{self.count} to {self.func.__name__}")
        return self.func(*args, **kwargs)

@CountCalls
def say_hi():
    """Say hi."""
    return "Hi!"

# Test class decorator
print("Testing class decorator:")
print(say_hi())
print(say_hi())
print(say_hi())
print(f"Function was called {say_hi.count} times")
print()

# ----------------------------------------------------------------------------
# 8. Real-World Decorators
# ----------------------------------------------------------------------------

# Example: Rate limiting decorator
def rate_limit(max_calls, period):
    """Limit the number of calls to a function in a given period."""
    
    calls = []
    
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            now = time.time()
            
            # Remove calls older than 'period' seconds
            while calls and calls[0] < now - period:
                calls.pop(0)
            
            if len(calls) >= max_calls:
                remaining = calls[0] + period - now
                return f"Rate limit exceeded. Try again in {remaining:.2f} seconds."
            
            calls.append(now)
            return func(*args, **kwargs)
        
        return wrapper
    
    return decorator

@rate_limit(max_calls=3, period=10)
def limited_function():
    """A function with rate limiting."""
    return "Function executed successfully!"

# Test rate limiting (would need to wait in real usage to see the limit)
print("Testing rate limiting decorator:")
for _ in range(5):
    print(limited_function())

# ----------------------------------------------------------------------------
# 9. Decorator Patterns
# ----------------------------------------------------------------------------

# Example: A decorator factory pattern
def log_to(target='console'):
    """A decorator factory that determines where to log."""
    
    def log_to_console(message):
        print(f"LOG: {message}")
    
    def log_to_file(message):
        with open('log.txt', 'a') as f:
            f.write(f"{message}\n")
    
    if target == 'file':
        log_function = log_to_file
    else:
        log_function = log_to_console
    
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            log_function(f"Calling {func.__name__} with {args}, {kwargs}")
            result = func(*args, **kwargs)
            log_function(f"Function {func.__name__} returned {result}")
            return result
        return wrapper
    
    return decorator

@log_to(target='console')
def divide(a, b):
    """Divide a by b."""
    return a / b

# Test logging decorator
print("\nTesting logging decorator:")
result = divide(10, 2)
print(f"Result: {result}")

# ----------------------------------------------------------------------------
# SUMMARY:
# - Decorators are a powerful way to modify or extend the behavior of functions
# - They follow the principle of wrapping one function with another
# - Basic syntax: @decorator before the function definition
# - Decorators can take parameters using decorator factories
# - Use functools.wraps to preserve the metadata of decorated functions
# - Multiple decorators can be stacked
# - Classes can be used as decorators with the __call__ method
# - Practical applications include timing, caching, authentication, and logging
# ============================================================================ 