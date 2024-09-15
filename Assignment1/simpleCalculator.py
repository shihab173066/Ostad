"""
(Project 1) : Simple Calculator
OVERVIEW:
In this assignment, you will develop a basic calculator program using Python. This project
will reinforce fundamental programming concepts including functions, user input,
conditional statements, and error handling. The application will run in the terminal and
should not use any external libraries or frameworks.
TASKS:
1. Function Definitions: Implement functions for the following operations: addition,
subtraction, multiplication, division, and modulus. Each function should take two
arguments, perform the corresponding operation, and return the result.
2. Implement User Input Handling: Prompt the user to select an operation ( e.g. 
1 for Add, 2 for Subtract, 3 for Multiply, 4 for Divide and 5 for Modulus) and input two
numbers. Convert these inputs into appropriate data types for calculations.
3. Conditional Logic: Use ‘if’, ‘elif’, and ‘else’ statements to determine which
arithmetic operation to perform based on user selection.
4. Output Formatting: Display the results in a clear and readable format. Examples:
Addition: 5 + 6 = 11
Division: 5 / 2 = 2.50
5. Error Handling: Include checks to handle division by zero and other potential
errors. Provide informative error messages to guide the user.
SAMPLE INPUT OUTPUT:
Select operation:
1. Add
2. Subtract
3. Multiply
4. Divide
5. Modulus
Enter choice (1/2/3/4/5): 1
Enter first number: 5
Enter second number: 8
5.0 + 8.0 = 13.0
"""

# Functions for each options

def add(N1, N2):
    return N1 + N2

def subtract(N1, N2):
    return N1 - N2

def multiply(N1, N2):
    return N1 * N2

def divide(N1, N2):
    if N2 == 0:
        return "Error: Division by zero is undefined."
    return N1 / N2

def modulus(N1, N2):
    if N2 == 0:
        return "Error: Modulus by zero is undefined."
    return N1 % N2

# Calculator Function
def calculator():
    # Display available operations
    print("""
          Welcome to Shihab's Calculator!
          Please select any of the following option -
          """)
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")

    # Get the user's choice and numbers
    select = input("Enter choice {1 OR 2 OR 3 OR 4 OR 5}: ")

    # Verify the choice is valid
    if select not in ['1', '2', '3', '4', '5']:
        print("Invalid choice. Please select a valid operation.")
        return calculator()

    try:
        Number1 = float(input("Enter 1st number: "))
        Number2 = float(input("Enter 2nd number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return calculator()

    # Perform the operation based on the user's choice
    if select == '1':
        result = add(Number1, Number2)
        print(f"{Number1} + {Number2} = {result}")
    elif select == '2':
        result = subtract(Number1, Number2)
        print(f"{Number1} - {Number2} = {result}")
    elif select == '3':
        result = multiply(Number1, Number2)
        print(f"{Number1} * {Number2} = {result}")
    elif select == '4':
        result = divide(Number1, Number2)
        print(f"{Number1} / {Number2} = {result}")
    elif select == '5':
        result = modulus(Number1, Number2)
        print(f"{Number1} % {Number2} = {result}")

    # Ask if the user wants to perform another calculation
    again = input("Do you want to perform another calculation? (y / or any character button): ").lower()
    if again == 'y':
        return calculator()
    else:
        print("Program Ended!")

# Start the calculator
calculator()



