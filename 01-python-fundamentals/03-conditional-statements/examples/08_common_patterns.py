# ============================================================================
# FILENAME: 08_common_patterns.py
# DESCRIPTION: Demonstrates common patterns and idioms for conditional statements in Python
# ============================================================================

"""
This module demonstrates common patterns and idioms for conditional statements
that are frequently used in real-world Python code. Understanding these patterns
will help you write more concise, readable, and effective code.
"""

# ----------------------------------------------------------------------------
# 1. Early Returns Pattern
# ----------------------------------------------------------------------------

def validate_username(username):
    """
    Validate a username against common requirements.
    Demonstrates the early returns pattern.
    
    Args:
        username (str): The username to validate
        
    Returns:
        tuple: (is_valid, error_message)
    """
    # Check if username is None or empty
    if not username:
        return (False, "Username cannot be empty")
    
    # Check if username is too short
    if len(username) < 3:
        return (False, "Username must be at least 3 characters long")
    
    # Check if username is too long
    if len(username) > 20:
        return (False, "Username cannot exceed 20 characters")
    
    # Check if username contains only allowed characters
    if not username.isalnum() and '_' not in username:
        return (False, "Username can only contain letters, numbers, and underscores")
    
    # If we reach here, the username is valid
    return (True, "Username is valid")

# Test the early returns pattern
print("Early Returns Pattern:")
print(validate_username(""))           # (False, 'Username cannot be empty')
print(validate_username("ab"))         # (False, 'Username must be at least 3 characters long')
print(validate_username("a" * 25))     # (False, 'Username cannot exceed 20 characters')
print(validate_username("user@name"))  # (False, 'Username can only contain letters, numbers, and underscores')
print(validate_username("user_123"))   # (True, 'Username is valid')

# ----------------------------------------------------------------------------
# 2. Default Value Pattern
# ----------------------------------------------------------------------------

def get_config_value(config, key, default=None):
    """
    Get a value from a configuration dictionary with a default fallback.
    Demonstrates the default value pattern.
    
    Args:
        config (dict): Configuration dictionary
        key (str): Key to look up
        default: Default value if key is not found
        
    Returns:
        The value associated with the key, or the default value
    """
    if key in config:
        return config[key]
    else:
        return default

# Test the default value pattern
print("\nDefault Value Pattern:")
app_config = {
    "debug": True,
    "port": 8080,
    "log_level": "INFO"
}

debug_mode = get_config_value(app_config, "debug", False)
port = get_config_value(app_config, "port", 5000)
host = get_config_value(app_config, "host", "localhost")
log_level = get_config_value(app_config, "log_level", "WARNING")

print(f"Debug Mode: {debug_mode}")       # Debug Mode: True
print(f"Port: {port}")                   # Port: 8080
print(f"Host: {host}")                   # Host: localhost
print(f"Log Level: {log_level}")         # Log Level: INFO

# Modern Python approach (using dict.get() method)
debug_mode = app_config.get("debug", False)
port = app_config.get("port", 5000)
host = app_config.get("host", "localhost")

print(f"Using dict.get(): Host = {host}")  # Using dict.get(): Host = localhost

# ----------------------------------------------------------------------------
# 3. Chain of Responsibility Pattern
# ----------------------------------------------------------------------------

def process_payment(payment_method, amount):
    """
    Process a payment through different payment processors.
    Demonstrates the chain of responsibility pattern.
    
    Args:
        payment_method (str): The payment method to use
        amount (float): The amount to charge
        
    Returns:
        str: Result of the payment processing
    """
    # Try to process with credit card
    if payment_method == "credit_card":
        return f"Processed ${amount:.2f} with credit card"
    
    # Try to process with PayPal
    elif payment_method == "paypal":
        return f"Processed ${amount:.2f} with PayPal"
    
    # Try to process with store credit
    elif payment_method == "store_credit":
        return f"Processed ${amount:.2f} with store credit"
    
    # Try to process with gift card
    elif payment_method == "gift_card":
        return f"Processed ${amount:.2f} with gift card"
    
    # Default fallback
    else:
        return f"Cannot process ${amount:.2f}: unsupported payment method '{payment_method}'"

