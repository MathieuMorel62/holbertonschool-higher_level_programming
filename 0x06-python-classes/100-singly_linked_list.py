#!/usr/bin/python3
""" Defines a node in a singly linked list """


class Node:
    """ Defines a node in a singly linked list """
    def __init__(self, data, next_node=None):
        """
        Initialize the node with data and next_node
        :param data: Integer data for the node
        :param next_node: Next node in the list, defaults to None
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Getter for the data attribute
        :return: Integer data for the node
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Setter for the data attribute
        :param value: Integer data for the node
        :raises TypeError: if data is not an integer
        """
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """
        Getter for the next_node attribute
        :return: Next node in the list
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter for the next_node attribute
        :param value: Next node in the list
        :raises TypeError: if next_node is not a Node object or None
        """
        if value is not None and type(value) != Node:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """ Defines a singly linked list """
    def __init__(self):
        """ Initialize the linked list """
        self.head = None

    def sorted_insert(self, value):
        """
        Inserts a node in the sorted position in the list
        :param value: Integer data for the new node
        """
        new = Node(value)
        node = self.head
        if not node or node.data > value:
            new.next_node = self.head
            self.head = new
        else:
            while node.next_node and node.next_node.data < value:
                node = node.next_node
            new.next_node = node.next_node
            node.next_node = new

    def __str__(self):
        """
        Returns a string representation of the linked list
        :return: String representation of the linked list
        """
        output = ""
        node = self.head
        while node:
            output += str(node.data) + "\n"
            node = node.next_node
        return output.rstrip()
