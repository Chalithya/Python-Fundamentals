# ============================================================================
# FILENAME: 06_nested_conditionals.py
# DESCRIPTION: Demonstrates how to use nested conditional statements in Python
# ============================================================================

"""
This module demonstrates the usage of nested conditional statements in Python.
Nested conditionals are if-statements that contain other if-statements within 
their blocks, allowing for more complex decision making.

While nested conditionals are powerful, they can quickly become hard to read
if there are too many levels of nesting. This module shows both good and bad
practices for implementing nested conditionals.
"""

# ----------------------------------------------------------------------------
# 1. Basic Nested Conditional Syntax
# ----------------------------------------------------------------------------

# A simple nested conditional example
age = 25
has_license = True

print("Driving eligibility check:")
if age >= 18:
    print("✓ Age requirement met: You are 18 or older.")
    
    if has_license:
        print("✓ License requirement met: You have a driver's license.")
        print("You are legally allowed to drive.")
    else:
        print("✗ License requirement not met: You don't have a driver's license.")
        print("You cannot legally drive until you get a license.")
else:
    print("✗ Age requirement not met: You must be at least 18 years old.")
    print("You cannot legally drive yet.")

# ----------------------------------------------------------------------------
# 2. Multiple Levels of Nesting (Be Careful With This)
# ----------------------------------------------------------------------------

# A more complex nested conditional example (weather activity recommendation)
temperature = 28
is_raining = False
is_weekend = True

print("\nWeather activity recommendation:")
if is_weekend:
    print("It's the weekend!")
    
    if temperature > 25:
        print("Temperature is warm (above 25°C).")
        
        if is_raining:
            print("But it's raining...")
            print("Recommendation: Indoor swimming or visit a museum.")
        else:
            print("And it's not raining!")
            print("Recommendation: Go to the beach or park.")
    else:
        print("Temperature is cool (25°C or below).")
        
        if is_raining:
            print("And it's raining...")
            print("Recommendation: Watch a movie at home or visit a café.")
        else:
            print("But it's not raining!")
            print("Recommendation: Go hiking or cycling.")
else:
    print("It's a weekday.")
    print("Focus on work/study, check weather later for evening activities.")

# ----------------------------------------------------------------------------
# 3. Refactoring Deeply Nested Conditionals
# ----------------------------------------------------------------------------

# Example of nested conditionals that can be hard to read
def calculate_shipping_bad(country, weight, express):
    """
    Calculate shipping cost based on destination, weight, and delivery speed.
    This example demonstrates a poor implementation with excessive nesting.
    
    Args:
        country (str): Shipping destination country
        weight (float): Package weight in kg
        express (bool): Whether express shipping is requested
        
    Returns:
        float: Calculated shipping cost
    """
    if country == "USA":
        if weight < 1:
            if express:
                cost = 15.0
            else:
                cost = 5.0
        else:
            if express:
                cost = 25.0
            else:
                cost = 10.0
    else:
        if country in ["Canada", "Mexico"]:
            if weight < 1:
                if express:
                    cost = 20.0
                else:
                    cost = 8.0
            else:
                if express:
                    cost = 35.0
                else:
                    cost = 15.0
        else:
            if weight < 1:
                if express:
                    cost = 40.0
                else:
                    cost = 15.0
            else:
                if express:
                    cost = 60.0
                else:
                    cost = 30.0
    
    return cost

# Example usage of the poorly implemented function
shipping_cost = calculate_shipping_bad("USA", 0.5, True)
print(f"\nBadly structured shipping cost calculation: ${shipping_cost}")  # Output: $15.0

# ----------------------------------------------------------------------------
# 4. Better Approach: Early Returns
# ----------------------------------------------------------------------------

