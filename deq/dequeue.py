
class Deq:

    class Node:

        def __init__(self, data, next=None, prev=None):
            self.data = data
            self.next = next
            self.prev = prev


    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__count = 0


    def is_empty(self):
        return self.__count == 0


    def enqueue(self, data):
        """добавление в конец очереди"""
        node = Deq.Node(data)
        if self.is_empty():
            self.__head = node
            self.__tail = node
        self.__tail.prev = node
        node.next = self.__tail
        self.__tail = node
        self.__count += 1


    def dequeue(self):
        """удаление из начала очереди"""
        if self.is_empty():
            return
        if self.__count == 1:
            self.__head, self.__tail = None, None
            return
        self.__head.prev.next = None
        self.__count -= 1


    def enqueue_first(self, data):
        """
        добавление в начало очереди(в голову)
        """
        node = Deq.Node(data)
        if self.is_empty():
            self.__tail = node
        node.prev = self.__head
        self.__head.next = node
        self.__head = node
        self.__count += 1


    def dequeue_last(self):
        """
        удаление из хвоста
        """
        if self.is_empty():
            return
        if self.__count == 1:
            self.__head, self.__tail = None, None
            return
        self.__tail = self.__tail.next
