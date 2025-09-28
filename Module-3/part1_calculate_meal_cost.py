def calculate_meal_cost():
    """
    Calculates the total cost of a meal, including tip and sales tax,
    and stores the amounts in a list.
    """
    try:
        food_charge = float(input("Enter the charge for the food: $"))
    except ValueError:
        print("Invalid input. Please enter a numeric value for the food charge.")
        return

    # Constants for tip and tax rates
    TIP_RATE = 0.18
    SALES_TAX_RATE = 0.07

    # Calculate tip and sales tax
    tip_amount = food_charge * TIP_RATE
    sales_tax_amount = food_charge * SALES_TAX_RATE
    total_amount = food_charge + tip_amount + sales_tax_amount

    # Store the amounts in a list
    meal_details = [
        food_charge,
        tip_amount,
        sales_tax_amount,
        total_amount
    ]

    # Display the results
    print("\nMeal Summary:")
    print(f"Food Charge: ${meal_details[0]:.2f}")
    print(f"Tip (18%): ${meal_details[1]:.2f}")
    print(f"Sales Tax (7%): ${meal_details[2]:.2f}")
    print(f"Total Amount: ${meal_details[3]:.2f}")

# Run the program
calculate_meal_cost()