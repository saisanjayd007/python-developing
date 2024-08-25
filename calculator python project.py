def calculator():
    print("Simple Calculator cerated by Sanjay")

    # Prompt the user to enter two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Display operation choices
    print("Select operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    # Prompt the user to select an operation
    choice = input("Enter your choice (1/2/3/4): ")

    # Perform the operation based on user choice
    if choice == '1':
        result = num1 + num2
        operation = '+'
    elif choice == '2':
        result = num1 - num2
        operation = '-'
    elif choice == '3':
        result = num1 * num2
        operation = '*'
    elif choice == '4':
        if num2 != 0:
            result = num1 / num2
            operation = '/'
        else:
            print("Error! Division by zero is not allowed.")
            return
    else:
        print("Invalid input! Please select a valid operation.")
        return

    # Display the result
    print(f"The result of {num1} {operation} {num2} is: {result}")

# Run the calculator function
calculator()
