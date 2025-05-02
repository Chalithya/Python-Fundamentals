# ============================================================================
# FILENAME: 06_type_conversion.py
# DESCRIPTION: Demonstrating type conversion (type casting) between Python data types
# ============================================================================

# ----------------------------------------------------------------------------
# 1. Converting to Integers (int)
# ----------------------------------------------------------------------------

# String to int conversion
str_num = "42"
int_from_str = int(str_num)  # Converts "42" to 42
print(f"String to int: '{str_num}' → {int_from_str} ({type(int_from_str)})") # Output: String to int: '42' → 42 <class 'int'>

# Float to int conversion (truncates decimal part)
float_num = 7.89
int_from_float = int(float_num)  # Converts 7.89 to 7 (truncates, doesn't round)
print(f"Float to int: {float_num} → {int_from_float} ({type(int_from_float)})") # Output: Float to int: 7.89 → 7 <class 'int'>

# Boolean to int conversion
bool_true = True
bool_false = False
int_from_true = int(bool_true)   # Converts True to 1
int_from_false = int(bool_false) # Converts False to 0
print(f"Boolean to int: {bool_true} → {int_from_true}, {bool_false} → {int_from_false}") # Output: Boolean to int: True → 1, False → 0

# Hexadecimal and binary string to int conversion
hex_str = "0x2A"  # Hexadecimal for 42
int_from_hex = int(hex_str, 16)  # Base 16 (start from index 2 to remove '0x')
bin_str = "0b101010"  # Binary for 42
int_from_bin = int(bin_str, 2)   # Base 2 (start from index 2 to remove '0b')
print(f"Hex to int: {hex_str} → {int_from_hex}")
print(f"Binary to int: {bin_str} → {int_from_bin}")

# Errors in int conversion (commented out to prevent program crash)
# int("hello")  # ValueError: invalid literal for int() with base 10
# int("3.14")   # ValueError: invalid literal for int() with base 10

try:
    invalid = int("hello")
except ValueError as e:
    print(f"Error converting 'hello' to int: {e}")

try:
    invalid = int("3.14")  # This fails - can't directly convert string with decimal
except ValueError as e:
    print(f"Error converting '3.14' to int: {e}")
    # Correct way:
    print(f"Correct way: int(float('3.14')) = {int(float('3.14'))}")
# Output
# Error converting '3.14' to int: invalid literal for int() with base 10: '3.14'
# Correct way: int(float('3.14')) = 3

# ----------------------------------------------------------------------------
# 2. Converting to Floating-point (float)
# ----------------------------------------------------------------------------

# String to float conversion
str_float = "3.14159"
float_from_str = float(str_float)  # Converts "3.14159" to 3.14159
print(f"\nString to float: '{str_float}' → {float_from_str} ({type(float_from_str)})") # Output: String to float: '3.14159' → 3.14159 <class 'float'>

# Integer to float conversion
int_num = 42
float_from_int = float(int_num)  # Converts 42 to 42.0
print(f"Integer to float: {int_num} → {float_from_int} ({type(float_from_int)})") # Output: Integer to float: 42 → 42.0 <class 'float'>

# Boolean to float conversion
float_from_true = float(True)   # Converts True to 1.0
float_from_false = float(False) # Converts False to 0.0
print(f"Boolean to float: {True} → {float_from_true}, {False} → {float_from_false}") # Output: Boolean to float: True → 1.0, False → 0.0

# Scientific notation string to float
sci_notation = "1.23e-4"  # Scientific notation
float_from_sci = float(sci_notation)  # Converts to 0.000123
print(f"Scientific notation to float: '{sci_notation}' → {float_from_sci}") # Output: Scientific notation to float: '1.23e-4' → 0.000123

# Errors in float conversion
try:
    invalid = float("hello")
except ValueError as e:
    print(f"Error converting 'hello' to float: {e}")

# ----------------------------------------------------------------------------
# 3. Converting to Strings (str)
# ----------------------------------------------------------------------------

# Integer to string conversion
num = 42
str_from_int = str(num)  # Converts 42 to "42"
print(f"\nInteger to string: {num} → '{str_from_int}' ({type(str_from_int)})") # Output: Integer to string: 42 → '42' (<class 'str'>)

# Float to string conversion
pi = 3.14159
str_from_float = str(pi)  # Converts 3.14159 to "3.14159"
print(f"Float to string: {pi} → '{str_from_float}' ({type(str_from_float)})") # Output: Float to string: 3.14159 → '3.14159' (<class 'str'>)

# Boolean to string conversion
str_from_true = str(True)   # Converts True to "True"
str_from_false = str(False) # Converts False to "False"
print(f"Boolean to string: {True} → '{str_from_true}', {False} → '{str_from_false}'") # Output: Boolean to string: True → 'True', False → 'False'

# None to string conversion
none_value = None
str_from_none = str(none_value)  # Converts None to "None"
print(f"None to string: {none_value} → '{str_from_none}'") # Output: None to string: None → 'None'

# List, tuple, and dictionary to string
my_list = [1, 2, 3]
my_tuple = (4, 5, 6)
my_dict = {"a": 1, "b": 2}

str_from_list = str(my_list)    # Converts [1, 2, 3] to "[1, 2, 3]"
str_from_tuple = str(my_tuple)  # Converts (4, 5, 6) to "(4, 5, 6)"
str_from_dict = str(my_dict)    # Converts {"a": 1, "b": 2} to "{'a': 1, 'b': 2}"

