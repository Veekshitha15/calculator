# Simple calculator in Python

def calculator():
    print("Welcome to the simple calculator!")
    print("Operations: +, -, *, /")
    
    try:
        # Get user input for numbers and operation
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter an operation (+, -, *, /): ").strip()

        # Perform the chosen operation
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                return
            result = num1 / num2
        else:
            print("Invalid operation. Please choose from +, -, *, or /.")
            return
        
        # Display the result
        print(f"The result of {num1} {operation} {num2} is: {result}")

    except ValueError:
        print("Invalid input. Please enter numeric values.")

# Run the calculator
calculator()
