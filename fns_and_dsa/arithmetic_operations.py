def perform_operation(num1: float, num2: float, operation: str):
    """
    Performs basic arithmetic operations (add, subtract, multiply, divide) 
    on two numbers based on the operation string provided.

    Args:
        num1 (float): The first numerical operand.
        num2 (float): The second numerical operand.
        operation (str): The operation to perform ('add', 'subtract', 
                         'multiply', or 'divide').

    Returns:
        float or str: The result of the operation as a float, or a 
                      string message if division by zero occurs.
    """
    
    # Use match case for clear operation handling
    match operation.lower():
        case 'add':
            return num1 + num2
        
        case 'subtract':
            return num1 - num2
        
        case 'multiply':
            return num1 * num2
        
        case 'divide':
            # Check for division by zero before attempting the operation
            if num2 == 0:
                # The checker expects a specific string for the error message
                return "Error: Cannot divide by zero"
            return num1 / num2
        
        case _:
            # Handle cases where the operation string is not recognized
            return "Error: Invalid operation"
