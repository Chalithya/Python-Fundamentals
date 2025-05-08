# Higher-Order Functions in Python

## Overview

Higher-order functions are functions that operate on other functions by taking them as arguments or returning them as results. This module explores Python's functional programming capabilities through higher-order functions, lambda expressions, and related concepts like closures and decorators.

## Key Concepts

1. **Functions as Objects** - Treating functions as first-class objects
2. **Lambda Functions** - Creating small anonymous functions
3. **Map, Filter, and Reduce** - Built-in higher-order functions
4. **Decorators** - Functions that modify other functions
5. **Closures** - Functions that remember their enclosing scope

## Detailed Explanation

### Functions as Objects

In Python, functions are first-class objects, which means they can be:
- Assigned to variables
- Passed as arguments to other functions
- Returned from other functions
- Stored in data structures like lists and dictionaries

```python
def greet(name):
    return f"Hello, {name}!"

# Assigning function to a variable
say_hello = greet

# Using the function through the variable
print(say_hello("Alice"))  # Output: Hello, Alice!

# Functions in data structures
function_list = [greet, len, str.upper]
for func in function_list:
    print(func("Python"))
```

Expected output:
```
Hello, Python!
6
PYTHON
```

Key points:
- Functions are objects with attributes
- You can access a function's name with `function.__name__`
- Functions have their own namespace and types

### Lambda Functions

Lambda functions are small anonymous functions defined with the `lambda` keyword:

```python
# Regular function
def square(x):
    return x * x

# Equivalent lambda function
square_lambda = lambda x: x * x

print(square(5))        # Output: 25
print(square_lambda(5)) # Output: 25
```

Lambda functions are useful in scenarios where a small function is needed for a short period:

```python
# Sorting a list of tuples by the second element
pairs = [(1, 'one'), (3, 'three'), (2, 'two')]
sorted_pairs = sorted(pairs, key=lambda pair: pair[1])
print(sorted_pairs)  # Output: [(1, 'one'), (3, 'three'), (2, 'two')]
```

Key points:
- Lambda functions are limited to a single expression
- They cannot contain statements or annotations
- Use regular functions for anything complex
- Lambda functions are powerful when used with higher-order functions

### Map, Filter, and Reduce

Python provides built-in higher-order functions for common operations:

1. **Map**: Applies a function to all items in an iterable

```python
numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x**2, numbers)
print(list(squared))  # Output: [1, 4, 9, 16, 25]

# With multiple iterables
a = [1, 2, 3]
b = [4, 5, 6]
added = map(lambda x, y: x + y, a, b)
print(list(added))    # Output: [5, 7, 9]
```

2. **Filter**: Filters elements from an iterable based on a function

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = filter(lambda x: x % 2 == 0, numbers)
print(list(even))     # Output: [2, 4, 6, 8, 10]
```

3. **Reduce**: Cumulatively applies a function to items of an iterable (from `functools`)

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)        # Output: 120 (1*2*3*4*5)
```

Key points:
- `map()` and `filter()` return iterators, not lists
- List comprehensions often provide a more readable alternative
- `reduce()` is in the `functools` module since Python 3

### Decorators

Decorators are higher-order functions that modify the behavior of other functions:

```python
def timer(func):
    """A decorator that prints the execution time of a function"""
    import time
    
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} executed in {end_time - start_time:.4f} seconds")
        return result
    
    return wrapper

@timer
def slow_function():
    """A function that takes some time to execute"""
    import time
    time.sleep(1)
    return "Done!"

result = slow_function()  # Output: slow_function executed in 1.0011 seconds
```

You can also apply multiple decorators to a single function:

```python
def bold(func):
    def wrapper(*args, **kwargs):
        return f"<b>{func(*args, **kwargs)}</b>"
    return wrapper

def italic(func):
    def wrapper(*args, **kwargs):
        return f"<i>{func(*args, **kwargs)}</i>"
    return wrapper

@bold
@italic
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))  # Output: <b><i>Hello, Alice!</i></b>
```

Key points:
- Decorators are applied from bottom to top
- They're commonly used for timing, logging, authentication, and caching
- The `@functools.wraps` decorator helps preserve the original function's metadata

### Closures

A closure is a function that remembers values from the enclosing scope even after that scope has finished executing:

```python
def counter_factory():
    count = 0
    
    def increment():
        nonlocal count
        count += 1
        return count
    
    return increment

counter = counter_factory()
print(counter())  # Output: 1
print(counter())  # Output: 2
print(counter())  # Output: 3
```

Closures are useful for:
- Creating function factories
- Implementing data hiding and encapsulation
- Preserving state between function calls

```python
def multiplier(factor):
    def multiply(number):
        return number * factor
    return multiply

double = multiplier(2)
triple = multiplier(3)

print(double(5))  # Output: 10
print(triple(5))  # Output: 15
```

Key points:
- The inner function must reference a variable from the outer function
- The outer function must return the inner function
- The `nonlocal` keyword allows modifying variables from the outer scope

## Common Pitfalls

- **Late Binding Closures**: Be careful with loops and closures
  ```python
  # BAD:
  functions = []
  for i in range(3):
      functions.append(lambda: i)
  
  # All functions will use the final value of i
  for f in functions:
      print(f())  # Outputs: 2, 2, 2
      
  # GOOD:
  functions = []
  for i in range(3):
      functions.append(lambda i=i: i)  # Default argument captures current value
  
  for f in functions:
      print(f())  # Outputs: 0, 1, 2
  ```

- **Performance Overhead**: Higher-order functions can introduce overhead
- **Excessive Nesting**: Too many nested functions hurt readability
- **Debugging Difficulty**: Complex higher-order functions can be harder to debug

## Real-world Applications

- **Web Frameworks**: Decorators for routing in Flask and Django
- **Data Processing**: Processing data pipelines with map/filter operations
- **Caching**: Memoization decorators for performance optimization
- **Testing**: Setting up test fixtures and mock objects
- **API Design**: Creating clean, functional interfaces

## Further Reading

- [Python Functional Programming HOWTO](https://docs.python.org/3/howto/functional.html)
- [PEP 3104 – Access to Names in Outer Scopes](https://peps.python.org/pep-3104/)
- [Python Decorators 101](https://realpython.com/primer-on-python-decorators/)
- [Functional Programming in Python](https://docs.python.org/3/library/functional.html) 