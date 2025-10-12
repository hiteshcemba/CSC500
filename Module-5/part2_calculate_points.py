def calculate_points(num_books):
    if num_books == 0:
        return 0
    elif num_books == 2:
        return 5
    elif num_books == 4:
        return 15
    elif num_books == 6:
        return 30
    elif num_books >= 8:
        return 60
    else:
        # Handles cases like 1, 3, 5, and other invalid inputs
        return "Points for this number of books are not defined."


print("Welcome to CSU Global Bookstore !")
while True:
    try:
        books_purchased = int(input("Enter the number of books purchased this month: "))
        if books_purchased < 0:
            print("Number of books cannot be negative. Please try again.")
            continue
        
        points = calculate_points(books_purchased)
        print(f"You have been awarded {points} points.")
        break
    except ValueError:
        print("Invalid input. Please enter a whole number.")
