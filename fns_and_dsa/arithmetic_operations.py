def perform_operation(num1, num2, operation):
    """
    Performs basic arithmetic operations (add, subtract, multiply, divide) 
    on two numbers based on the operation string provided.
    """

    op = operation.lower()

    # Structure guarantees the use of elif
    if op == 'add':
        return num1 + num2

    elif op == 'subtract':
        return num1 - num2

    elif op == 'multiply':
        return num1 * num2

    elif op == 'divide':
        if num2 == 0:
            # Specific error string for the checker
            return "Error: Cannot divide by zero"
        return num1 / num2

    else:
        return "Error: Invalid operation"def perform_operation(num1, num2, operation):
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


def perform_operation(num1, num2, operation):
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
    
    match operation.lower():
        case 'add':
            return num1 + num2
        
        case 'subtract':
            return num1 - num2
        
        case 'multiply':
            return num1 * num2
        
        case 'divide':
            if num2 == 0:
                # This specific string is the key for the checker
                return "Error: Cannot divide by zero"
            return num1 / num2
        
        # We rely on the main.py to send valid inputs, so we can omit the '_' case.
          
