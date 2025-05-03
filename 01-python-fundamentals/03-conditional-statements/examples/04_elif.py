# ============================================================================
# FILENAME: 04_elif.py
# DESCRIPTION: Demonstrates the use of elif (else if) statements in Python
# ============================================================================

# ----------------------------------------------------------------------------
# 1. Basic elif Structure - Multiple Conditions
# ----------------------------------------------------------------------------

print("BASIC ELIF STRUCTURE:")
print("-" * 50)

# The elif statement allows you to check multiple conditions in sequence
# Python checks each condition in order and executes the block for the first
# True condition, then skips all the remaining conditions.

score = 85

# Here we're checking score ranges for grade assignment
if score >= 90:
    grade = "A"
    print(f"Score: {score} → Grade: {grade} (Excellent!)")
elif score >= 80:  # This condition is only checked if the first one is False
    grade = "B"
    print(f"Score: {score} → Grade: {grade} (Good!)")
elif score >= 70:  # This condition is only checked if the first two are False
    grade = "C"
    print(f"Score: {score} → Grade: {grade} (Satisfactory)")
elif score >= 60:  # This condition is only checked if the first three are False
    grade = "D"
    print(f"Score: {score} → Grade: {grade} (Needs Improvement)")
else:  # This block executes if all previous conditions are False
    grade = "F"
    print(f"Score: {score} → Grade: {grade} (Failed)")

print("\n" + "-" * 50 + "\n")

# ----------------------------------------------------------------------------
# 2. Order Matters in elif Chains
# ----------------------------------------------------------------------------

print("ORDER MATTERS IN ELIF CHAINS:")
print("-" * 50)

# The order of conditions in an elif chain is crucial because only the first
# True condition will have its block executed.

age = 25

# Example 1: Correct ordering (from most specific to most general)
print("Example 1: Correct ordering")
if age >= 65:
    print("Senior Citizen")
elif age >= 18:
    print("Adult")
else:
    print("Minor")

# Example 2: Incorrect ordering (problematic)
print("\nExample 2: Incorrect ordering (problematic)")
if age >= 18:
    print("Adult")  # This will execute for all adults, including seniors
elif age >= 65:
    print("Senior Citizen")  # This will never execute because all seniors are >= 18
else:
    print("Minor")

# Example 3: Testing exact values
day_num = 2

print("\nExample 3: Testing exact values")
if day_num == 1:
    day = "Monday"
elif day_num == 2:
    day = "Tuesday"
elif day_num == 3:
    day = "Wednesday"
elif day_num == 4:
    day = "Thursday"
elif day_num == 5:
    day = "Friday"
elif day_num == 6:
    day = "Saturday"
elif day_num == 7:
    day = "Sunday"
else:
    day = "Invalid day number"

print(f"Day number {day_num} is {day}")

print("\n" + "-" * 50 + "\n")

# ----------------------------------------------------------------------------
# 3. Multiple Conditions per elif
# ----------------------------------------------------------------------------

print("MULTIPLE CONDITIONS PER ELIF:")
print("-" * 50)

# You can combine multiple conditions in each part of the if-elif-else chain
# using logical operators (and, or, not)

temp = 28
humidity = 75
is_sunny = True

# Weather advisor with complex conditions
print(f"Temperature: {temp}°C, Humidity: {humidity}%, Sunny: {is_sunny}")

if temp > 30 and humidity > 80:
    print("Weather: Hot and humid! Stay hydrated.")
elif temp > 30 and humidity <= 80:
    print("Weather: Hot but bearable. Wear light clothing.")
elif temp > 20 and is_sunny:
    print("Weather: Warm and sunny. Great day to be outside!")
elif temp > 20 and not is_sunny:
    print("Weather: Warm but not sunny. Good for outdoor activities.")
elif temp > 10:
    print("Weather: Cool. Bring a light jacket.")
