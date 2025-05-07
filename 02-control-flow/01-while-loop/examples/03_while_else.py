# ============================================================================
# FILENAME: 03_while_else.py
# DESCRIPTION: Demonstrates the while-else construct in Python
# ============================================================================

# ----------------------------------------------------------------------------
# 1. Basic While-Else Example
# ----------------------------------------------------------------------------

print("Basic while-else example:")
counter = 0
while counter < 5:
    print(f"Counter: {counter}")
    counter += 1
else:
    print("Loop completed without a break statement")

# The else block executed because the loop condition became False

# ----------------------------------------------------------------------------
# 2. While-Else with Break
# ----------------------------------------------------------------------------

print("\nWhile-else with a break:")
counter = 0
while counter < 5:
    print(f"Counter: {counter}")
    if counter == 2:
        print("Breaking the loop early")
        break
    counter += 1
else:
    # This will NOT execute because the loop was exited with a break
    print("This message won't be printed")

print("Loop ended")

# ----------------------------------------------------------------------------
# 3. Using While-Else for Search Operations
# ----------------------------------------------------------------------------

print("\nSearch example with while-else:")
numbers = [10, 15, 20, 25, 30]
search_value = 22
index = 0

while index < len(numbers):
    if numbers[index] == search_value:
        print(f"Found {search_value} at index {index}")
        break
    index += 1
else:
    print(f"{search_value} not found in the list")

# Search again with a value that exists in the list
search_value = 25
index = 0

while index < len(numbers):
    if numbers[index] == search_value:
        print(f"Found {search_value} at index {index}")
        break
    index += 1
else:
    print(f"{search_value} not found in the list")

# ----------------------------------------------------------------------------
# 4. While-Else for Validating Conditions
# ----------------------------------------------------------------------------

print("\nValidation example with while-else:")
attempts = 3
password = "secret123"

while attempts > 0:
    user_input = input(f"Enter password ({attempts} attempts left): ")
    if user_input == password:
        print("Access granted!")
        break
    attempts -= 1
else:
    print("Access denied: Too many incorrect attempts")

# ----------------------------------------------------------------------------
# SUMMARY:
# - The 'else' clause in a while loop executes when the loop condition becomes False
# - If the loop exits due to a 'break' statement, the 'else' clause is skipped
# - This structure is useful for search operations to handle "not found" cases
# - While-else provides a cleaner alternative to using flag variables
# - It's a unique Python feature not found in many other programming languages
# ============================================================================ 