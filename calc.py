# Asks the User for the first number, second number, and the operation to be perfomed

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

# Performs the operation based on the user's input
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    # Handles division by zero
    if num2 == 0:
        result = "Error! Division by zero."
    else:
        result = num1 / num2
else:
    result = "Invalid operation"

# Displays the result
print(f"{num1} {operation} {num2} = {result}")
