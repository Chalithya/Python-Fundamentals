# ============================================================================
# FILENAME: 05_documentation_and_best_practices.py
# DESCRIPTION: Demonstrates function documentation and best practices in Python
# ============================================================================

# ----------------------------------------------------------------------------
# 1. Function Documentation (Docstrings)
# ----------------------------------------------------------------------------

def simple_docstring():
    """This is a simple one-line docstring."""
    pass

def google_style_docstring(param1, param2, optional_param='default'):
    """Summary line of what the function does.
    
    Extended description of the function's purpose and behavior.
    Multiple paragraphs are supported.
    
    Args:
        param1 (int): Description of param1
        param2 (str): Description of param2
        optional_param (str, optional): Description of optional parameter.
            Defaults to 'default'.
    
    Returns:
        bool: Description of the return value
        
    Raises:
        ValueError: If param1 is negative
        TypeError: If param2 is not a string
    
    Examples:
        >>> google_style_docstring(1, 'test')
        True
        >>> google_style_docstring(2, 'test', 'custom')
        True
    """
    if param1 < 0:
        raise ValueError("param1 must be positive")
    if not isinstance(param2, str):
        raise TypeError("param2 must be a string")
    
    # Function implementation
    return True

def numpy_style_docstring(x, y):
    """
    Calculate the sum of two arrays.
    
    Parameters
    ----------
    x : array_like
        First input array
    y : array_like
        Second input array
        
    Returns
    -------
    ndarray
        The sum of `x` and `y`
        
    Notes
    -----
    This is just an example of NumPy style documentation.
    """
    return x + y

def sphinx_style_docstring(name, age):
    """Return a greeting message.
    
    :param name: The person's name
    :type name: str
    :param age: The person's age
    :type age: int
    :return: A greeting message
    :rtype: str
    :raises ValueError: If age is negative
    """
    if age < 0:
        raise ValueError("Age cannot be negative")
    return f"Hello {name}, you are {age} years old."

# ----------------------------------------------------------------------------
# 2. Accessing Documentation
# ----------------------------------------------------------------------------

# Getting help on functions
if __name__ == "__main__":
    print("Help for google_style_docstring:")
    print(help(google_style_docstring))
    
    # Access the docstring directly
    print("\nAccessing docstring directly:")
    print(simple_docstring.__doc__)

# ----------------------------------------------------------------------------
# 3. Function Naming Conventions
# ----------------------------------------------------------------------------

# Good naming conventions
def calculate_area(length, width):
    """Calculate the area of a rectangle."""
    return length * width

def is_prime(number):
    """Check if a number is prime."""
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def get_user_info():
    """Retrieve user information."""
    # Implementation
    return {"name": "User", "age": 30}

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5 / 9

# Bad naming conventions (commented out)
# def area(l, w):  # Too vague and uses single-letter parameters
#     return l * w
#
# def check(n):  # Too vague
#     # Implementation
#     pass
#
# def doStuff():  # Not snake_case and vague
#     # Implementation
#     pass

# ----------------------------------------------------------------------------
# 4. Function Parameter Best Practices
# ----------------------------------------------------------------------------

# Good parameter design
def create_user(username, email, password, is_admin=False, login_count=0):
    """Create a new user account.
    
    Args:
        username (str): The user's username
        email (str): The user's email address
        password (str): The user's password
        is_admin (bool, optional): Whether the user is an admin. Defaults to False.
        login_count (int, optional): Initial login count. Defaults to 0.
    
    Returns:
        dict: The created user object
    """
    # Implementation
    return {
        "username": username,
        "email": email,
        "password": password,  # In reality, this should be hashed
        "is_admin": is_admin,
        "login_count": login_count
    }

# Using None as default for mutable parameters
def add_to_list(item, item_list=None):
    """Add an item to a list, creating the list if needed.
    
    Args:
        item: The item to add
        item_list (list, optional): The list to add to. Defaults to None.
    
    Returns:
        list: The updated list
    """
    if item_list is None:
        item_list = []
    item_list.append(item)
    return item_list

