# node.py

class Node:
    """
    A class to represent a node in a singly linked list.

    Attributes:
    data: The data to be stored in the node.
    next: A reference to the next node in the list.
    
    Methods:
    __init__(data): Initializes the node with the given data.
    get_data(): Returns the data stored in the node.
    set_data(data): Sets the data for the node.
    get_next(): Returns the next node reference.
    set_next(next_node): Sets the next node reference.
    """
    
    def __init__(self, data=None):
        """Initializes a new node with data and sets the next pointer to None."""
        self.data = data
        self.next = None
    
    def get_data(self):
        """Returns the data stored in the node."""
        return self.data
    
    def set_data(self, data):
        """Sets the data for the node."""
        self.data = data
    
    def get_next(self):
        """Returns the reference to the next node."""
        return self.next
    
    def set_next(self, next_node):
        """Sets the reference to the next node."""
        self.next = next_node
