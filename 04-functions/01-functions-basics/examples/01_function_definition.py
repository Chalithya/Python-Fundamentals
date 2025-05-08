# ============================================================================
# FILENAME: 01_function_definition.py
# DESCRIPTION: Demonstrates basic function definition and calling in Python
# ============================================================================

# ----------------------------------------------------------------------------
# 1. Basic Function Definition
# ----------------------------------------------------------------------------

# Define a simple function that prints a message
def say_hello():
    """A simple function that prints a greeting"""
    print("Hello, World!")

# Call the function
say_hello()  # Output: Hello, World!

# ----------------------------------------------------------------------------
# 2. Function with Parameters
# ----------------------------------------------------------------------------

# Define a function that accepts a parameter
def greet(name):
    """A function that greets a person by name"""
    print(f"Hello, {name}!")

# Call the function with an argument
greet("Alice")  # Output: Hello, Alice!
greet("Bob")    # Output: Hello, Bob!

# ----------------------------------------------------------------------------
# 3. Function with Multiple Parameters
# ----------------------------------------------------------------------------

# Define a function with multiple parameters
def describe_person(name, age, job):
    """A function that describes a person using multiple parameters"""
    print(f"{name} is {age} years old and works as a {job}.")

# Call the function with multiple arguments
describe_person("Alice", 30, "Developer")
# Output: Alice is 30 years old and works as a Developer.

# ----------------------------------------------------------------------------
# 4. Function with Default Parameter Values
# ----------------------------------------------------------------------------

# Define a function with default parameter values
def greet_with_default(name="World"):
    """A function with a default parameter value"""
    print(f"Hello, {name}!")

# Call the function without arguments (uses default)
greet_with_default()  # Output: Hello, World!

# Call the function with an argument (overrides default)
greet_with_default("Python Programmer")  # Output: Hello, Python Programmer!

# ----------------------------------------------------------------------------
# 5. Function with Multiple Default Parameters
# ----------------------------------------------------------------------------

# Define a function with multiple default parameters
def create_profile(name, age=25, job="Developer", location="Remote"):
    """A function with multiple default parameters"""
    profile = {
        "name": name,
        "age": age,
        "job": job,
        "location": location
    }
    print(f"Profile created: {profile}")
    return profile

# Call with only required arguments
create_profile("Alice")
# Output: Profile created: {'name': 'Alice', 'age': 25, 'job': 'Developer', 'location': 'Remote'}

# Call with some optional arguments
create_profile("Bob", age=30, location="New York")
# Output: Profile created: {'name': 'Bob', 'age': 30, 'job': 'Developer', 'location': 'New York'}

# ----------------------------------------------------------------------------
# SUMMARY:
# - Functions are defined using the 'def' keyword followed by a name and parentheses
# - Function bodies are indented
# - Functions can accept parameters (variables listed in the function definition)
# - Arguments are values passed to functions when calling them
# - Default parameter values can be specified using the '=' operator
# - Default parameters are used when the caller doesn't provide a value
# ============================================================================ 