else:
    print("Weather: Cold. Wear warm clothing.")

# Example with 'or' conditions - determining transportation method
distance = 5  # distance in kilometers
has_car = True
is_raining = False
public_transport_available = True

print(f"\nTravel info: Distance: {distance}km, Has car: {has_car}, Raining: {is_raining}")

if distance < 1:
    print("Transportation: Walking distance")
elif is_raining and has_car:
    print("Transportation: Better drive due to rain")
elif is_raining and public_transport_available:
    print("Transportation: Take public transport due to rain")
elif distance < 5 and not is_raining:
    print("Transportation: Consider biking or walking")
elif has_car or public_transport_available:
    print("Transportation: Drive or take public transport")
else:
    print("Transportation: Call a taxi")

print("\n" + "-" * 50 + "\n")

# ----------------------------------------------------------------------------
# 4. Comparing elif with match/case (Python 3.10+)
# ----------------------------------------------------------------------------

print("COMPARING ELIF WITH MATCH/CASE:")
print("-" * 50)

# In Python 3.10+, you can use match/case as an alternative to if/elif/else
# for certain types of pattern matching. Here's the comparison:

# Example using if/elif/else for simple value matching
command = "open"

print("Using if/elif/else:")
if command == "quit":
    print("Exiting the program...")
elif command == "open":
    print("Opening file...")
elif command == "save":
    print("Saving file...")
else:
    print(f"Unknown command: {command}")

# The same example using match/case (Python 3.10+)
# Uncomment if using Python 3.10 or newer
'''
print("\nUsing match/case:")
match command:
    case "quit":
        print("Exiting the program...")
    case "open":
        print("Opening file...")
    case "save":
        print("Saving file...")
    case _:  # Default case (like else)
        print(f"Unknown command: {command}")
'''

# match/case is more powerful for pattern matching with complex data
# For simple value checking, if/elif/else works perfectly fine

print("\n" + "-" * 50 + "\n")

# ----------------------------------------------------------------------------
# 5. elif vs. dict-based Dispatching
# ----------------------------------------------------------------------------

print("ELIF VS. DICT-BASED DISPATCHING:")
print("-" * 50)

# For certain types of conditions, especially when checking equality against
# many constant values, a dictionary can be more efficient and cleaner than
# long if/elif chains.

# Example 1: Using if/elif for command handling
command = "help"

print("Using if/elif for commands:")
if command == "quit":
    action = "Exiting the program"
elif command == "help":
    action = "Displaying help information"
elif command == "open":
    action = "Opening a file"
elif command == "save":
    action = "Saving a file"
elif command == "print":
    action = "Printing a document"
else:
    action = f"Unknown command: {command}"

print(action)

# Example 2: Using a dictionary for the same functionality
print("\nUsing a dictionary for commands:")
command_actions = {
    "quit": "Exiting the program",
    "help": "Displaying help information",
    "open": "Opening a file",
    "save": "Saving a file",
    "print": "Printing a document"
}

# Get the action for the command, with a default if not found
action = command_actions.get(command, f"Unknown command: {command}")
print(action)

# Example 3: Dictionary with function values (more advanced)
def quit_action():
    return "Exiting the program"

def help_action():
    return "Displaying help information"

def open_action():
    return "Opening a file"

print("\nUsing a dictionary with functions:")
command_functions = {
    "quit": quit_action,
    "help": help_action,
    "open": open_action
}

# Get and call the function for the command
if command in command_functions:
    action = command_functions[command]()
else:
    action = f"Unknown command: {command}"

print(action)

print("\n" + "-" * 50 + "\n")

# ----------------------------------------------------------------------------
# 6. Real-World Example: State Machine
# ----------------------------------------------------------------------------

print("REAL-WORLD EXAMPLE: STATE MACHINE:")
print("-" * 50)

