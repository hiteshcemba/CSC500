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
        
        # Note: Using :.0f to match the example's integer price and total cost formatting ($1 and $10)
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.0f} = ${total_cost:.0f}")

# Step 2: Build the ItemManager class to hold the collection
class ItemManager:
    """
    Manages a collection of ItemToPurchase objects using a list (array object).
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

# Main execution section (Step 2)
def main():
    # Initialize the Item Manager
    manager = ItemManager()

    # --- Item 1 Input and Creation ---
    item1 = get_item_input(1)
    # Add Item 1 to the manager's collection
    manager.add_item(item1)

    # --- Item 2 Input and Creation ---
    item2 = get_item_input(2)
    # Add Item 2 to the manager's collection
    manager.add_item(item2)
    
    # Optional: Verification that items are stored in the manager (for internal testing)
    # print("\n--- Verification: Items Stored ---")
    # for i, item in enumerate(manager.items_collection):
    #     print(f"Item {i+1} stored: ", end="")
    #     item.print_item_cost()

if __name__ == "__main__":
    main()