# Test the chain of responsibility pattern
print("\nChain of Responsibility Pattern:")
print(process_payment("credit_card", 99.95))  # Processed $99.95 with credit card
print(process_payment("paypal", 59.99))       # Processed $59.99 with PayPal
print(process_payment("bitcoin", 199.99))     # Cannot process $199.99: unsupported payment method 'bitcoin'

# ----------------------------------------------------------------------------
# 4. State Machine Pattern
# ----------------------------------------------------------------------------

def process_order(order):
    """
    Process an order based on its current state.
    Demonstrates a simple state machine pattern.
    
    Args:
        order (dict): The order to process
        
    Returns:
        dict: The updated order
    """
    current_state = order["status"]
    
    # State: New
    if current_state == "new":
        order["status"] = "payment_pending"
        order["notes"].append("Order created and waiting for payment")
    
    # State: Payment Pending
    elif current_state == "payment_pending":
        if order["payment_received"]:
            order["status"] = "preparing"
            order["notes"].append("Payment received, preparing order")
        else:
            order["notes"].append("Payment reminder sent")
    
    # State: Preparing
    elif current_state == "preparing":
        order["status"] = "shipping"
        order["notes"].append("Order prepared and ready for shipping")
    
    # State: Shipping
    elif current_state == "shipping":
        if order["delivered"]:
            order["status"] = "completed"
            order["notes"].append("Order delivered and completed")
        else:
            order["notes"].append("Shipping update: order in transit")
    
    # State: Completed
    elif current_state == "completed":
        order["notes"].append("Order already completed, no action needed")
    
    # State: Cancelled
    elif current_state == "cancelled":
        order["notes"].append("Order is cancelled, no further processing")
    
    # Unknown state
    else:
        order["notes"].append(f"Error: Unknown order status '{current_state}'")
    
    return order

# Test the state machine pattern
print("\nState Machine Pattern:")
# Create a new order
my_order = {
    "id": "ORD-12345",
    "status": "new",
    "items": ["Product A", "Product B"],
    "payment_received": False,
    "delivered": False,
    "notes": []
}

# Process the order through different states
my_order = process_order(my_order)
print(f"Order status: {my_order['status']}")
print(f"Notes: {my_order['notes'][-1]}")

# Update payment and process again
my_order["payment_received"] = True
my_order = process_order(my_order)
print(f"Order status: {my_order['status']}")
print(f"Notes: {my_order['notes'][-1]}")

# Process the preparing order
my_order = process_order(my_order)
print(f"Order status: {my_order['status']}")
print(f"Notes: {my_order['notes'][-1]}")

# ----------------------------------------------------------------------------
# 5. Toggle Flag Pattern
# ----------------------------------------------------------------------------

def update_feature_flags(user, feature_flags):
    """
    Update feature flags for a user based on certain conditions.
    Demonstrates the toggle flag pattern.
    
    Args:
        user (dict): User information
        feature_flags (dict): Current feature flag settings
        
    Returns:
        dict: Updated feature flag settings
    """
    # Copy the current flags
    updated_flags = feature_flags.copy()
    
    # Enable dark mode for premium users or those who explicitly enabled it
    updated_flags["dark_mode"] = user["is_premium"] or feature_flags["dark_mode"]
    
    # Enable beta features for developers or premium users who opted in
    updated_flags["beta_features"] = (user["is_developer"] or 
                                     (user["is_premium"] and user["beta_opted_in"]))
    
    # Enable notifications based on user preferences
    updated_flags["notifications"] = user["notification_preferences"]["enabled"]
    
    # Disable high-load features for mobile users unless they're premium
    if user["device_type"] == "mobile" and not user["is_premium"]:
        updated_flags["high_load_features"] = False
    
    # Always enable essential features
    updated_flags["essential_features"] = True
    
    return updated_flags

# Test the toggle flag pattern
print("\nToggle Flag Pattern:")
# User profile
user_profile = {
    "username": "jane_doe",
    "is_premium": True,
    "is_developer": False,
    "beta_opted_in": True,
    "device_type": "desktop",
    "notification_preferences": {
        "enabled": True,
        "email": True,
        "push": False
    }
}

