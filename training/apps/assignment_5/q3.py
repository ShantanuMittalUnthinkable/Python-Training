from typing import Any


class Node:

    data: Any
    next_node: Any = None

class LinkedList:

    def __init__(self, first: Node = None) -> None:
        
        self.first = first

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

        while(p.data != key):
            previous_node = p
            p = p.next_node

        if p.data != key:
            raise Exception("Key not present in linked list.")
        
        previous_node.next_node = p.next_node