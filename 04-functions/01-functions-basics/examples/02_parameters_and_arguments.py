# ============================================================================
# FILENAME: 02_parameters_and_arguments.py
# DESCRIPTION: Demonstrates different ways to pass arguments to functions
# ============================================================================

# ----------------------------------------------------------------------------
# 1. Positional Arguments
# ----------------------------------------------------------------------------

# Define a function with multiple parameters
def display_info(name, age, job):
    """A function that displays personal information using positional parameters"""
    print(f"Name: {name}, Age: {age}, Job: {job}")

# Call the function with positional arguments
# Arguments are matched to parameters by position
display_info("Alice", 30, "Developer")  
# Output: Name: Alice, Age: 30, Job: Developer

# Changing the order changes which parameter receives which value
display_info("Developer", "Alice", 30)  
# Output: Name: Developer, Age: Alice, Job: 30

# ----------------------------------------------------------------------------
# 2. Keyword Arguments
# ----------------------------------------------------------------------------

# Call the same function using keyword arguments
# Arguments are matched to parameters by name
display_info(name="Bob", age=25, job="Designer")
# Output: Name: Bob, Age: 25, Job: Designer

# Keyword arguments can be specified in any order
display_info(job="Engineer", name="Charlie", age=35)
# Output: Name: Charlie, Age: 35, Job: Engineer

# ----------------------------------------------------------------------------
# 3. Mixing Positional and Keyword Arguments
# ----------------------------------------------------------------------------

# Mixing positional and keyword arguments
# Positional arguments must come before keyword arguments
display_info("Dave", job="Manager", age=40)
# Output: Name: Dave, Age: 40, Job: Manager

# This would cause an error - positional after keyword:
# display_info(name="Eve", 28, "Analyst")

# ----------------------------------------------------------------------------
# 4. Variable-Length Positional Arguments (*args)
# ----------------------------------------------------------------------------

# Define a function that accepts a variable number of positional arguments
def add_numbers(*args):
    """A function that adds a variable number of arguments"""
    total = sum(args)
    print(f"Adding {args} gives {total}")
    return total

# Call with different numbers of arguments
add_numbers(1, 2)             # Output: Adding (1, 2) gives 3
add_numbers(1, 2, 3, 4, 5)    # Output: Adding (1, 2, 3, 4, 5) gives 15
add_numbers()                 # Output: Adding () gives 0

# ----------------------------------------------------------------------------
# 5. Variable-Length Keyword Arguments (**kwargs)
# ----------------------------------------------------------------------------

# Define a function that accepts a variable number of keyword arguments
def create_person(**kwargs):
    """A function that creates a person dictionary from keyword arguments"""
    print(f"Creating person with attributes: {kwargs}")
    return kwargs

# Call with different sets of keyword arguments
person1 = create_person(name="Alice", age=30, job="Developer")
# Output: Creating person with attributes: {'name': 'Alice', 'age': 30, 'job': 'Developer'}

person2 = create_person(name="Bob", email="bob@example.com")
# Output: Creating person with attributes: {'name': 'Bob', 'email': 'bob@example.com'}

# ----------------------------------------------------------------------------
# 6. Combining All Argument Types
# ----------------------------------------------------------------------------

# Define a function using all argument types
def master_function(pos1, pos2, *args, kw1="default", kw2="default", **kwargs):
    """A function demonstrating all argument types"""
    print(f"Positional arguments: {pos1}, {pos2}")
    print(f"Variable positional arguments: {args}")
    print(f"Keyword arguments: kw1={kw1}, kw2={kw2}")
    print(f"Variable keyword arguments: {kwargs}")

# Call with a mix of argument types
master_function(
    "first",           # pos1
    "second",          # pos2
    1, 2, 3,           # *args
    kw1="custom",      # kw1
    extra1="value1",   # **kwargs
    extra2="value2"    # **kwargs
)

# Output:
# Positional arguments: first, second
# Variable positional arguments: (1, 2, 3)
# Keyword arguments: kw1=custom, kw2=default
# Variable keyword arguments: {'extra1': 'value1', 'extra2': 'value2'}

# ----------------------------------------------------------------------------
# 7. Unpacking Arguments
# ----------------------------------------------------------------------------

# Define a simple function
def display_point(x, y, z):
    """Display coordinates of a 3D point"""
    print(f"Point coordinates: ({x}, {y}, {z})")

# Create a list/tuple of values
point_list = [1, 2, 3]
point_tuple = (4, 5, 6)

# Unpack the list/tuple into positional arguments using *
display_point(*point_list)   # Output: Point coordinates: (1, 2, 3)
display_point(*point_tuple)  # Output: Point coordinates: (4, 5, 6)

# Create a dictionary of values
point_dict = {"z": 9, "y": 8, "x": 7}

# Unpack the dictionary into keyword arguments using **
display_point(**point_dict)  # Output: Point coordinates: (7, 8, 9)

# ----------------------------------------------------------------------------
# SUMMARY:
# - Positional arguments are matched by position
# - Keyword arguments are matched by name
# - Positional arguments must come before keyword arguments
# - *args collects extra positional arguments into a tuple
# - **kwargs collects extra keyword arguments into a dictionary
# - * unpacks iterables (like lists/tuples) into positional arguments
# - ** unpacks dictionaries into keyword arguments
# ============================================================================ 