# Default feature flags
default_flags = {
    "dark_mode": False,
    "beta_features": False,
    "notifications": True,
    "high_load_features": True,
    "essential_features": True
}

# Update the flags based on user profile
user_flags = update_feature_flags(user_profile, default_flags)

# Display the results
print("Default flags:")
for feature, enabled in default_flags.items():
    print(f"  {feature}: {'✓' if enabled else '✗'}")

print("\nUser-specific flags:")
for feature, enabled in user_flags.items():
    print(f"  {feature}: {'✓' if enabled else '✗'}")

# ----------------------------------------------------------------------------
# 6. Null Object Pattern
# ----------------------------------------------------------------------------

class User:
    """A standard user with profile information."""
    
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.is_guest = False
    
    def get_display_name(self):
        """Get the display name for the user."""
        return self.name
    
    def can_access_feature(self, feature):
        """Check if the user can access a specific feature."""
        restricted_features = ["admin", "analytics"]
        return feature not in restricted_features
    
    def get_email_for_notifications(self):
        """Get the email for sending notifications."""
        return self.email

class GuestUser:
    """A null object representing a guest user."""
    
    def __init__(self):
        self.user_id = "guest"
        self.name = "Guest"
        self.email = None
        self.is_guest = True
    
    def get_display_name(self):
        """Get the display name for the guest user."""
        return "Guest User"
    
    def can_access_feature(self, feature):
        """Check if the guest can access a specific feature."""
        allowed_features = ["browse", "search", "view_public"]
        return feature in allowed_features
    
    def get_email_for_notifications(self):
        """Get the email for sending notifications (none for guests)."""
        return None

def get_user(user_id):
    """
    Get a user by ID. Demonstrates the null object pattern.
    Returns a GuestUser if the user is not found.
    
    Args:
        user_id (str): The user ID to look up
        
    Returns:
        User or GuestUser: The found user or a guest user
    """
    # Simulate a user database
    users = {
        "user123": User("user123", "John Doe", "john@example.com"),
        "user456": User("user456", "Jane Smith", "jane@example.com"),
    }
    
    # Return the user if found, otherwise return a guest user
    return users.get(user_id, GuestUser())

# Test the null object pattern
print("\nNull Object Pattern:")
# Get a registered user
john = get_user("user123")
print(f"User: {john.get_display_name()}")
print(f"Can access 'search': {john.can_access_feature('search')}")
print(f"Can access 'admin': {john.can_access_feature('admin')}")
print(f"Email for notifications: {john.get_email_for_notifications()}")

# Get a non-existent user (returns a GuestUser)
unknown = get_user("nonexistent")
print(f"\nUser: {unknown.get_display_name()}")
print(f"Is guest: {unknown.is_guest}")
print(f"Can access 'search': {unknown.can_access_feature('search')}")
print(f"Can access 'admin': {unknown.can_access_feature('admin')}")
print(f"Email for notifications: {unknown.get_email_for_notifications()}")

# ----------------------------------------------------------------------------
# 7. Factory Pattern with Conditionals
# ----------------------------------------------------------------------------

def create_shape(shape_type, **kwargs):
    """
    Create a shape object based on the specified type.
    Demonstrates the factory pattern with conditionals.
    
    Args:
        shape_type (str): The type of shape to create
        **kwargs: Additional parameters for the shape
        
    Returns:
        dict: A shape object with appropriate properties
    """
    # Create a circle
    if shape_type == "circle":
        if "radius" not in kwargs:
            raise ValueError("Radius is required for circles")
        
        radius = kwargs["radius"]
        return {
            "type": "circle",
            "radius": radius,
            "area": 3.14159 * radius * radius,
            "perimeter": 2 * 3.14159 * radius
        }
    
    # Create a rectangle
    elif shape_type == "rectangle":
        if "width" not in kwargs or "height" not in kwargs:
            raise ValueError("Width and height are required for rectangles")
        
        width = kwargs["width"]
        height = kwargs["height"]
        return {
            "type": "rectangle",
            "width": width,
            "height": height,
            "area": width * height,
            "perimeter": 2 * (width + height)
        }
    
    # Create a square (special case of rectangle)
    elif shape_type == "square":
        if "side" not in kwargs:
            raise ValueError("Side length is required for squares")
        
        side = kwargs["side"]
        return {
            "type": "square",
            "side": side,
            "area": side * side,
            "perimeter": 4 * side
        }
    
    # Create a triangle
    elif shape_type == "triangle":
        if "a" not in kwargs or "b" not in kwargs or "c" not in kwargs:
            raise ValueError("Three sides (a, b, c) are required for triangles")
        
        a = kwargs["a"]
        b = kwargs["b"]
        c = kwargs["c"]
        perimeter = a + b + c
        # Heron's formula for triangle area
        s = perimeter / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        
        return {
            "type": "triangle",
            "sides": [a, b, c],
            "area": area,
            "perimeter": perimeter
        }
    
    # Unknown shape type
    else:
        raise ValueError(f"Unknown shape type: {shape_type}")

