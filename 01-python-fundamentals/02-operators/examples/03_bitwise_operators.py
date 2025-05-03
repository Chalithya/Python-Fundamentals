# ============================================================================
# FILENAME: 03_bitwise_operators.py
# DESCRIPTION: Demonstrates the use of bitwise operators in Python
# ============================================================================

# ----------------------------------------------------------------------------
# 1. Binary Representation Basics
# ----------------------------------------------------------------------------

# This function helps us visualize binary representations
def show_binary(n, bits=8):
    """Show binary representation of a number with a specified bit width"""
    binary = bin(n)[2:]  # Convert to binary and remove '0b' prefix
    # Pad with leading zeros to match specified bit width
    padded = binary.zfill(bits)
    return f"{n} = {padded} (binary)"

# Let's look at some binary representations
print("Binary Representations:")
for num in [0, 1, 2, 5, 10, 15, 255]:
    print(show_binary(num))

print("\n" + "-" * 50 + "\n")

# ----------------------------------------------------------------------------
# 2. Bitwise AND Operator (&)
# ----------------------------------------------------------------------------

# Bitwise AND performs a logical AND operation on each pair of bits
# If both bits are 1, the result is 1; otherwise, it's 0

a = 60  # 00111100 in binary
b = 13  # 00001101 in binary

# Bitwise AND operation
result = a & b  # 00001100 in binary (12 in decimal)

print("Bitwise AND (&):")
print(show_binary(a))
print(show_binary(b))
print(f"a & b = {show_binary(result)}")

# Common uses of bitwise AND:
# 1. Checking if a bit is set (1)
# 2. Masking (extracting specific bits)

# Example: Check if the 3rd bit (from right) is set in number 10
num = 10  # 00001010 in binary
mask = 4  # 00000100 in binary (bit at position 3)
is_bit_set = (num & mask) > 0
print(f"\nIs the 3rd bit set in {num}? {is_bit_set}")

# Example: Extract the last 4 bits of a number
num = 171  # 10101011 in binary
mask = 0x0F  # 00001111 in binary (last 4 bits)
extracted = num & mask
print(f"Last 4 bits of {num}: {show_binary(extracted, 4)}")

print("\n" + "-" * 50 + "\n")

# ----------------------------------------------------------------------------
# 3. Bitwise OR Operator (|)
# ----------------------------------------------------------------------------

# Bitwise OR performs a logical OR operation on each pair of bits
# If either bit is 1, the result is 1; otherwise, it's 0

a = 60  # 00111100 in binary
b = 13  # 00001101 in binary

# Bitwise OR operation
result = a | b  # 00111101 in binary (61 in decimal)

print("Bitwise OR (|):")
print(show_binary(a))
print(show_binary(b))
print(f"a | b = {show_binary(result)}")

# Common uses of bitwise OR:
# 1. Setting specific bits to 1
# 2. Combining flags or options

# Example: Set the 3rd and 5th bits in number 0
num = 0  # 00000000 in binary
mask = 20  # 00010100 in binary (bits at positions 3 and 5)
with_bits_set = num | mask
print(f"\nSetting bits 3 and 5: {show_binary(with_bits_set)}")

# Example: Combining flags (common in system programming)
# Define flags
READ_PERMISSION = 4    # 00000100
WRITE_PERMISSION = 2   # 00000010
EXECUTE_PERMISSION = 1 # 00000001

# Give read and write permissions
permissions = READ_PERMISSION | WRITE_PERMISSION  # 00000110 (6)
print(f"Read + Write permissions: {show_binary(permissions, 3)}")

# Add execute permission
permissions = permissions | EXECUTE_PERMISSION  # 00000111 (7)
print(f"Read + Write + Execute permissions: {show_binary(permissions, 3)}")

print("\n" + "-" * 50 + "\n")

# ----------------------------------------------------------------------------
# 4. Bitwise XOR Operator (^)
# ----------------------------------------------------------------------------

# Bitwise XOR performs a logical exclusive OR operation on each pair of bits
# If the bits are different, the result is 1; if they're the same, it's 0

a = 60  # 00111100 in binary
b = 13  # 00001101 in binary

# Bitwise XOR operation
result = a ^ b  # 00110001 in binary (49 in decimal)

