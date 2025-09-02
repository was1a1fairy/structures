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
        node = Node(data)
        if self.is_empty():
            self.__head = node
            self.__tail = node
        else:
            self.__tail.next = node
            node.prev = self.__tail
            self.__tail = node
        self.__count += 1


    def add_head(self, data):
        node = Node(data)
        if not self.is_empty():
            node.next = self.__head
            self.__head.prev = node
        else:
            self.__tail = node
        self.__head = node
        self.__count += 1


    def pop(self, index: int):
        """удаляет элемент по индексу, индексация с 1го"""
        if index >= self.__count or index <= 0:  return None
        iter = self.__head
        for i in range(index-1):
            iter = iter.next
        iter.prev.next = iter.next
        self.__count -= 1
        return iter


    def pop_head(self):
        """удалить с начала"""
        self.__head = self.__head.next
        self.__head.prev = None
        self.__count -= 1
    
    
    def remove(self, elem):
        """удаляет первое вхождение элемента"""
        iter = self.__head
        while iter is not None:
            if iter.data == elem:
                iter.prev.next = iter.next
                return
            iter = iter.next
        self.__count -= 1 
        
    
    def insert(self, index, elem):
        """вставляет элемент по индексу"""
        node = Node(elem)
        iter = self.__head
        for i in range(index-2):
            iter = iter.next
        node.next = iter.next
        node.prev = iter
        iter.next.prev = node
        iter.next = node
        self.__count += 1

    def __get_count(self):
        return self.__count

    def search(self, index):
        """ищет элемент по индексу и возвращает его(ноду)"""
        iter = self.__head
        for i in range(index-2):
            iter = iter.next
        return iter
