# This program demonstrates a simple shopping cart system using the ItemToPurchase class.

class ItemToPurchase:
    """
    Represents an item to be purchased, with a name, price, and quantity.
    """
    
    def __init__(self):
        """
        Default constructor that initializes the item's attributes.
        """
        self.item_name = "none"
        self.item_price = 0.0
        self.item_quantity = 0

    def print_item_cost(self):
        """
        Prints the item's cost in the specified format.
        Example: Bottled Water 10 @ $1 = $10
        """
        total_cost = self.item_price * self.item_quantity
        print(f'{self.item_name} {self.item_quantity} @ ${int(self.item_price)} = ${int(total_cost)}')

# Example usage (not part of the class definition):
# To test the class, you can create an instance and call the method.
# For example, if you set the attributes manually:
# item = ItemToPurchase()
# item.item_name = "Bottled Water"
# item.item_price = 1.0
# item.item_quantity = 10
# item.print_item_cost()
# This would output: Bottled Water 10 @ $1 = $10

class ItemsManager:
    """
    Represents an ItemsManager class which collect the array of ItemToPurchase.
    """
    def __init__(self):
        """
        Default constructor that initializes the item's attributes.
        """
        self.listitems = [];
     
    def addItemInList(self,item):
         """
        Adding new item in to listitems array
        """
        self.listitems.append(item)