print("Bitwise XOR (^):")
print(show_binary(a))
print(show_binary(b))
print(f"a ^ b = {show_binary(result)}")

# Common uses of bitwise XOR:
# 1. Toggling bits (flipping 0s to 1s and vice versa)
# 2. Finding bits that differ between two values
# 3. Simple encryption/decryption
# 4. Computing parity

# Example: Toggle specific bits
num = 60   # 00111100 in binary
mask = 15  # 00001111 in binary
toggled = num ^ mask  # Toggle the last 4 bits
print(f"\nToggling last 4 bits of {num}: {show_binary(toggled)}")

# Example: Simple XOR encryption
message = 83  # 01010011 in binary
key = 42      # 00101010 in binary
encrypted = message ^ key
decrypted = encrypted ^ key  # XOR with the same key decrypts

print(f"Original: {show_binary(message)}")
print(f"Key: {show_binary(key)}")
print(f"Encrypted: {show_binary(encrypted)}")
print(f"Decrypted: {show_binary(decrypted)}")

print("\n" + "-" * 50 + "\n")

# ----------------------------------------------------------------------------
# 5. Bitwise NOT Operator (~)
# ----------------------------------------------------------------------------

# Bitwise NOT inverts all the bits of a number (0s become 1s, 1s become 0s)
# In Python, ~n = -(n+1) due to two's complement representation

a = 60  # 00111100 in binary

# Bitwise NOT operation
result = ~a  # 11000011 in binary, but Python represents it as -61

print("Bitwise NOT (~):")
print(show_binary(a))
print(f"~a = {result} (not shown in binary due to two's complement representation)")

# Understanding two's complement:
# In Python, negative numbers are stored using two's complement
# ~n = -n - 1

print(f"~{a} = {~a}")
print(f"-{a} - 1 = {-a - 1}")

# To see the actual bit pattern of ~a for an 8-bit number:
mask_8bit = 0xFF  # 11111111 (8 bits all set to 1)
inverted_8bit = ~a & mask_8bit
print(f"~a (8-bit): {show_binary(inverted_8bit)}")

print("\n" + "-" * 50 + "\n")

# ----------------------------------------------------------------------------
# 6. Left Shift Operator (<<)
# ----------------------------------------------------------------------------

# Left shift moves all bits to the left by a specified number of positions
# New bits on the right are filled with 0s

a = 5  # 00000101 in binary

# Left shift by 1, 2, and 3 positions
result1 = a << 1  # 00001010 in binary (10 in decimal)
result2 = a << 2  # 00010100 in binary (20 in decimal)
result3 = a << 3  # 00101000 in binary (40 in decimal)

print("Left Shift (<<):")
print(show_binary(a))
print(f"a << 1 = {show_binary(result1)}")
print(f"a << 2 = {show_binary(result2)}")
print(f"a << 3 = {show_binary(result3)}")

# Left shift by n is equivalent to multiplying by 2^n
print(f"\n{a} << 1 = {result1} (= {a} × 2^1)")
print(f"{a} << 2 = {result2} (= {a} × 2^2)")
print(f"{a} << 3 = {result3} (= {a} × 2^3)")

# Be careful with large shifts, as they can exceed the integer size
try:
    big_shift = a << 1000  # This might not work as expected
    print(f"a << 1000 = {big_shift}")
except Exception as e:
    print(f"Error with large shift: {e}")

print("\n" + "-" * 50 + "\n")

# ----------------------------------------------------------------------------
# 7. Right Shift Operator (>>)
# ----------------------------------------------------------------------------

# Right shift moves all bits to the right by a specified number of positions
# For positive numbers, new bits on the left are filled with 0s
# For negative numbers, the behavior is implementation-dependent

a = 20  # 00010100 in binary

# Right shift by 1, 2, and 3 positions
result1 = a >> 1  # 00001010 in binary (10 in decimal)
result2 = a >> 2  # 00000101 in binary (5 in decimal)
result3 = a >> 3  # 00000010 in binary (2 in decimal)

print("Right Shift (>>):")
print(show_binary(a))
print(f"a >> 1 = {show_binary(result1)}")
print(f"a >> 2 = {show_binary(result2)}")
print(f"a >> 3 = {show_binary(result3)}")

