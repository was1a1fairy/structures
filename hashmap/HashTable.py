class HashMap:

    class Node:

        def __init__(self, key, value):
            self.key = key
            self.value = value

    def __init__(self):
        self.__n = 100
        self.__array = [None] * self.__n
        self.__count = 0

    def __hash(self, key) -> int:
        return hash(key) % len(self.__array)

    def add(self, key, value):
        if self.__count == len(self.__array):
            self.__array.append(None)
        h = self.__hash(key)
        if self.__array[h] is not None:
            self.add(h, value)
        self.__count += 1
        self.__array[h] = HashMap.Node(key, value)

    def remove(self, key):
        h = self.__hash(key)
        if self.__array[h] is None:
            return
        if self.__array[h].key != key:
            self.remove(h)
        self.__array[h] = None
        self.__count -= 1

    def give_value(self, key):
        h = self.__hash(key)
        if self.__array[h] is None:
            return
        if self.__array[h].key != key:
            self.give_value(h)
        return self.__array[h].value
