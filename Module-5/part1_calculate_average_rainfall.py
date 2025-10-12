def calculate_average_rainfall():
    """
    Collects rainfall data over a period of years and calculates the average.
    """
    while True:
        try:
            num_years = int(input("Enter the number of years: "))
            if num_years < 1:
                print("Number of years cannot be less than 1. Please try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a whole number for the number of years.")

    total_rainfall = 0
    total_months = num_years * 12

    for year in range(1, num_years + 1):
        print(f"\n--- Year {year} ---")
        for month in range(1, 13):
            while True:
                try:
                    rainfall = float(input(f"Enter the inches of rainfall for month {month}: "))
                    if rainfall < 0:
                        print("Rainfall cannot be negative. Please try again.")
                    else:
                        total_rainfall += rainfall
                        break
                except ValueError:
                    print("Invalid input. Please enter a numerical value for rainfall.")

    average_rainfall = total_rainfall / total_months if total_months > 0 else 0

    print("\n--- Rainfall Summary ---")
    print(f"Number of months: {total_months}")
    print(f"Total inches of rainfall: {total_rainfall:.2f}")
    print(f"Average rainfall per month: {average_rainfall:.2f}")

# Run the program
calculate_average_rainfall()