# Right shift by n is equivalent to integer division by 2^n
print(f"\n{a} >> 1 = {result1} (= {a} ÷ 2^1)")
print(f"{a} >> 2 = {result2} (= {a} ÷ 2^2)")
print(f"{a} >> 3 = {result3} (= {a} ÷ 2^3)")

# Right shift behavior with negative numbers (sign bit is preserved)
negative_num = -20
result_neg = negative_num >> 1
print(f"\n{negative_num} >> 1 = {result_neg}")

print("\n" + "-" * 50 + "\n")

# ----------------------------------------------------------------------------
# 8. Practical Applications of Bitwise Operations
# ----------------------------------------------------------------------------

print("Practical Applications of Bitwise Operations:")

# 1. Fast multiplication and division
num = 25
print(f"{num} × 2 = {num << 1}")  # Multiply by 2
print(f"{num} × 4 = {num << 2}")  # Multiply by 4
print(f"{num} ÷ 2 = {num >> 1}")  # Divide by 2 (integer division)
print(f"{num} ÷ 4 = {num >> 2}")  # Divide by 4 (integer division)

# 2. Finding if a number is even or odd
# If the least significant bit is 0, the number is even; if it's 1, the number is odd
print("\nChecking even/odd:")
for num in [7, 12, 25, 30]:
    is_odd = num & 1  # Extract the last bit
    print(f"{num} is {'odd' if is_odd else 'even'}")

# 3. Swapping variables using XOR (without a temporary variable)
print("\nSwapping variables with XOR:")
x, y = 10, 25
print(f"Before swap: x = {x}, y = {y}")

x = x ^ y  # x now holds x XOR y
y = x ^ y  # y now holds (x XOR y) XOR y = x
x = x ^ y  # x now holds (x XOR y) XOR x = y

print(f"After swap: x = {x}, y = {y}")

# 4. Checking if a number is a power of 2
print("\nChecking if a number is a power of 2:")
for num in [1, 2, 4, 7, 8, 15, 16, 32]:
    # A number is a power of 2 if and only if it has exactly one bit set to 1
    # n & (n-1) clears the rightmost set bit in n
    is_power_of_2 = num > 0 and (num & (num - 1)) == 0
    print(f"{num} is{' ' if is_power_of_2 else ' not '}a power of 2")

# 5. Bitmap operations (setting, clearing, toggling, checking bits)
print("\nBitmap Operations:")
bitmap = 0

# Set bit at position 1 (0-indexed)
bitmap |= (1 << 1)
print(f"After setting bit 1: {show_binary(bitmap, 4)}")

# Set bit at position 3
bitmap |= (1 << 3)
print(f"After setting bit 3: {show_binary(bitmap, 4)}")

# Check if bit at position 2 is set
is_bit2_set = (bitmap & (1 << 2)) != 0
print(f"Is bit 2 set? {is_bit2_set}")

# Check if bit at position 3 is set
is_bit3_set = (bitmap & (1 << 3)) != 0
print(f"Is bit 3 set? {is_bit3_set}")

# Clear bit at position 1
bitmap &= ~(1 << 1)
print(f"After clearing bit 1: {show_binary(bitmap, 4)}")

# Toggle bit at position 3
bitmap ^= (1 << 3)
print(f"After toggling bit 3: {show_binary(bitmap, 4)}")

# Toggle bit at position 3 again
bitmap ^= (1 << 3)
print(f"After toggling bit 3 again: {show_binary(bitmap, 4)}")

# 6. Creating a simple bit field for configuration flags
print("\nUsing Bit Fields for Configuration Flags:")

# Define configuration flags
CONFIG_OPTION_A = 1 << 0  # 00000001
CONFIG_OPTION_B = 1 << 1  # 00000010
CONFIG_OPTION_C = 1 << 2  # 00000100
CONFIG_OPTION_D = 1 << 3  # 00001000

# Create a configuration with options A and C enabled
config = CONFIG_OPTION_A | CONFIG_OPTION_C
print(f"Initial config: {show_binary(config, 4)}")

# Check if option B is enabled
is_option_b_enabled = (config & CONFIG_OPTION_B) != 0
print(f"Is option B enabled? {is_option_b_enabled}")