print(f"List to string: {my_list} → '{str_from_list}'") # Output: List to string: [1, 2, 3] → '[1, 2, 3]'
print(f"Tuple to string: {my_tuple} → '{str_from_tuple}'") # Output: Tuple to string: (4, 5, 6) → '(4, 5, 6)'
print(f"Dictionary to string: {my_dict} → '{str_from_dict}'") # Output: Dictionary to string: {'a': 1, 'b': 2} → "{'a': 1, 'b': 2}"

# ----------------------------------------------------------------------------
# 4. Converting to Booleans (bool)
# ----------------------------------------------------------------------------

# Numeric values to boolean
bool_from_zero = bool(0)       # Converts 0 to False
bool_from_one = bool(1)        # Converts 1 to True
bool_from_neg = bool(-5)       # Converts -5 to True (any non-zero number is True)
print(f"\nNumeric to boolean: 0 → {bool_from_zero}, 1 → {bool_from_one}, -5 → {bool_from_neg}") # Output: Numeric to boolean: 0 → False, 1 → True, -5 → True

# String to boolean
bool_from_empty = bool("")     # Converts empty string to False
bool_from_str = bool("hello")  # Converts non-empty string to True
print(f"String to boolean: '' → {bool_from_empty}, 'hello' → {bool_from_str}") # Output: String to boolean: '' → False, 'hello' → True

# Collections to boolean
bool_from_empty_list = bool([])        # Converts empty list to False
bool_from_list = bool([1, 2, 3])       # Converts non-empty list to True
bool_from_empty_dict = bool({})        # Converts empty dict to False
bool_from_dict = bool({"a": 1})        # Converts non-empty dict to True
print(f"Collections to boolean: [] → {bool_from_empty_list}, [1,2,3] → {bool_from_list}") # Output: Collections to boolean: [] → False, [1,2,3] → True
print(f"Empty dict → {bool_from_empty_dict}, Non-empty dict → {bool_from_dict}") # Output: Empty dict → False, Non-empty dict → True

# None to boolean
bool_from_none = bool(None)    # Converts None to False
print(f"None to boolean: None → {bool_from_none}") # Output: None to boolean: None → False

# ----------------------------------------------------------------------------
# 5. Multiple Conversions and Special Cases
# ----------------------------------------------------------------------------

# Chain of conversions
original = "42.75"
to_float = float(original)     # "42.75" → 42.75
to_int = int(to_float)         # 42.75 → 42
back_to_str = str(to_int)      # 42 → "42"
print(f"\nChain conversion: '{original}' → float({original}) → int({to_float}) → str({to_int}) = '{back_to_str}'")

# Special case: Converting between number systems
decimal = 42
# Convert to different representations
hex_repr = hex(decimal)        # 42 → "0x2a" (hexadecimal)
oct_repr = oct(decimal)        # 42 → "0o52" (octal)
bin_repr = bin(decimal)        # 42 → "0b101010" (binary)

print(f"Number system conversions for {decimal}:")
print(f"Hexadecimal: {hex_repr}")
print(f"Octal: {oct_repr}")
print(f"Binary: {bin_repr}")

# Converting back to decimal
back_from_hex = int(hex_repr, 16)  # "0x2a" → 42
back_from_oct = int(oct_repr, 8)   # "0o52" → 42
back_from_bin = int(bin_repr, 2)   # "0b101010" → 42

print(f"Back to decimal:")
print(f"From hex: {back_from_hex}")
print(f"From octal: {back_from_oct}")
print(f"From binary: {back_from_bin}")

# ----------------------------------------------------------------------------
# 6. Practical Type Conversion Example
# ----------------------------------------------------------------------------

print("\nPractical example: Processing user data")

# Simulating user input (typically strings)
user_age = "25"
user_height = "1.75"
user_is_student = "yes"
user_grades = "85,92,78,95"

# Converting to appropriate types for processing
age = int(user_age)
height = float(user_height)
is_student = user_is_student.lower() in ["yes", "y", "true", "1"]
grades = [int(grade) for grade in user_grades.split(",")]

# Processing data
next_year_age = age + 1
height_in_cm = height * 100
avg_grade = sum(grades) / len(grades)
status = "Student" if is_student else "Non-student"

# Output processed data
print(f"User profile:") # Output: User profile:
print(f"  Age: {age} (next year: {next_year_age})") # Output:   Age: 25 (next year: 26)
print(f"  Height: {height}m ({height_in_cm:.0f}cm)") # Output:   Height: 1.75m (175cm)
print(f"  Status: {status}") # Output:   Status: Student
print(f"  Grades: {grades}") # Output:   Grades: [85, 92, 78, 95]
print(f"  Average Grade: {avg_grade:.1f}") # Output:   Average Grade: 87.5

# ----------------------------------------------------------------------------
# SUMMARY:
# - Type conversion (casting) changes a value from one data type to another
# - Built-in conversion functions:
#   * int() - Convert to integer
#   * float() - Convert to floating-point number
#   * str() - Convert to string
#   * bool() - Convert to boolean
# - Not all conversions are possible; handle potential errors with try/except
# - Numeric conversions follow specific rules:
#   * int() truncates float values (doesn't round)
#   * True converts to 1, False converts to 0
# - Boolean conversion rules:
#   * Numbers: 0 is False, everything else is True
#   * Strings: empty string is False, everything else is True
#   * Collections: empty collections are False, non-empty are True
#   * None is always False
# - Special number system conversions: hex(), oct(), bin()
# - Type conversion is crucial for processing user input and data manipulation
# ============================================================================ 