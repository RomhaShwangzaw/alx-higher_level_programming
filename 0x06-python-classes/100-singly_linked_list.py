#!/usr/bin/python3
''' A singly linked list module '''


class Node:
    ''' A class that defines a node of a singly linked list '''

    def __init__(self, data, next_node=None):
        ''' Initialization function '''

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        ''' Gets the value of data '''

        return self.__data

    @data.setter
    def data(self, value):
        ''' Sets the value of data '''

        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        ''' Gets the value of next_node '''

        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        ''' Sets the value of next_node '''

        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    ''' A class that defines a singly linked list '''

    def __init__(self):
        """Initalize a new SinglyLinkedList."""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new Node to the SinglyLinkedList.
        The node is inserted into the list at the correct
        ordered numerical position.
        Args:
            value (Node): The new Node to insert.
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """Define the print() representation of a SinglyLinkedList."""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
