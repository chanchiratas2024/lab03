# linked_list.py

from node import Node  # Importamos la clase Node desde el módulo node

class LinkedList:
    """
    A class to represent a singly linked list.

    Attributes:
    head: The first node in the list (or None if the list is empty).
    length: The number of nodes in the list.

    Methods:
    __init__(): Initializes an empty linked list.
    display(): Returns a string representation of the linked list.
    list_length(): Returns the number of nodes in the list.
    insert_at_beginning(data): Inserts a new node at the beginning of the list.
    insert_at_end(data): Inserts a new node at the end of the list.
    insert_at_position(position, data): Inserts a new node at a specific position.
    delete_from_beginning(): Deletes and returns the first node.
    delete_from_end(): Deletes and returns the last node.
    delete_from_position(position): Deletes and returns the node at a specific position.
    search(data): Searches for a node with specific data and returns its position.
    """
    
    def __init__(self):
        """Initializes an empty linked list."""
        self.head = None
        self.length = 0
    
    def display(self):
        """Returns a string representation of the linked list."""
        if self.head is None:
            return "Empty list"
        
        current = self.head
        result = ""
        
        while current is not None:
            result += str(current.get_data()) + " -> "
            current = current.get_next()
        
        return result + "None"

    def list_length(self):
        """Returns the number of nodes in the linked list."""
        count = 0
        current = self.head
        
        while current is not None:
            count += 1
            current = current.get_next()
        
        return count

    def insert_at_beginning(self, data):
        """Inserts a new node with data at the beginning of the list."""
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
        else:
            new_node.set_next(self.head)
            self.head = new_node
        
        self.length += 1
        return True

    def insert_at_end(self, data):
        """Inserts a new node with data at the end of the list."""
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.get_next() is not None:
                current = current.get_next()
            current.set_next(new_node)
        
        self.length += 1
        return True

    def insert_at_position(self, position, data):
        """Inserts a new node at a specific position in the list."""
        if position < 0 or position > self.length:
            return False
        
        if position == 0:
            return self.insert_at_beginning(data)
        
        if position == self.length:
            return self.insert_at_end(data)
        
        new_node = Node(data)
        current = self.head
        count = 0
        
        while count < position - 1:
            current = current.get_next()
            count += 1
        
        new_node.set_next(current.get_next())
        current.set_next(new_node)
        
        self.length += 1
        return True

    def delete_from_beginning(self):
        """Deletes and returns the first node."""
        if self.head is None:
            return None
        
        data = self.head.get_data()
        self.head = self.head.get_next()
        self.length -= 1
        
        return data

    def delete_from_end(self):
        """Deletes and returns the last node."""
        if self.head is None:
            return None
        
        if self.head.get_next() is None:
            data = self.head.get_data()
            self.head = None
            self.length -= 1
            return data
        
        current = self.head
        while current.get_next().get_next() is not None:
            current = current.get_next()
        
        data = current.get_next().get_data()
        current.set_next(None)
        self.length -= 1
        
        return data

    def delete_from_position(self, position):
        """Deletes and returns the node at the specific position."""
        if position < 0 or position >= self.length or self.head is None:
            return None
        
        if position == 0:
            return self.delete_from_beginning()
        
        if position == self.length - 1:
            return self.delete_from_end()
        
        current = self.head
        count = 0
        
        while count < position - 1:
            current = current.get_next()
            count += 1
        
        node_to_delete = current.get_next()
        data = node_to_delete.get_data()
        current.set_next(node_to_delete.get_next())
        self.length -= 1
        
        return data

    def search(self, data):
        """Searches for a node with specific data and returns its position."""
        if self.head is None:
            return -1
        
        current = self.head
        position = 0
        
        while current is not None:
            if current.get_data() == data:
                return position
            current = current.get_next()
            position += 1
        
        return -1
