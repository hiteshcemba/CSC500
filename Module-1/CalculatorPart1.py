# Program for addition and subtraction
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    addition_result = num1 + num2
    subtraction_result = num1 - num2

    print(f"The addition of {num1} and {num2} is: {addition_result}")
    print(f"The subtraction between {num1} and {num2} is: {subtraction_result}")
except ValueError:
    print("Invalid input. Please enter numerical values.")
