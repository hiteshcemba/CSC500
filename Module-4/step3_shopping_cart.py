# Step 1: Build the ItemToPurchase class
class ItemToPurchase:
    """
    Represents an item to be purchased, tracking its name, price, and quantity.
    """
    def __init__(self):
        """
        Default constructor: Initializes item attributes to default values.
        """
        # Attributes
        self.item_name = "none"  # string
        self.item_price = 0.0    # float
        self.item_quantity = 0   # int

    def print_item_cost(self):
        """
        Calculates and prints the cost of the item in the specified format.
        Example: Bottled Water 10 @ $1 = $10
        """
        total_cost = self.item_price * self.item_quantity
        
        # Note: Using :.0f to match the example's integer price and total cost formatting
        # We assume prices are whole numbers based on the example ($1, $3, $10, $13)
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.0f} = ${total_cost:.0f}")
        return total_cost # Return cost for aggregation in ItemManager


# Step 2 & 3: Build the ItemManager class to hold the collection and calculate total cost
class ItemManager:
    """
    Manages a collection of ItemToPurchase objects and calculates the total cost.
    """
    def __init__(self):
        """
        Initializes the list to hold the item collection.
        """
        self.items_collection = []

    def add_item(self, item):
        """
        Adds an ItemToPurchase object to the collection list.
        """
        if isinstance(item, ItemToPurchase):
            self.items_collection.append(item)
        else:
            print(f"Error: Cannot add non-ItemToPurchase object to the collection.")

    def print_total_cost(self):
        """
        Calculates and prints the total cost of all items in the collection,
        including individual item costs, in the specified format.
        """
        if not self.items_collection:
            print("\nTOTAL COST\n(Shopping cart is empty.)")
            return

        grand_total = 0.0
        
        print("\nTOTAL COST")
        
        for item in self.items_collection:
            # Call the item's method to print its individual cost
            item_total = item.print_item_cost()
            # Aggregate the cost
            grand_total += item_total
        
        # Output the final total cost (matching the integer formatting of the example)
        print(f"Total: ${grand_total:.0f}")


# Helper function to handle user input and object creation
def get_item_input(item_number):
    """
    Prompts the user for item details and creates an ItemToPurchase object.
    """
    print(f"\nItem {item_number}")
    
    # Create a new object of the ItemToPurchase class
    item = ItemToPurchase()
    
    # Read user input and update the object's attributes
    item.item_name = input("Enter the item name:\n")
    
    try:
        item.item_price = float(input("Enter the item price:\n"))
    except ValueError:
        print("Invalid input for price. Setting to 0.0.")
        item.item_price = 0.0
        
    try:
        item.item_quantity = int(input("Enter the item quantity:\n"))
    except ValueError:
        print("Invalid input for quantity. Setting to 0.")
        item.item_quantity = 0
    
    return item

# Main execution section
def main():
    # Initialize the Item Manager
    manager = ItemManager()

    # --- Item 1 Input and Creation (Step 2) ---
    item1 = get_item_input(1)
    manager.add_item(item1)

    # --- Item 2 Input and Creation (Step 2) ---
    item2 = get_item_input(2)
    manager.add_item(item2)

    # --- Output Total Cost (Step 3) ---
    manager.print_total_cost()


if __name__ == "__main__":
    main()