def calculate_shipping_better(country, weight, express):
    """
    Calculate shipping cost based on destination, weight, and delivery speed.
    This example demonstrates a better implementation using early returns.
    
    Args:
        country (str): Shipping destination country
        weight (float): Package weight in kg
        express (bool): Whether express shipping is requested
        
    Returns:
        float: Calculated shipping cost
    """
    # USA shipping rates
    if country == "USA":
        if weight < 1 and express:
            return 15.0
        elif weight < 1:
            return 5.0
        elif express:
            return 25.0
        else:
            return 10.0
    
    # Canada and Mexico shipping rates
    if country in ["Canada", "Mexico"]:
        if weight < 1 and express:
            return 20.0
        elif weight < 1:
            return 8.0
        elif express:
            return 35.0
        else:
            return 15.0
    
    # International shipping rates (all other countries)
    if weight < 1 and express:
        return 40.0
    elif weight < 1:
        return 15.0
    elif express:
        return 60.0
    else:
        return 30.0

# Example usage of the better implemented function
shipping_cost = calculate_shipping_better("USA", 0.5, True)
print(f"Better structured shipping cost calculation: ${shipping_cost}")  # Output: $15.0

# ----------------------------------------------------------------------------
# 5. Best Approach: Eliminate Nesting with Helper Functions and Lookup Tables
# ----------------------------------------------------------------------------

def calculate_shipping_best(country, weight, express):
    """
    Calculate shipping cost using a lookup table approach.
    This example demonstrates the best implementation with minimal nesting.
    
    Args:
        country (str): Shipping destination country
        weight (float): Package weight in kg
        express (bool): Whether express shipping is requested
        
    Returns:
        float: Calculated shipping cost
    """
    # Determine region category
    if country == "USA":
        region = "domestic"
    elif country in ["Canada", "Mexico"]:
        region = "neighboring"
    else:
        region = "international"
    
    # Determine weight category
    weight_category = "light" if weight < 1 else "heavy"
    
    # Determine speed category
    speed = "express" if express else "standard"
    
    # Shipping cost lookup table
    shipping_rates = {
        "domestic": {
            "light": {"standard": 5.0, "express": 15.0},
            "heavy": {"standard": 10.0, "express": 25.0}
        },
        "neighboring": {
            "light": {"standard": 8.0, "express": 20.0},
            "heavy": {"standard": 15.0, "express": 35.0}
        },
        "international": {
            "light": {"standard": 15.0, "express": 40.0},
            "heavy": {"standard": 30.0, "express": 60.0}
        }
    }
    
    # Look up the shipping cost
    return shipping_rates[region][weight_category][speed]

# Example usage of the best implemented function
shipping_cost = calculate_shipping_best("USA", 0.5, True)
print(f"Best structured shipping cost calculation: ${shipping_cost}")  # Output: $15.0

# ----------------------------------------------------------------------------
# 6. Using Guard Clauses to Reduce Nesting
# ----------------------------------------------------------------------------

def process_order(item_id, quantity, is_vip=False):
    """
    Process an order with guard clauses to reduce nesting.
    
    Args:
        item_id (str): Product identifier
        quantity (int): Number of items ordered
        is_vip (bool): Whether the customer is a VIP
        
    Returns:
        str: Order status message
    """
    # Guard clause 1: Check for valid item ID
    if not item_id or not isinstance(item_id, str):
        return "Error: Invalid item ID"
    
    # Guard clause 2: Check for valid quantity
    if quantity <= 0:
        return "Error: Quantity must be positive"
    
    # Guard clause 3: Check for inventory availability (simulated)
    inventory = {"ABC123": 10, "XYZ789": 5, "LMN456": 0}
    
    if item_id not in inventory:
        return f"Error: Item {item_id} not found in catalog"
    
    if inventory[item_id] < quantity:
        return f"Error: Not enough inventory. Only {inventory[item_id]} available."
    
    # Process the valid order
    discount = 0.1 if is_vip else 0
    
    # Instead of nested conditionals for VIP processing, 
    # we handle the special cases with guard clauses and
    # then proceed with the "normal" flow
    
    return f"Order processed: {quantity} x {item_id} with {discount*100}% discount"

# Test the function with various inputs
print("\nOrder Processing Examples:")
print(process_order("", 2))            # Output: Error: Invalid item ID
print(process_order("ABC123", 0))      # Output: Error: Quantity must be positive
print(process_order("INVALID", 1))     # Output: Error: Item INVALID not found in catalog
print(process_order("LMN456", 1))      # Output: Error: Not enough inventory. Only 0 available.
print(process_order("ABC123", 5))      # Output: Order processed: 5 x ABC123 with 0.0% discount
print(process_order("ABC123", 5, True))# Output: Order processed: 5 x ABC123 with 10.0% discount

