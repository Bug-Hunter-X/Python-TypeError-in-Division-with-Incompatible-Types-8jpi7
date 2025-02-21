def function_with_uncommon_error(x, y):
    try:
        if isinstance(x,(int,float)) and isinstance(y,(int,float)):
            if y==0:
                raise ZeroDivisionError("Division by zero")
            result = x / y
            return result
        else:
            raise TypeError("Unsupported operand type(s) for / ")
    except ZeroDivisionError as e:
        print(f"Error: {e}")
        return None
    except TypeError as e:
        print(f"Error: {e}")
        return None

# Example usage
print(function_with_uncommon_error(10, 2))  # Output: 5.0
print(function_with_uncommon_error(10, 0))  # Output: Error: Division by zero
print(function_with_uncommon_error(10, "2")) # Output: Error: Unsupported operand type(s) for /
print(function_with_uncommon_error(10, 2.5)) #Output: 4.0
print(function_with_uncommon_error("10",2)) # Output: Error: Unsupported operand type(s) for /