class Queue:


    class Node:

        def __init__(self, data, prev=None):
            self.data = data
            self.prev = prev


    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__count = 0


    def enqueue(self, data):
        """
        добавление элемента в конец очереди
        """

        node = Queue.Node(data)

        if self.is_empty():
            self.__head = node
        else:
            self.__tail.prev = node

        self.__tail = node
        self.__count += 1


    def dequeue(self):
        """
        удаляет элемент из начала очереди и возвращает его
        """

        if self.is_empty():
            return None

        node = self.__head
        self.__head = node.prev

        if self.__count == 1:
            self.__tail = None

        self.__count -= 1
        return node.data
    

    def peek(self):

        if not self.is_empty():
            return self.__head.data


    def is_empty(self):

        return self.__count == 0


    def __get_count(self):
        return self.__count


    count = property(__get_count)
