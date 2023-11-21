#!/usr/bin/python3
"""Module: defines a singly linked list"""


class Node:
    """Node: defines a node object"""
    def __init__(self, data, next_node=None):
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = data
        if not isinstance(next_node, Node) and next_node is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = next_node

    @property
    def data(self):
        """gets the value of __data"""
        return self.__data

    @data.setter
    def data(self, value):
        """setes the value of __data"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """gets the value of __next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """sets the value of __next_node"""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """SinglyLinkedList: defines a singly linked list object"""
    def __init__(self):
        """__init__: constructs a SinglyLinkedList object"""
        self.__head = None

    def sorted_insert(self, value):
        """sorted_insert: inserts a Node respecting order"""
        newnode = Node(value)
        if self.__head is None:
            newnode.next_node = None
            self.__head = newnode
        elif value < self.__head.data:
            newnode.next_node = self.__head
            self.__head = newnode
        else:
            iterator = self.__head
            while (iterator.next_node is not None and
                    iterator.next_node.data < value):
                iterator = iterator.next_node
            newnode.next_node = iterator.next_node
            iterator.next_node = newnode

    def __str__(self):
        """Define the print of a SinglyLinkedList."""
        string = []
        iterator = self.__head
        while iterator is not None:
            string.append(str(iterator.data))
            iterator = iterator.next_node
        return ('\n'.join(string))


if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.sorted_insert(2)
    sll.sorted_insert(5)
    sll.sorted_insert(3)
    sll.sorted_insert(10)
    sll.sorted_insert(1)
    sll.sorted_insert(-4)
    sll.sorted_insert(-3)
    sll.sorted_insert(4)
    sll.sorted_insert(5)
    sll.sorted_insert(12)
    sll.sorted_insert(3)
    print(sll)
