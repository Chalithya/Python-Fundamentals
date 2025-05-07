# ============================================================================
# FILENAME: 04_nested_while.py
# DESCRIPTION: Demonstrates nested while loops in Python
# ============================================================================

# ----------------------------------------------------------------------------
# 1. Basic Nested While Loop
# ----------------------------------------------------------------------------

print("BASIC NESTED WHILE LOOPS:")
print("\nExample 1: Simple nested loop")

# Outer loop iterates through rows
row = 1
while row <= 3:
    # Inner loop iterates through columns
    col = 1
    while col <= 3:
        print(f"({row}, {col})", end=" ")
        col += 1
    # After inner loop completes, print a newline
    print()
    row += 1

# ----------------------------------------------------------------------------
# 2. Creating Patterns with Nested Loops
# ----------------------------------------------------------------------------

print("\nExample 2: Creating a triangle pattern")

# Number of rows
rows = 5
i = 1

while i <= rows:
    # Print i asterisks in each row
    j = 1
    while j <= i:
        print("*", end=" ")
        j += 1
    print()
    i += 1

print("\nExample 3: Creating a number triangle pattern")

i = 1
while i <= 5:
    j = 1
    while j <= i:
        print(j, end=" ")
        j += 1
    print()
    i += 1

# ----------------------------------------------------------------------------
# 3. Matrix Operations with Nested Loops
# ----------------------------------------------------------------------------

print("\nExample 4: Processing a 2D matrix")

# Define a 3x3 matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Print matrix in grid format
row = 0
print("Matrix:")
while row < len(matrix):
    col = 0
    while col < len(matrix[row]):
        print(f"{matrix[row][col]:2d}", end=" ")
        col += 1
    print()
    row += 1

# Calculate the sum of all elements in the matrix
row = 0
total = 0
while row < len(matrix):
    col = 0
    while col < len(matrix[row]):
        total += matrix[row][col]
        col += 1
    row += 1

print(f"Sum of all elements: {total}")

# ----------------------------------------------------------------------------
# 4. Nested Loops with Break and Continue
# ----------------------------------------------------------------------------

print("\nExample 5: Nested loops with break")

# Find the first even number in each row and stop processing that row
print("Finding first even number in each row:")

row = 0
while row < len(matrix):
    col = 0
    while col < len(matrix[row]):
        if matrix[row][col] % 2 == 0:
            print(f"Row {row}: Found even number {matrix[row][col]} at column {col}")
            break  # Break inner loop once even number is found
        col += 1
    
    # If no even number found in the row
    if col == len(matrix[row]):
        print(f"Row {row}: No even numbers found")
    
    row += 1

# ----------------------------------------------------------------------------
# SUMMARY:
# - Nested while loops place one loop inside another
# - The inner loop runs completely for each iteration of the outer loop
# - They're useful for working with multi-dimensional data structures like matrices
# - Nested loops can create patterns and process grid-based data
# - Be careful with performance: nested loops multiply the number of iterations
# ============================================================================ 