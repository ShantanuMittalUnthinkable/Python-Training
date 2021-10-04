from typing import Any


class Node:

    data: Any
    next_node: Any = None

    def __init__(self, data: Any, next_node: Any = None) -> None:
        self.data = data
        self.next_node = next_node

class LinkedList:

    def __init__(self, first: Node = None) -> None:
        
        self.first = first

    def __str__(self) -> str:
        
        return str(self.display_all())

    def append_node(self, incoming_node: Node) -> None:

        '''
        To add a node at the end of the linked list
        '''

        p = self.first

        if p != None:

            while(p.next_node != None):
                p = p.next_node

            p.next_node = incoming_node

        else:

            self.first = incoming_node
    
    def add_node(self, key: int, incoming_node: Node) -> None:

        '''
        To add a node after a key
        '''

        target_node = None

        p = self.first

        while(p.data != key):
            p = p.next_node

        if p.data != key:
            raise Exception("Key not present in linked list.")

        incoming_node.next_node = p.next_node
        p.next_node = incoming_node

    def delete_node(self, key: int):

        previous_node = None

        p = self.first
        print(p)

        while(p.data != key):
            print(p)
            previous_node = p
            p = p.next_node

        if p.data != key:
            raise Exception("Key not present in linked list.")
        
        previous_node.next_node = p.next_node

    def display_all(self):

        result = []

        p = self.first
        if self.first:
            print(p)
            while(p.next_node != None):
                result.append(p.data)
                p = p.next_node

        return result

    def reverse(self):

        next_node = None
        previous_node = None
        
        p = self.first

        while(p != None):

            next_node = p.next_node

            p.next_node = previous_node
            previous_node = p

            p = next_node

        self.first = previous_node

    def search_node(self, key):

        position = 0

        p = self.first
        found = False

        while(p.next_node != None):
            if p.data == key:
                return position
            else:
                position += 1

        return -1