# The model of the commissary application
# 
# The primary functions that we have are
# - Storing information on products we own
# - Storing lists of things we might want to buy
# - Storing the relative location of items
# 
# Get count of items
# - filter by
#   - item type
#   - item location
#   - item property


create class
    name: 'Book'



@dataclass
class InventoryItem:
    '''Class for keeping track of an item in inventory.'''
    name: str
    unit_price: float
    quantity_on_hand: int = 0

    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand



class Book():
    """
    A digital or physical book
    """
    def in_collection() bool:

