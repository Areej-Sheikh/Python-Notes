# Implement exception handling for division by zero.
try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    result = a / b
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter numeric values.")


# Implement try-except to handle division by zero.
try:
    num = int(input("Enter numerator: "))
    den = int(input("Enter denominator: "))
    result = num / den
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")


