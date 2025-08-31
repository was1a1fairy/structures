
class Node:

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:


    def __init__(self):
        self.__count = 0
        self.__head = None


    def is_empty(self):
        return self.__count == 0


    def add(self, elem):
        """
        добавляет элемент в начало списка
        """
        if self.is_empty():
            node = Node(elem, None)
        else:
            node = Node(elem, self.__head)
        self.__head = node
        self.__count += 1


    def append(self, elem):
        """
        добавляет новый элемент в конец списка
        """
        node = Node(elem, None)

        if self.is_empty():
            self.__head = node
        else:
            iterator = self.__head
            while iterator.next is not None:
                iterator = iterator.next

            iterator.next = node
        self.__count += 1


    def insert(self, index:int, elem):
        """
        добавляет новый элемент по индексу
        индекс от 0 до self.count -1
        """
        if not isinstance(index, int):  return None
        if index >= self.__count or index <= 0:  return None

        iter = self.__head
        for i in range(index-1):
            iter = iter.next

        node = Node(elem, iter.next)
        iter.next = node

  
    def count(elem):
      pass

  
    def remove(self, elem):
        """
        удаляет элементы, соответствующие переданному значению
        """
        iter = self.__head
        while iter.next is not None:
            if iter.next.elem == elem:
                iter.next = iter.next.next
                self.__count -= 1
            iter = iter.next

    def clear_all(self):
        self.__count = 0
        self.__head = None


    def get_count(self):
        return self.__count
