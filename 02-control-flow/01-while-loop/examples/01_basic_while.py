# ============================================================================
# FILENAME: 01_basic_while.py
# DESCRIPTION: Demonstrates the fundamentals of while loops in Python
# ============================================================================

# ----------------------------------------------------------------------------
# 1. Basic While Loop
# ----------------------------------------------------------------------------

# A simple while loop that counts from 0 to 4
counter = 0
while counter < 5:
    print(f"Count: {counter}")
    counter += 1  # Don't forget to increment the counter to avoid infinite loop

# Note: The loop stops when counter becomes 5 (condition becomes False)

# ----------------------------------------------------------------------------
# 2. While Loop with Accumulator
# ----------------------------------------------------------------------------

# Using a while loop to sum numbers from 1 to 5
sum_value = 0
i = 1

while i <= 5:
    sum_value += i
    print(f"Added {i}, sum is now {sum_value}")
    i += 1

print(f"Final sum: {sum_value}")  # Output: Final sum: 15

# ----------------------------------------------------------------------------
# 3. Countdown with While Loop
# ----------------------------------------------------------------------------

# Counting down from 5 to 1
countdown = 5
print("Countdown starting...")

while countdown > 0:
    print(countdown)
    countdown -= 1

print("Blast off!")

# ----------------------------------------------------------------------------
# 4. While Loop with Multiple Conditions
# ----------------------------------------------------------------------------

# Loop continues while both conditions are true
number = 1
max_number = 10
sum_threshold = 25
total = 0

while number <= max_number and total < sum_threshold:
    total += number
    print(f"Number: {number}, Running total: {total}")
    number += 1

print(f"Loop ended. Final number: {number-1}, Final total: {total}")

# ----------------------------------------------------------------------------
# SUMMARY:
# - While loops run as long as their condition evaluates to True
# - The condition is checked at the start of each iteration
# - Make sure to modify the condition variable(s) to avoid infinite loops
# - While loops can use complex conditions with multiple variables
# ============================================================================ 