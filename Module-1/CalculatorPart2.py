# Ask the user to input two numbers
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Perform multiplication
    product = num1 * num2
    print(f"The product of {num1} and {num2} is: {product}")

    # Perform division, handling division by zero
    if num2 == 0:
        print("Division by zero is not allowed.")
    else:
        quotient = num1 / num2
        print(f"The quotient of {num1} divided by {num2} is: {quotient}")

except ValueError:
    print("Invalid input. Please enter numerical values.")