# ----------------------------------------------------------------------------
# 7. Complex Real-World Example: Loan Eligibility
# ----------------------------------------------------------------------------

def check_loan_eligibility(credit_score, annual_income, loan_amount, employment_years):
    """
    Determine if a customer is eligible for a loan.
    
    Args:
        credit_score (int): Customer's credit score (300-850)
        annual_income (float): Annual income in dollars
        loan_amount (float): Requested loan amount in dollars
        employment_years (float): Years at current employer
        
    Returns:
        tuple: (is_eligible, reason, interest_rate)
    """
    # Guard clauses for invalid inputs
    if credit_score < 300 or credit_score > 850:
        return (False, "Invalid credit score", None)
    
    if annual_income <= 0:
        return (False, "Invalid income", None)
    
    if loan_amount <= 0:
        return (False, "Invalid loan amount", None)
    
    if employment_years < 0:
        return (False, "Invalid employment history", None)
    
    # Calculate debt-to-income ratio (DTI)
    # For simplicity, we assume the loan will be paid over 5 years
    monthly_payment = loan_amount / (5 * 12)
    monthly_income = annual_income / 12
    dti_ratio = monthly_payment / monthly_income
    
    # Start with basic eligibility rules
    if credit_score < 580:
        return (False, "Credit score too low", None)
    
    if dti_ratio > 0.43:
        return (False, "Debt-to-income ratio too high", None)
    
    if employment_years < 1:
        return (False, "Employment history too short", None)
    
    # Determine interest rate based on credit score ranges
    if credit_score >= 750:
        interest_rate = 3.5
    elif credit_score >= 700:
        interest_rate = 4.0
    elif credit_score >= 650:
        interest_rate = 4.5
    elif credit_score >= 620:
        interest_rate = 5.0
    else:
        interest_rate = 6.5
    
    # Adjust interest rate based on employment history
    if employment_years >= 5:
        interest_rate -= 0.25
    
    # Adjust interest rate based on income
    if annual_income > 100000:
        interest_rate -= 0.25
    
    return (True, "Approved", interest_rate)

# Test with various applicants
def display_loan_result(applicant_name, credit_score, annual_income, loan_amount, employment_years):
    """
    Display the loan eligibility results for an applicant.
    
    Args:
        applicant_name (str): Name of the applicant
        credit_score (int): Applicant's credit score
        annual_income (float): Applicant's annual income
        loan_amount (float): Requested loan amount
        employment_years (float): Years at current employer
    """
    result = check_loan_eligibility(credit_score, annual_income, loan_amount, employment_years)
    
    print(f"\nLoan Application: {applicant_name}")
    print(f"Credit Score: {credit_score}")
    print(f"Annual Income: ${annual_income:,.2f}")
    print(f"Loan Amount: ${loan_amount:,.2f}")
    print(f"Years Employed: {employment_years}")
    
    if result[0]:
        print(f"Result: {result[1]} at {result[2]}% interest rate")
    else:
        print(f"Result: Declined - {result[1]}")

# Test cases
print("\nLoan Eligibility Test Cases:")
display_loan_result("Alice", 760, 85000, 250000, 6)     # Should be approved
display_loan_result("Bob", 550, 45000, 150000, 2)       # Should be declined
display_loan_result("Charlie", 680, 75000, 350000, 3)   # Likely declined due to DTI
display_loan_result("Diana", 700, 120000, 300000, 7)    # Should be approved

# ----------------------------------------------------------------------------
# SUMMARY:
# - Nested conditionals are if-statements inside other if-statements
# - Deep nesting can make code harder to read and maintain (avoid going beyond 3 levels)
# - Use techniques like early returns, guard clauses, and lookup tables to reduce nesting
# - Break complex nested logic into separate helper functions
# - Flatten nested conditionals by combining conditions with logical operators
# - Use named variables for complex conditions to improve readability
# - Consider alternative approaches like dictionaries or polymorphism for complex logic
# ============================================================================ 