# Test the factory pattern
print("\nFactory Pattern with Conditionals:")
try:
    # Create different shapes
    circle = create_shape("circle", radius=5)
    rectangle = create_shape("rectangle", width=4, height=6)
    square = create_shape("square", side=4)
    triangle = create_shape("triangle", a=3, b=4, c=5)
    
    # Display the shapes
    print(f"Circle: radius={circle['radius']}, area={circle['area']:.2f}")
    print(f"Rectangle: {rectangle['width']}x{rectangle['height']}, area={rectangle['area']}")
    print(f"Square: side={square['side']}, area={square['area']}")
    print(f"Triangle: sides={triangle['sides']}, area={triangle['area']:.2f}")
    
    # Try creating an invalid shape
    # invalid_shape = create_shape("oval", radius=5, width=10)
except ValueError as e:
    print(f"Error: {e}")

# ----------------------------------------------------------------------------
# 8. Command Dispatcher Pattern
# ----------------------------------------------------------------------------

def dispatch_command(command, args):
    """
    Dispatch a command to the appropriate handler.
    Demonstrates the command dispatcher pattern.
    
    Args:
        command (str): The command to execute
        args (dict): Arguments for the command
        
    Returns:
        str: Result of the command execution
    """
    # Define command handlers as a dictionary
    command_handlers = {
        "greet": lambda args: f"Hello, {args.get('name', 'Guest')}!",
        "add": lambda args: f"Result: {args.get('a', 0) + args.get('b', 0)}",
        "subtract": lambda args: f"Result: {args.get('a', 0) - args.get('b', 0)}",
        "multiply": lambda args: f"Result: {args.get('a', 0) * args.get('b', 0)}",
        "divide": lambda args: f"Result: {args.get('a', 0) / args.get('b', 1)}" if args.get('b', 0) != 0 else "Error: Division by zero",
        "help": lambda args: "Available commands: " + ", ".join(command_handlers.keys())
    }
    
    # Look up the command in the handlers dictionary
    if command in command_handlers:
        # Execute the command handler with the provided arguments
        return command_handlers[command](args)
    else:
        # Command not found
        return f"Unknown command: {command}. Type 'help' to see available commands."

# Test the command dispatcher pattern
print("\nCommand Dispatcher Pattern:")
commands = [
    ("greet", {"name": "Alice"}),
    ("add", {"a": 5, "b": 3}),
    ("subtract", {"a": 10, "b": 4}),
    ("multiply", {"a": 2, "b": 6}),
    ("divide", {"a": 20, "b": 4}),
    ("divide", {"a": 10, "b": 0}),
    ("unknown", {}),
    ("help", {})
]

for cmd, args in commands:
    result = dispatch_command(cmd, args)
    print(f"Command '{cmd}': {result}")

# ----------------------------------------------------------------------------
# SUMMARY:
# - Early Returns Pattern: Return from a function as soon as you have a valid result
# - Default Value Pattern: Provide fallback values for missing data
# - Chain of Responsibility Pattern: Process in sequence until one handler succeeds
# - State Machine Pattern: Change behavior based on current state
# - Toggle Flag Pattern: Enable/disable features based on conditions
# - Null Object Pattern: Provide a default object instead of null/None
# - Factory Pattern: Create objects based on specified parameters
# - Command Dispatcher Pattern: Route commands to the appropriate handlers
# - These patterns help write cleaner, more maintainable conditional logic
# ============================================================================ 