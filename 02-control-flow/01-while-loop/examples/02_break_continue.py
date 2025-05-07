# ============================================================================
# FILENAME: 02_break_continue.py
# DESCRIPTION: Demonstrates break and continue statements in while loops
# ============================================================================

# ----------------------------------------------------------------------------
# 1. Using break to Exit a Loop Early
# ----------------------------------------------------------------------------

print("BREAK STATEMENT EXAMPLES:")

# Example 1: Exit when a specific value is found
print("\nExample 1: Finding a number divisible by 7")
number = 1
while number <= 30:
    if number % 7 == 0:
        print(f"Found it! {number} is divisible by 7")
        break  # Exit the loop when the first multiple of 7 is found
    number += 1

# Example 2: Simulating a search with a sentinel value
print("\nExample 2: Searching for a specific value")
data = [10, 25, 32, 8, 16, 42, 85, 99]
target = 42
index = 0

while index < len(data):
    if data[index] == target:
        print(f"Target {target} found at index {index}")
        break  # Exit the loop when the target is found
    index += 1
else:  # This executes if the loop completes without a break
    print(f"Target {target} not found")

# ----------------------------------------------------------------------------
# 2. Using continue to Skip Iterations
# ----------------------------------------------------------------------------

print("\nCONTINUE STATEMENT EXAMPLES:")

# Example 1: Skip even numbers
print("\nExample 1: Processing only odd numbers")
counter = 0
while counter < 10:
    counter += 1
    if counter % 2 == 0:  # If the number is even
        continue  # Skip to the next iteration
    print(f"Processing odd number: {counter}")

# Example 2: Skip values that meet certain criteria
print("\nExample 2: Skip numbers divisible by 3")
number = 0
while number < 20:
    number += 1
    if number % 3 == 0:
        continue  # Skip numbers divisible by 3
    print(f"Processing {number}")

# ----------------------------------------------------------------------------
# 3. Common Patterns Using break and continue
# ----------------------------------------------------------------------------

print("\nCOMMON PATTERNS:")

# Example: Processing user input with validation
print("\nExample: Input validation loop")
print("Enter 'quit' to exit the loop")

while True:  # Infinite loop that relies on break to exit
    user_input = input("Enter a positive number: ")
    
    if user_input.lower() == 'quit':
        print("Exiting the loop")
        break
    
    # Skip non-numeric input
    if not user_input.isdigit():
        print("That's not a number. Try again.")
        continue
    
    number = int(user_input)
    
    # Skip negative numbers (though we already checked with isdigit)
    if number <= 0:
        print("Please enter a positive number. Try again.")
        continue
    
    # Process valid input
    print(f"You entered {number}, and its square is {number**2}")

# ----------------------------------------------------------------------------
# SUMMARY:
# - Use 'break' to exit a loop immediately when a condition is met
# - Use 'continue' to skip the current iteration and move to the next one
# - These statements provide greater control over loop execution
# - 'break' in a while loop prevents the else clause from executing
# - Infinite loops with break conditions are a common pattern for input validation
# ============================================================================ 