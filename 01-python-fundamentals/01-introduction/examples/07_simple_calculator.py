# ============================================================================
# FILENAME: 07_first_complete_program.py
# DESCRIPTION: A simple calculator implementing the four basic operations
# ============================================================================

def display_welcome():
    """Display welcome message and instructions"""
    print("=" * 50)
    print("WELCOME TO THE PYTHON CALCULATOR")
    print("=" * 50)
    print("This program performs basic arithmetic operations:")
    print("  1. Addition (+)")
    print("  2. Subtraction (-)")
    print("  3. Multiplication (*)")
    print("  4. Division (/)")
    print("=" * 50)

def get_numbers():
    """Get two numbers from the user"""
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        return num1, num2
    except ValueError:
        print("Error: Please enter valid numbers.")
        return get_numbers()  # Recursively try again

def get_operation():
    """Get the desired operation from the user"""
    print("\nSelect an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    choice = input("\nEnter your choice (1-4): ")
    
    if choice in ["1", "2", "3", "4"]:
        return choice
    else:
        print("Invalid choice. Please select a number between 1 and 4.")
        return get_operation()  # Recursively try again

def perform_calculation(num1, num2, operation):
    """Perform the selected calculation and return the result"""
    if operation == "1":  # Addition
        result = num1 + num2
        symbol = "+"
    elif operation == "2":  # Subtraction
        result = num1 - num2
        symbol = "-"
    elif operation == "3":  # Multiplication
        result = num1 * num2
        symbol = "*"
    elif operation == "4":  # Division
        if num2 == 0:
            return "Error: Cannot divide by zero!"
        result = num1 / num2
        symbol = "/"
    
    # Format result for better display (avoid trailing zeros for integers)
    if result == int(result):
        result = int(result)
    
    return f"{num1} {symbol} {num2} = {result}"

def ask_continue():
    """Ask if the user wants to perform another calculation"""
    response = input("\nDo you want to perform another calculation? (y/n): ")
    return response.lower() in ["y", "yes"]

def main():
    """Main program function that coordinates the calculator"""
    display_welcome()
    
    while True:
        # Get input values
        num1, num2 = get_numbers()
        operation = get_operation()
        
        # Calculate and display result
        result = perform_calculation(num1, num2, operation)
        print("\nRESULT:")
        print(result)
        
        # Check if user wants to continue
        if not ask_continue():
            break
    
    print("\nThank you for using the Python Calculator! Goodbye!")

# This conditional checks if the file is being run directly (not imported)
if __name__ == "__main__":
    main()

# ============================================================================
# EXPLANATION:
#
# This program demonstrates a complete Python application that:
#
# 1. Uses functions to organize code into logical sections
# 2. Implements error handling with try/except
# 3. Takes user input and performs validation
# 4. Does calculations based on user choices
# 5. Formats output appropriately
# 6. Uses a loop to allow multiple calculations
# 7. Uses the if __name__ == "__main__" pattern for proper script execution
#
# Program Flow:
# - Welcome message is displayed
# - User enters two numbers
# - User selects an operation
# - Calculation is performed and result displayed
# - User can choose to continue or exit
# - When done, a goodbye message is displayed
# 
# Key Concepts Demonstrated:
# - Function definitions and docstrings
# - User input and type conversion
# - Decision making with if/elif/else
# - Error handling with try/except
# - Recursion for input validation
# - String formatting
# - Conditional script execution
# ============================================================================ 