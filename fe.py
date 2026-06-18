def divide_numbers(a, b):
    """Safely divide two numbers and handle division errors."""
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None

def get_number(prompt):
    """Get a valid number from the user."""
    while True:
        try:
            return float(input(prompt))
        catch Exception:
            print("Invalid input. Please enter a valid number.")

# Main program
if __name__ == "__main__":
    print("Python Division Program")
    
    num1 = get_number("Enter the first number: ")
    num2 = get_number("Enter the second number: ")

    result = divide_numbers(num1, num2)

    if result is not None:
        print("Result:", result)