# Bad parameter practices (commented out)
# def process(data, l=[]):  # Using mutable default parameter
#     l.append(data)
#     return l
#
# def complex_function(a, b, c, d, e, f, g, h):  # Too many parameters
#     # Implementation
#     pass

# ----------------------------------------------------------------------------
# 5. Function Size and Complexity
# ----------------------------------------------------------------------------

# Good: Small, focused function
def validate_email(email):
    """Validate an email address format.
    
    Args:
        email (str): The email to validate
        
    Returns:
        bool: True if valid, False otherwise
    """
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

# Good: Breaking complex tasks into smaller functions
def calculate_statistics(numbers):
    """Calculate statistical measures for a list of numbers.
    
    Args:
        numbers (list): List of numbers
        
    Returns:
        dict: Dictionary with statistical measures
    """
    return {
        "mean": calculate_mean(numbers),
        "median": calculate_median(numbers),
        "range": calculate_range(numbers),
        "variance": calculate_variance(numbers)
    }

def calculate_mean(numbers):
    """Calculate the mean of a list of numbers."""
    return sum(numbers) / len(numbers)

def calculate_median(numbers):
    """Calculate the median of a list of numbers."""
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 0:
        return (sorted_numbers[n//2 - 1] + sorted_numbers[n//2]) / 2
    else:
        return sorted_numbers[n//2]

def calculate_range(numbers):
    """Calculate the range of a list of numbers."""
    return max(numbers) - min(numbers)

def calculate_variance(numbers):
    """Calculate the variance of a list of numbers."""
    mean = calculate_mean(numbers)
    return sum((x - mean) ** 2 for x in numbers) / len(numbers)

# ----------------------------------------------------------------------------
# 6. Function Return Values
# ----------------------------------------------------------------------------

# Good: Consistent return values
def find_user(user_id):
    """Find a user by ID.
    
    Args:
        user_id (int): The user ID to find
        
    Returns:
        dict or None: User dict if found, None otherwise
    """
    # Simulated database lookup
    users = {
        1: {"name": "Alice", "email": "alice@example.com"},
        2: {"name": "Bob", "email": "bob@example.com"}
    }
    
    return users.get(user_id)  # Returns None if not found

# Good: Using named tuples for multiple return values
def get_dimensions():
    """Get dimensions of something.
    
    Returns:
        namedtuple: A named tuple with width, height, and depth
    """
    from collections import namedtuple
    Dimensions = namedtuple('Dimensions', ['width', 'height', 'depth'])
    return Dimensions(width=10, height=20, depth=30)

# ----------------------------------------------------------------------------
# 7. Error Handling in Functions
# ----------------------------------------------------------------------------

def divide(a, b):
    """Divide a by b.
    
    Args:
        a (float): Numerator
        b (float): Denominator
        
    Returns:
        float: Result of division
        
    Raises:
        ZeroDivisionError: If b is zero
        TypeError: If inputs are not numbers
    """
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Both inputs must be numbers")
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

# Graceful error handling
def safe_divide(a, b):
    """Safely divide a by b, returning None if it fails.
    
    Args:
        a (float): Numerator
        b (float): Denominator
        
    Returns:
        float or None: Result of division or None if it fails
    """
    try:
        return divide(a, b)
    except (ZeroDivisionError, TypeError) as e:
        print(f"Error: {e}")
        return None

# ----------------------------------------------------------------------------
# 8. Comment Usage
# ----------------------------------------------------------------------------

def complex_algorithm(data):
    """Implement a complex algorithm on the data."""
    # Prepare the data
    processed_data = [x * 2 for x in data]
    
    # Step 1: Calculate the intermediate values
    # This is a crucial step because...
    intermediate = sum(processed_data) / len(processed_data)
    
    # Step 2: Apply the formula (simplified for example)
    # Using the standard formula from...
    result = intermediate ** 2
    
    return result

# ----------------------------------------------------------------------------
# SUMMARY:
# - Use descriptive docstrings to document your functions
# - Follow consistent naming conventions (snake_case for functions)
# - Design parameters carefully, use sensible defaults
# - Avoid mutable default arguments
# - Keep functions small and focused on a single task
# - Return consistent types from functions
# - Handle errors appropriately
# - Use comments to explain why, not what
# ============================================================================ 