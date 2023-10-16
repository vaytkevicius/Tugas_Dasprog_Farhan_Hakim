def arithmetic_calculator(operator, *args):
    """
    Perform arithmetic operations on the given arguments based on the operator.
    
    Parameters:
        operator (str): Arithmetic operator ('+', '-', '*', '/').
        args (float): Variable number of arguments on which the operation will be performed.
        
    Returns:
        float: Result of the arithmetic operation.
        
    Raises:
        ValueError: If an invalid operator is provided.
        ZeroDivisionError: If division by zero is attempted.
    """
    if operator in ['+', '-', '*', '/']:
        result = args[0]
        for num in args[1:]:
            if operator == '+':
                result += num
            elif operator == '-':
                result -= num
            elif operator == '*':
                result *= num
            elif operator == '/':
                if num == 0:
                    raise ZeroDivisionError("Division by zero is not allowed.")
                result /= num
        return result
    else:
        raise ValueError("Invalid operator. Please use '+', '-', '*', or '/'.")
        

# Example Usage
try:
    print(arithmetic_calculator('+', 1, 2, 3))  # Output: 6 (1 + 2 + 3)
    print(arithmetic_calculator('-', 10, 5, 2))  # Output: 3 (10 - 5 - 2)
    print(arithmetic_calculator('*', 2, 3, 4))  # Output: 24 (2 * 3 * 4)
    print(arithmetic_calculator('/', 10, 2))     # Output: 5 (10 / 2)
    print(arithmetic_calculator('/', 5, 0))      # Output: Error (ZeroDivisionError)
    print(arithmetic_calculator('%', 2, 3, 4))    # Output: Error (ValueError)
except (ValueError, ZeroDivisionError) as e:
    print(f"Error: {e}")