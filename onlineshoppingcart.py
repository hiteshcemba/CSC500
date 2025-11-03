from datetime import date

class ItemToPurchase:
    """
    Represents a single item with its name, description, price, and quantity.
    """
    def __init__(self, item_name="none", item_description="none", item_price=0.0, item_quantity=0):
        """
        Initializes an ItemToPurchase object.

        Args:
            item_name (str): The name of the item.
            item_description (str): A description of the item.
            item_price (float): The price of a single item.
            item_quantity (int): The number of items to purchase.
        """
        self.item_name = item_name
        self.item_description = item_description
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):  
        """
        Calculates and prints the total cost for this specific item.
        """
        total_cost = self.item_quantity * self.item_price
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.0f} = ${total_cost:.0f}")

    def print_item_description(self):
        """
        Prints the item's name and its description.
        """
        print(f"{self.item_name}: {self.item_description}")


class ShoppingCart:
    """
    Manages a customer's shopping cart, containing multiple ItemToPurchase objects.
    """
    def __init__(self, customer_name="none", current_date=date.today()):
        """
        Initializes a ShoppingCart object with customer information and an empty cart.

        Args:
            customer_name (str): The name of the customer.
            current_date (date): The current date.
        """
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = {}  # Using a dictionary with item name as key

    def add_item(self, item_to_purchase):
        """
        Adds a new ItemToPurchase object to the cart.

        Args:
            item_to_purchase (ItemToPurchase): The item to be added to the cart.
        """
        self.cart_items[item_to_purchase.item_name] = item_to_purchase

    def remove_item(self, item_name):
        """
        Removes an item from the cart by its name.

        Args:
            item_name (str): The name of the item to be removed.
        """
        if item_name in self.cart_items:
            del self.cart_items[item_name]
        else:
            print("Item not found in cart. Nothing removed.")

    def modify_item(self, item_to_purchase):
        """
        Modifies an existing item's attributes (description, price, or quantity) in the cart.

        Args:
            item_to_purchase (ItemToPurchase): The new item object containing updated attributes.
        """
        if item_to_purchase.item_name in self.cart_items:
            existing_item = self.cart_items[item_to_purchase.item_name]
            if item_to_purchase.item_description != "none":
                existing_item.item_description = item_to_purchase.item_description
            if item_to_purchase.item_price != 0.0:
                existing_item.item_price = item_to_purchase.item_price
            if item_to_purchase.item_quantity != 0:
                existing_item.item_quantity = item_to_purchase.item_quantity
        else:
            print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        """
        Calculates and returns the total quantity of all items in the cart.

        Returns:
            int: The total number of items.
        """
        total_quantity = 0
        for item in self.cart_items.values():
            total_quantity += item.item_quantity
        return total_quantity

    def get_cost_of_cart(self):
        """
        Calculates and returns the total cost of all items in the cart.

        Returns:
            float: The total cost of the cart.
        """
        total_cost = 0.0
        for item in self.cart_items.values():
            total_cost += (item.item_quantity * item.item_price)
        return total_cost

    def print_total(self):
        """
        Prints a detailed summary of the shopping cart, including the total cost.
        """
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date.strftime('%B /%d /%Y')}")
        if not self.cart_items:
            print("Shopping Cart Is Empty")
        else:
            print(f"Number of Items: {self.get_num_items_in_cart()}")
            for item in self.cart_items.values():
                item.print_item_cost()
            print(f"Total: ${self.get_cost_of_cart():.0f}")

    def print_descriptions(self):
        """
        Prints a list of item descriptions for all items in the cart.
        """
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items.values():
            item.print_item_description()


# Helper function to handle user input and object creation
def get_item_input(item_number):
    """
    Prompts the user for item details and creates an ItemToPurchase object.

    Args:
        item_number (int): The sequential number of the item being entered.

    Returns:
        ItemToPurchase: A new object with the user-provided item details.
    """
    print(f"\nItem {item_number}")
    item = ItemToPurchase()
    item.item_name = input("Enter the item name:\n")
    item.item_description = input("Enter the item description:\n")
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

def print_menu(shopcart):
    """
    Outputs a menu of options for manipulating the shopping cart and processes user choices.
    
    Args:
        shopcart (ShoppingCart): The ShoppingCart object to interact with.
    """
    menu_options = {
        'a': 'Add item to cart',
        'r': 'Remove item from cart',
        'c': 'Change item quantity',
        'i': 'Output items\' descriptions',
        'o': 'Output shopping cart',
        'q': 'Quit'
    }

    choice = ''
    while choice != 'q':
        print("\nMENU")
        for key, value in menu_options.items():
            print(f"{key} - {value}")
        
        choice = input("Choose an option: ").lower().strip()
        
        if choice == 'a':
            print("\n*** Add Item To Shopping Cart ***")
            item_to_add = get_item_input(len(shopcart.cart_items) + 1)
            shopcart.add_item(item_to_add)
        elif choice == 'r':
            print("\n*** Remove Item From Cart ***")
            item_name_to_remove = input("Enter name of item to remove:\n")
            shopcart.remove_item(item_name_to_remove)
        elif choice == 'c':
            print("\n*** Change Item Quantity To Shopping Cart ***")
            item_name_to_modify = input("Enter the item name:\n")
            if item_name_to_modify in shopcart.cart_items:
                try:
                    new_quantity = int(input("Enter the new quantity:\n"))
                    if new_quantity > 0:
                        modified_item = ItemToPurchase(item_name_to_modify, item_quantity=new_quantity)
                        shopcart.modify_item(modified_item)
                    else:
                        print("Invalid quantity. Quantity must be a positive number.")
                except ValueError:
                    print("Invalid quantity. Please enter a number.")
            else:
                print("Item not found in cart. Nothing modified.")
        elif choice == 'i':
            print("\n*** Output Shopping Cart - Print Description ***")
            shopcart.print_descriptions()
        elif choice == 'o':
            print("\n*** Output Shopping Cart - Print Total ***")
            shopcart.print_total()
        elif choice == 'q':
            print("\nGoodbye from CSU Global Shopping Cart!")
            break
        else:
            print("Invalid choice. Please try again.")

def main():
    """
    Main function to run the shopping cart program.
    """
    print("Welcome to CSU Global Shopping Cart")
    
    customer_name = input("Enter customer's name:\n")
    current_date = input("Enter today's date::\n")
    shopcart = ShoppingCart(customer_name,current_date)

    print_menu(shopcart)

if __name__ == "__main__":
    main()