# Enable option D
config |= CONFIG_OPTION_D
print(f"After enabling option D: {show_binary(config, 4)}")

# Disable option A
config &= ~CONFIG_OPTION_A
print(f"After disabling option A: {show_binary(config, 4)}")

print("\n" + "-" * 50 + "\n")

# ----------------------------------------------------------------------------
# 9. Bitwise Operations with Different Data Types
# ----------------------------------------------------------------------------

print("Bitwise Operations with Different Data Types:")

# 1. Bytes and bytearray objects
# Bitwise operations can be performed on bytes objects (Python 3)
byte1 = bytes([0b10101010])  # Create a bytes object with a single byte
byte2 = bytes([0b11110000])

# To apply bitwise operations on bytes, we need to convert to integers,
# perform the operation, and convert back to bytes
result_and = bytes([byte1[0] & byte2[0]])
result_or = bytes([byte1[0] | byte2[0]])
result_xor = bytes([byte1[0] ^ byte2[0]])

print(f"byte1: {bin(byte1[0])}")
print(f"byte2: {bin(byte2[0])}")
print(f"AND result: {bin(result_and[0])}")
print(f"OR result: {bin(result_or[0])}")
print(f"XOR result: {bin(result_xor[0])}")

# 2. Boolean operations vs. bitwise operations
print("\nBoolean vs. Bitwise Operations:")
# Boolean operations (and, or, not) work with truth values
# Bitwise operations (&, |, ~) work with individual bits

# Boolean operations
print(f"True and False = {True and False}")
print(f"True or False = {True or False}")
print(f"not True = {not True}")

# Similar bitwise operations
print(f"1 & 0 = {1 & 0}")
print(f"1 | 0 = {1 | 0}")
print(f"~1 = {~1}")  # Remember that ~ returns a negative number due to two's complement

print("\n" + "-" * 50 + "\n")

# ----------------------------------------------------------------------------
# 10. Advanced Bit Manipulation Techniques
# ----------------------------------------------------------------------------

print("Advanced Bit Manipulation Techniques:")

# 1. Counting the number of set bits (population count or Hamming weight)
def count_set_bits(n):
    """Count the number of 1's in the binary representation of n"""
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count

for num in [0, 1, 7, 15, 16, 255]:
    print(f"Number of set bits in {num}: {count_set_bits(num)}")

# Python's built-in bin() and count method
print("\nUsing built-in methods:")
for num in [0, 1, 7, 15, 16, 255]:
    # Convert to binary, remove '0b' prefix, count '1's
    count = bin(num).count('1')
    print(f"Number of set bits in {num}: {count}")

# 2. Finding the position of the rightmost set bit
def rightmost_set_bit_position(n):
    """Return position of rightmost set bit (LSB position = 0)"""
    if n == 0:
        return -1  # No bits are set
    position = 0
    while (n & 1) == 0:
        position += 1
        n >>= 1
    return position

print("\nRightmost set bit positions:")
for num in [1, 2, 4, 6, 8, 12, 16]:
    pos = rightmost_set_bit_position(num)
    print(f"Rightmost set bit in {num} ({bin(num)}) is at position {pos}")

# 3. Isolating the rightmost set bit
print("\nIsolating the rightmost set bit:")
for num in [12, 10, 18, 24]:
    # n & (-n) or n & (~n + 1) isolates the rightmost set bit
    rightmost_bit = num & -num
    print(f"For {num} ({bin(num)}), rightmost set bit: {rightmost_bit} ({bin(rightmost_bit)})")

print("\n" + "-" * 50 + "\n")

# ----------------------------------------------------------------------------
# SUMMARY:
# - Bitwise operators work at the bit level with individual bits
# - & (AND): Set bits where both operands have 1s
# - | (OR): Set bits where either operand has 1s
# - ^ (XOR): Set bits where exactly one operand has 1s
# - ~ (NOT): Invert all bits (flips 0s and 1s)
# - << (Left Shift): Move bits left, filling with 0s
# - >> (Right Shift): Move bits right, behavior with sign bit varies
# - Bitwise operations are useful for flag manipulation, optimization,
#   low-level programming, and embedded systems
# - Understanding binary representation is key to effective use
# ============================================================================ 