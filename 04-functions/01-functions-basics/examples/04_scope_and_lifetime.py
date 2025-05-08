# ============================================================================
# FILENAME: 04_scope_and_lifetime.py
# DESCRIPTION: Demonstrates variable scope and lifetime in Python functions
# ============================================================================

# ----------------------------------------------------------------------------
# 1. Local Scope
# ----------------------------------------------------------------------------

# Variables defined inside a function are in local scope
def demonstrate_local_scope():
    """Show how local variables work"""
    # This is a local variable
    local_var = "I am local to this function"
    print(local_var)  # This works fine

# Call the function
demonstrate_local_scope()  # Output: I am local to this function

# Try to access the local variable outside the function
# This would cause an error:
# print(local_var)  # NameError: name 'local_var' is not defined

# ----------------------------------------------------------------------------
# 2. Global Scope
# ----------------------------------------------------------------------------

# Variables defined at the module level are in global scope
global_var = "I am a global variable"

def access_global():
    """Access a global variable from inside a function"""
    # We can read global variables inside functions
    print(f"Inside function: {global_var}")

# Call the function
access_global()  # Output: Inside function: I am a global variable

# Access the global variable outside the function
print(f"Outside function: {global_var}")  # Output: Outside function: I am a global variable

# ----------------------------------------------------------------------------
# 3. Modifying Global Variables
# ----------------------------------------------------------------------------

counter = 0

def increment_without_global():
    """Try to modify a global variable without global keyword"""
    # This creates a new local variable instead of modifying the global one
    counter = counter + 1  # This would cause an error
    print(f"Inside function: {counter}")

# The above function would cause: UnboundLocalError: local variable 'counter' 
# referenced before assignment

# Use the global keyword to modify global variables
def increment_with_global():
    """Modify a global variable using the global keyword"""
    global counter
    counter = counter + 1
    print(f"Inside function: {counter}")

# Call the function
increment_with_global()  # Output: Inside function: 1
print(f"Outside function: {counter}")  # Output: Outside function: 1

# Call again to see the change persists
increment_with_global()  # Output: Inside function: 2
print(f"Outside function: {counter}")  # Output: Outside function: 2

# ----------------------------------------------------------------------------
# 4. Enclosing Scope (Nested Functions)
# ----------------------------------------------------------------------------

def outer_function():
    """Demonstrate enclosing scope with a nested function"""
    # This variable is in the enclosing scope of the inner function
    enclosing_var = "I am in the enclosing scope"
    
    def inner_function():
        """Access variables from the enclosing scope"""
        # We can access variables from the enclosing scope
        print(f"Inner function accessing: {enclosing_var}")
    
    # Call the inner function
    inner_function()  # Output: Inner function accessing: I am in the enclosing scope
    
    # The enclosing variable is still accessible here
    print(f"Outer function accessing: {enclosing_var}")

# Call the outer function
outer_function()

# The enclosing variable is not accessible outside the outer function
# print(enclosing_var)  # This would cause an error

# ----------------------------------------------------------------------------
# 5. The nonlocal Keyword
# ----------------------------------------------------------------------------

def counter_function():
    """Demonstrate the nonlocal keyword for modifying enclosing variables"""
    count = 0
    
    def increment():
        """Increment the counter from the enclosing scope"""
        nonlocal count
        count += 1
        print(f"Counter is now: {count}")
    
    # Call the inner function multiple times
    increment()  # Output: Counter is now: 1
    increment()  # Output: Counter is now: 2
    increment()  # Output: Counter is now: 3
    
    # The change is visible in the enclosing scope
    print(f"Final counter: {count}")  # Output: Final counter: 3

# Call the function
counter_function()

# ----------------------------------------------------------------------------
# 6. Variable Lifetime
# ----------------------------------------------------------------------------

def demonstrate_lifetime():
    """Show how variable lifetime works"""
    # Local variables are created when the function is called
    life_var = "I am alive!"
    print(life_var)
    # Local variables are destroyed when the function exits

# Call the function multiple times - a new local variable is created each time
demonstrate_lifetime()  # Output: I am alive!
demonstrate_lifetime()  # Output: I am alive!

# ----------------------------------------------------------------------------
# 7. The LEGB Rule (Lookup order)
# ----------------------------------------------------------------------------

# Python follows the LEGB rule for variable lookup:
# Local -> Enclosing -> Global -> Built-in

# Global variable
x = "global x"

def outer():
    """Demonstrate the LEGB rule with a nested function"""
    # Enclosing variable
    x = "enclosing x"
    
    def inner():
        # Local variable
        x = "local x"
        print(f"inner x: {x}")  # Looks up local first
    
    inner()  # Output: inner x: local x
    print(f"outer x: {x}")  # Looks up enclosing

outer()  # Prints: inner x: local x, outer x: enclosing x
print(f"global x: {x}")  # Output: global x: global x

# ----------------------------------------------------------------------------
# 8. Built-in Scope
# ----------------------------------------------------------------------------

# Built-in functions like print, len, etc. are in the built-in scope

def demonstrate_builtin_scope():
    """Show how built-in functions can be accessed and overridden"""
    # We can access built-in functions
    print(len("Hello"))  # Output: 5
    
    # We can override built-in names (not recommended)
    len = "Not a function anymore"
    print(len)  # Output: Not a function anymore
    
    # The original built-in is not accessible locally now
    # print(len("Hello"))  # This would cause a TypeError

# Call the function
demonstrate_builtin_scope()

# The global built-in is still accessible outside the function
print(len("Hello, world!"))  # Output: 13

# ----------------------------------------------------------------------------
# SUMMARY:
# - Local scope: Variables defined inside a function
# - Enclosing scope: Variables in outer functions (for nested functions)
# - Global scope: Variables defined at the module level
# - Built-in scope: Python's built-in functions and names
# - The 'global' keyword allows modifying global variables from a function
# - The 'nonlocal' keyword allows modifying enclosing variables
# - Python uses the LEGB rule (Local, Enclosing, Global, Built-in) for lookup
# - Variable lifetime is tied to scope: locals exist only during function execution
# ============================================================================ 