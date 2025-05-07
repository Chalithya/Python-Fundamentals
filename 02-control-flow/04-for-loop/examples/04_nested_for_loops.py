# ============================================================================
# FILENAME: 04_nested_for_loops.py
# DESCRIPTION: Demonstrates nested for loops in Python
# ============================================================================

# ----------------------------------------------------------------------------
# 1. Basic Nested Loops
# ----------------------------------------------------------------------------

print("BASIC NESTED LOOPS:")

# Simple 2D grid pattern
print("\nSimple 2D grid (3x3):")
for i in range(3):
    for j in range(3):
        print(f"({i},{j})", end=" ")
    print()  # newline after each row

# Creating a multiplication table
print("\nMultiplication table (1-5):")
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i*j:2d}", end=" ")
    print()

# ----------------------------------------------------------------------------
# 2. Pattern Printing
# ----------------------------------------------------------------------------

print("\nPATTERN PRINTING:")

# Right triangle pattern
print("\nRight triangle pattern:")
rows = 5
for i in range(rows):
    for j in range(i + 1):
        print("*", end=" ")
    print()

# Inverted right triangle pattern
print("\nInverted right triangle pattern:")
for i in range(rows, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

# Pyramid pattern
print("\nPyramid pattern:")
for i in range(rows):
    # Print spaces
    for j in range(rows - i - 1):
        print(" ", end="")
    # Print stars
    for k in range(2 * i + 1):
        print("*", end="")
    print()

# ----------------------------------------------------------------------------
# 3. Working with Nested Data Structures
# ----------------------------------------------------------------------------

print("\nWORKING WITH NESTED DATA STRUCTURES:")

# Nested lists (matrices)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("\nIterating over a matrix:")
for row in matrix:
    for element in row:
        print(f"{element:2d}", end=" ")
    print()

# Accessing by indices
print("\nAccessing matrix by indices:")
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(f"matrix[{i}][{j}] = {matrix[i][j]}")

# Flattening a matrix
print("\nFlattening a matrix:")
flattened = []
for row in matrix:
    for element in row:
        flattened.append(element)
print(flattened)

# Flattening with list comprehension (more Pythonic)
flattened_comp = [element for row in matrix for element in row]
print(f"Flattened with comprehension: {flattened_comp}")

# Working with dictionaries of lists
student_grades = {
    "Alice": [85, 90, 92],
    "Bob": [78, 80, 75],
    "Charlie": [95, 92, 90]
}

print("\nIterating over a dictionary of lists:")
for student, grades in student_grades.items():
    print(f"{student}'s grades:", end=" ")
    for grade in grades:
        print(grade, end=" ")
    # Calculate average
    average = sum(grades) / len(grades)
    print(f"(Average: {average:.1f})")

# ----------------------------------------------------------------------------
# 4. Nested Loop with Conditionals
# ----------------------------------------------------------------------------

print("\nNESTED LOOPS WITH CONDITIONALS:")

# Filter even numbers within ranges
print("\nFilter even numbers from multiple ranges:")
for i in range(3):
    base = i * 10
    print(f"Even numbers in range {base+1}-{base+10}:", end=" ")
    for j in range(base + 1, base + 11):
        if j % 2 == 0:
            print(j, end=" ")
    print()

# Finding prime numbers
print("\nPrime numbers up to 30:")
for num in range(2, 31):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")
print()

# ----------------------------------------------------------------------------
# 5. Nested Loop Control
# ----------------------------------------------------------------------------

print("\nNESTED LOOP CONTROL:")

# Using break in nested loops
print("\nUsing break in nested loops:")
for i in range(5):
    print(f"Outer loop: {i}")
    for j in range(5):
        print(f"  Inner loop: {j}", end="")
        if j == 2:
            print(" - Breaking inner loop")
            break
        print()
    
# Labels and nested loops (Python doesn't have built-in labeled breaks)
print("\nEmulating labeled breaks:")
found = False
print("Searching for value 5 in a matrix:")
for i in range(len(matrix)):
    if found:
        break
    for j in range(len(matrix[i])):
        if matrix[i][j] == 5:
            print(f"Found 5 at position [{i}][{j}]")
            found = True
            break

# Alternative approach using functions
print("\nUsing functions for cleaner breaks:")
def find_value(matrix, value):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == value:
                return (i, j)  # Return position when found
    return None  # Return None if not found

position = find_value(matrix, 8)
if position:
    print(f"Found 8 at position {position}")

# ----------------------------------------------------------------------------
# 6. Performance Considerations
# ----------------------------------------------------------------------------

print("\nPERFORMANCE CONSIDERATIONS:")

# Nested loops can be computationally expensive
print("\nNested loop efficiency:")
print("Number of iterations in various nested loops:")

small_size = 10
print(f"Two nested loops (10×10): {small_size * small_size} iterations")
print(f"Three nested loops (10×10×10): {small_size * small_size * small_size} iterations")

# Optimizing nested loops (example)
print("\nOptimization example:")
print("Instead of:")
print("for i in range(n):")
print("    for j in range(n):")
print("        for k in range(n):")
print("            # O(n³) operation")
print("\nConsider alternatives like:")
print("# Precompute results where possible")
print("# Use NumPy operations for matrix/vector operations")
print("# Use list comprehensions or generator expressions")
print("# Consider algorithmic improvements to reduce complexity")

# ----------------------------------------------------------------------------
# 7. Real-world Examples
# ----------------------------------------------------------------------------

print("\nREAL-WORLD EXAMPLES:")

# Image processing (simulated)
print("\nSimulated image processing (3×3 pixel grid):")
image = [
    [0, 128, 255],
    [128, 200, 128],
    [255, 128, 0]
]

print("Original pixel values:")
for row in image:
    for pixel in row:
        print(f"{pixel:3d}", end=" ")
    print()

# Apply a transformation (invert colors)
print("\nInverted pixel values:")
for i in range(len(image)):
    for j in range(len(image[i])):
        # Invert color (255 - original value)
        inverted = 255 - image[i][j]
        print(f"{inverted:3d}", end=" ")
    print()

# Coordinate system traversal (e.g., game board)
print("\nTraversing a chess-like board:")
for row in range(8, 0, -1):  # Rows 8 down to 1
    for col in "abcdefgh":    # Columns a through h
        print(f"{col}{row}", end=" ")
    print()

# ----------------------------------------------------------------------------
# SUMMARY:
# - Nested loops allow iteration through multi-dimensional data structures
# - They're essential for 2D grids, matrices, and complex data structures
# - Control flow (break, continue) can be used with care in nested loops
# - Performance can degrade quickly with multiple levels of nesting
# - Consider optimization techniques for deeply nested loops
# - Real-world applications include image processing, game development,
#   data analysis, and matrix operations
# ============================================================================ 