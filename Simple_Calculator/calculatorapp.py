def calculator():
    # Prompting user for input
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    operation = input("Choose an operator (+, -, *, /): ")

    # Calculation based on the chosen operation
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Error, Division by zero."
    else:
        return "Invalid operation."

    # Displaying the results 
    return f"The result is: {result}"

    # Calling the calculator function
    print(calculator())
  