# Using if/elif/else to implement a simple state machine
# Here we'll simulate a simple turnstile state machine with states:
# - LOCKED: Initial state, waiting for coin
# - UNLOCKED: Turnstile is unlocked, waiting for push
# - BROKEN: Turnstile is out of order

# Possible events: insert_coin, push, fix, break_down

current_state = "LOCKED"
events = ["insert_coin", "push", "push", "break_down", "push", "fix", "insert_coin", "push"]

print(f"Initial state: {current_state}")

for event in events:
    print(f"\nEvent: {event}")
    
    if current_state == "LOCKED":
        if event == "insert_coin":
            current_state = "UNLOCKED"
            print("Turnstile unlocked! You may now push through.")
        elif event == "push":
            current_state = "LOCKED"
            print("Turnstile is locked. Please insert a coin first.")
        elif event == "break_down":
            current_state = "BROKEN"
            print("Turnstile is now broken. Maintenance required.")
        else:
            print("No effect in locked state.")
            
    elif current_state == "UNLOCKED":
        if event == "push":
            current_state = "LOCKED"
            print("Thanks for passing through. Turnstile is now locked again.")
        elif event == "insert_coin":
            current_state = "UNLOCKED"
            print("Coin inserted, but turnstile was already unlocked.")
        elif event == "break_down":
            current_state = "BROKEN"
            print("Turnstile is now broken. Maintenance required.")
        else:
            print("No effect in unlocked state.")
            
    elif current_state == "BROKEN":
        if event == "fix":
            current_state = "LOCKED"
            print("Turnstile has been fixed and is now locked.")
        else:
            print("Turnstile is broken. Please wait for maintenance.")
    
    print(f"Current state: {current_state}")

print("\n" + "-" * 50 + "\n")

# ----------------------------------------------------------------------------
# 7. Common Mistakes with elif
# ----------------------------------------------------------------------------

print("COMMON MISTAKES WITH ELIF:")
print("-" * 50)

# Common mistake 1: Missing colon after the condition
# This would cause a syntax error:
# if x > 0:
#     print("Positive")
# elif x < 0  # Missing colon
#     print("Negative")

# Common mistake 2: Incorrect indentation
x = 5
if x > 0:
    print("x is positive")
    # The following line would normally cause an IndentationError if incorrectly indented
    # print("This line should be indented")

# Common mistake 3: Using = instead of == for comparison
y = 10
if y == 10:  # Correct comparison
    print("y equals 10")
# The following would be incorrect (assignment instead of comparison):
# if y = 10:
#     print("This would cause a syntax error")

# Common mistake 4: Incorrect condition evaluation order
z = 100
print("\nOverlapping conditions with incorrect order:")
if z > 0:
    print("z is positive")  # This will execute
elif z > 50:
    print("z is greater than 50")  # This won't execute even though it's true
elif z > 100:
    print("z is greater than 100")

print("\nFixed order with non-overlapping conditions:")
if z > 100:
    print("z is greater than 100")
elif z > 50:
    print("z is between 51 and 100")  # This will execute
elif z > 0:
    print("z is between 1 and 50")

# Common mistake 5: Redundant conditions
value = 42

# Redundant check
if value == 42:
    print("\nValue is 42")
elif value > 40 and value < 45:
    print("Value is between 41 and 44")  # This won't execute even when true
    
# Better approach with mutually exclusive conditions
if value == 42:
    print("Value is exactly 42")
elif value > 40 and value < 45 and value != 42:
    print("Value is between 41 and 44, but not 42")

print("\n" + "-" * 50 + "\n")

# ----------------------------------------------------------------------------
# SUMMARY:
# - elif allows checking multiple conditions in sequence
# - Only the first matching condition's block will execute
# - The order of conditions is crucial - arrange from most specific to general
# - Complex conditions can be created using logical operators
# - Dictionaries can be alternatives to long if/elif chains for value matching
# - Common mistakes include incorrect syntax, indentation, and condition order
# ============================================================================ 