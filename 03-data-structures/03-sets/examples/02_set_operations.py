# ============================================================================
# FILENAME: 02_set_operations.py
# DESCRIPTION: Demonstrating mathematical set operations and methods
# ============================================================================

# ----------------------------------------------------------------------------
# 1. Define Sample Sets
# ----------------------------------------------------------------------------

# Sets for demonstrating operations
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
C = {1, 3, 5, 7, 9}

print("Set A:", A)
print("Set B:", B)
print("Set C:", C)
print()

# ----------------------------------------------------------------------------
# 2. Set Union
# ----------------------------------------------------------------------------
# Union: All elements from both sets (no duplicates)

# Using the union() method
union_result = A.union(B)
print("A.union(B):", union_result)

# Using the | operator (more concise)
union_operator_result = A | B
print("A | B:", union_operator_result)

# Union of multiple sets
multi_union = A.union(B, C)
print("Union of A, B, and C:", multi_union)
print("Using operators: A | B | C:", A | B | C)

print()

# ----------------------------------------------------------------------------
# 3. Set Intersection
# ----------------------------------------------------------------------------
# Intersection: Elements that appear in both sets

# Using the intersection() method
intersection_result = A.intersection(B)
print("A.intersection(B):", intersection_result)

# Using the & operator
intersection_operator_result = A & B
print("A & B:", intersection_operator_result)

# Intersection of multiple sets
multi_intersection = A.intersection(B, C)
print("Intersection of A, B, and C:", multi_intersection)
print("Using operators: A & B & C:", A & B & C)

print()

# ----------------------------------------------------------------------------
# 4. Set Difference
# ----------------------------------------------------------------------------
# Difference: Elements in the first set but not in the second

# Using the difference() method
difference_result = A.difference(B)
print("A.difference(B):", difference_result)

# Using the - operator
difference_operator_result = A - B
print("A - B:", difference_operator_result)

# The order matters for difference
reverse_difference = B.difference(A)
print("B.difference(A):", reverse_difference)
print("B - A:", B - A)

# Difference with multiple sets: elements in A but not in B or C
multi_difference = A.difference(B, C)
print("A.difference(B, C):", multi_difference)
print("Using operators: A - B - C:", A - B - C)

print()

# ----------------------------------------------------------------------------
# 5. Symmetric Difference
# ----------------------------------------------------------------------------
# Symmetric Difference: Elements in either set, but not in both

# Using the symmetric_difference() method
symmetric_difference_result = A.symmetric_difference(B)
print("A.symmetric_difference(B):", symmetric_difference_result)

# Using the ^ operator
symmetric_difference_operator_result = A ^ B
print("A ^ B:", symmetric_difference_operator_result)

# Symmetric difference of multiple sets (note: needs to be chained)
multi_symmetric_difference = A ^ B ^ C
print("A ^ B ^ C:", multi_symmetric_difference)
# Note: A.symmetric_difference(B, C) would cause an error

print()

# ----------------------------------------------------------------------------
# 6. Set Comparison Operations
# ----------------------------------------------------------------------------

# Create some sample sets for comparison
X = {1, 2, 3, 4, 5}
Y = {1, 2, 3}
Z = {1, 2, 3, 4, 5, 6}
W = {10, 11, 12}

print("X:", X)
print("Y:", Y)
print("Z:", Z)
print("W:", W)

# Subset check (is Y a subset of X?)
is_subset = Y.issubset(X)
print("\nY.issubset(X):", is_subset)
print("Y <= X:", Y <= X)  # Operator version

# Proper subset (is Y a proper subset of X? - subset but not equal)
proper_subset = Y < X
print("Y < X (proper subset):", proper_subset)

# Superset check (is X a superset of Y?)
is_superset = X.issuperset(Y)
print("\nX.issuperset(Y):", is_superset)
print("X >= Y:", X >= Y)  # Operator version

# Proper superset (is X a proper superset of Y? - superset but not equal)
proper_superset = X > Y
print("X > Y (proper superset):", proper_superset)

# Equality check
print("\nX == Y:", X == Y)  # False
print("X == X:", X == X)  # True

# Disjoint check (do sets have any elements in common?)
are_disjoint = X.isdisjoint(W)
print("\nX.isdisjoint(W):", are_disjoint)  # True - no common elements
print("X.isdisjoint(Y):", X.isdisjoint(Y))  # False - have common elements

print()

# ----------------------------------------------------------------------------
# 7. Modifying Sets with Set Operations
# ----------------------------------------------------------------------------

# Create sets to modify
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("Original set1:", set1)
print("Original set2:", set2)

# Update: Add all elements from another set (union in-place)
set1.update(set2)
print("\nAfter set1.update(set2):", set1)

# Reset the sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Intersection update: Keep only elements found in both sets
set1.intersection_update(set2)
print("\nAfter set1.intersection_update(set2):", set1)

# Reset the sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Difference update: Remove elements found in another set
set1.difference_update(set2)
print("\nAfter set1.difference_update(set2):", set1)

# Reset the sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Symmetric difference update: Keep elements in either set, but not in both
set1.symmetric_difference_update(set2)
print("\nAfter set1.symmetric_difference_update(set2):", set1)

print()

# ----------------------------------------------------------------------------
# 8. Practical Examples
# ----------------------------------------------------------------------------

# Example 1: Finding unique elements
data = [1, 2, 2, 3, 4, 4, 5, 5, 5]
unique_elements = set(data)
print("Original data:", data)
print("Unique elements:", unique_elements)

# Example 2: Finding common elements between lists
list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]
common_elements = set(list1).intersection(set(list2))
print("\nList1:", list1)
print("List2:", list2)
print("Common elements:", common_elements)

# Example 3: Removing common elements (finding unique to each list)
unique_to_list1 = set(list1).difference(set(list2))
unique_to_list2 = set(list2).difference(set(list1))
print("Elements unique to list1:", unique_to_list1)
print("Elements unique to list2:", unique_to_list2)
print("All unique elements (in either but not both):", set(list1) ^ set(list2))

# Example 4: Checking if one group is a subset of another
required_skills = {"Python", "SQL", "Git"}
candidate1_skills = {"Python", "JavaScript", "HTML", "SQL", "Git"}
candidate2_skills = {"Python", "JavaScript"}

print("\nRequired skills:", required_skills)
print("Candidate 1 skills:", candidate1_skills)
print("Candidate 2 skills:", candidate2_skills)

print("Candidate 1 has all required skills:", required_skills.issubset(candidate1_skills))
print("Candidate 2 has all required skills:", required_skills.issubset(candidate2_skills))

# Example 5: Finding missing skills
missing_skills_candidate2 = required_skills.difference(candidate2_skills)
print("Skills candidate 2 is missing:", missing_skills_candidate2)

# ----------------------------------------------------------------------------
# SUMMARY:
# - Set operations allow powerful data manipulation with mathematical precision
# - Union (|): all elements from both sets
# - Intersection (&): elements common to both sets
# - Difference (-): elements in first set but not in second
# - Symmetric Difference (^): elements in either set but not in both
# - Comparison operations: subset, superset, equality, disjointness
# - In-place methods: update, intersection_update, difference_update, etc.
# - Sets are powerful for removing duplicates, finding common elements,
#   and performing other set-based operations
# ============================================================================ 