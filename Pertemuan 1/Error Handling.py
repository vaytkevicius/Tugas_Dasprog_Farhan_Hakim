def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None
    except TypeError:
        print("Error: Invalid data types")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
    else:
        return result
    finally:
        print("Division operation complete")
        
# Example usages
print(divide(10, 2)) # Output: 5.0
print(divide(10, 0)) # Output: Error: Division by zero\nDivision operation complete\nNone
print(divide("10", 0)) # Output: Error: Invalid data types\nDivision operation complete\nNone