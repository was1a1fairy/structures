class Node:

    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.prev = prev
        self.next = next

class DoubleLinkedList:

    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__count = 0

    def is_empty(self):
        return self.__count == 0

    def add(self, data):
        pass

    def add_head(self, data):
        pass

    def pop(self):
        pass

    def pop_head(self):
        pass

    def pop_index(self):
        pass

    def insert(self):
        pass

    def __get_count(self):
        return self.__count

    def search(self, index):
        pass
