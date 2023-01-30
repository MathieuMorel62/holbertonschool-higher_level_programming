#!/usr/bin/python3


class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and type(value) != Node:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def sorted_insert(self, value):
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
        output = ""
        node = self.head
        while node:
            output += str(node.data) + "\n"
            node = node.next_node
        return output.rstrip()
