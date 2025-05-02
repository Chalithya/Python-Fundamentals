# ============================================================================
# FILENAME: 08_python_comments.py
# DESCRIPTION: Demonstration of how to use comments in Python
# ============================================================================

# ----------------------------------------------------------------------------
# 1. Single-line Comments
# ----------------------------------------------------------------------------

# This is a single-line comment in Python
print("Hello World")  # Comments can also appear after code on the same line

# Comments are ignored by the Python interpreter
# print("This line won't execute because it's commented out")

# Single-line comments are useful for:
# - Brief explanations of code
# - Temporarily disabling code (commenting out)
# - Adding reminders or TODOs
# - Explaining complex logic

# TODO: This is a common convention for marking tasks that need to be done
# FIXME: This marks code that needs to be fixed
# NOTE: Used for important notes about the code

# ----------------------------------------------------------------------------
# 2. Multi-line Comments (using multiple # symbols)
# ----------------------------------------------------------------------------

# Python doesn't have a specific multi-line comment syntax like /* */ in some
# other programming languages. Instead, we use multiple single-line comments.
# This is a common way to create longer explanations or documentation
# that spans multiple lines.

# ----------------------------------------------------------------------------
# 3. Docstrings (Documentation Strings)
# ----------------------------------------------------------------------------

# Docstrings are not technically comments, but they serve a similar purpose
# for documenting functions, classes, and modules. They use triple quotes.

def calculate_area(length, width):
    """
    Calculate the area of a rectangle.
    
    Args:
        length (float): The length of the rectangle
        width (float): The width of the rectangle
        
    Returns:
        float: The area of the rectangle
    """
    return length * width

# Accessing the docstring:
print("\nDocstring example:")
print(calculate_area.__doc__)

# You can also use triple quotes for multi-line strings that aren't docstrings
explanation = """
This is a multi-line string.
It's not a comment, but sometimes
it's used for text blocks.
"""
print("\nMulti-line string (not a comment):")
print(explanation)

# ----------------------------------------------------------------------------
# 4. Block Comments for Code Sections
# ----------------------------------------------------------------------------

# === Initialize Program Variables ===
user_name = "Alice"
score = 0
level = 1

# === Main Game Loop ===
print("\nGame Simulation:")
# Simulate a simple game loop
print(f"Welcome, {user_name}!")
print(f"Starting Level: {level}, Score: {score}")

# Update score (this would normally be in a loop)
score += 100  # Add points for completing level
level += 1    # Advance to next level

print(f"Level Complete! New Level: {level}, Score: {score}")

# ----------------------------------------------------------------------------
# 5. Good Comment Practices
# ----------------------------------------------------------------------------

# GOOD: Explain WHY, not WHAT (the code should show what it does)
# Bad example:
x = 0
x = x + 1  # Increment x by 1
# Good example:
attempts = 0
attempts += 1  # Increment the number of attempts after each failed try

# GOOD: Use comments to explain complex logic
def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    
    # If n is divisible by 2 or 3, it's not prime
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    # Check divisibility by numbers of form 6k±1 up to sqrt(n)
    # This is an optimization based on the fact that all primes > 3
    # can be expressed as 6k±1
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
        
    return True

# GOOD: Update comments when you update code
# If code changes but comments don't, the comments become misleading

# ----------------------------------------------------------------------------
# 6. Special Comment Markers
# ----------------------------------------------------------------------------

# These are common conventions used by developers and some tools:

# TODO: Add input validation
# FIXME: This calculation is incorrect for negative numbers
# HACK: Temporary workaround until proper solution is implemented
# XXX: This code is problematic and needs attention
# BUG: Known issue - crashes with empty input
# NOTE: Remember that this function requires setup_environment() to be called first
# REVIEW: This algorithm could be optimized

# ----------------------------------------------------------------------------
# 7. Commenting Style Guidelines
# ----------------------------------------------------------------------------

# PEP 8 (Python's style guide) recommends:
# - Comments should be complete sentences
# - The first word should be capitalized (unless it's an identifier)
# - Use inline comments sparingly
# - Comments should be clear and to the point
# - Ensure comments are up to date with the code they describe

# Example following PEP 8 guidelines:
def connect_to_database(host, port, username, password):
    """
    Establish connection to the database server.
    
    This function attempts to create a secure connection to the specified
    database server and returns a connection object if successful.
    
    Args:
        host (str): Database server hostname or IP
        port (int): Port number to connect on
        username (str): Authentication username
        password (str): Authentication password
        
    Returns:
        Connection: Database connection object or None if connection fails
        
    Raises:
        ConnectionError: If the database server is unreachable
        AuthenticationError: If credentials are invalid
    """
    # Connection implementation would go here
    pass  # 'pass' is a placeholder meaning "do nothing"

# ----------------------------------------------------------------------------
# SUMMARY:
# - Comments help make code more readable and maintainable
# - Single-line comments use the # symbol
# - Multi-line comments use multiple # symbols (one per line)
# - Docstrings (""") document functions, classes, and modules
# - Good comments explain WHY, not WHAT
# - Keep comments up-to-date with code changes
# - Follow PEP 8 guidelines for consistent commenting style
# - Use special markers (TODO, FIXME, etc.) for specific types of notes
# ============================================================================ 