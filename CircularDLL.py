class Node:
    def __init__(self, value):
        self.prev_node = None
        self.value = value
        self.next_node = None


class CircularDLL:

    def __init__(self, value):
        self.tail = self.head = Node(value)
        self.size = 1

    def insert_first(self, value):
        new_node = Node(value)
        self.head.prev_node = new_node
        self.tail.next_node = new_node
        new_node.next_node = self.head
        new_node.prev_node = self.tail
        self.head = new_node
        self.size += 1

    def insert_end(self, value):
        new_node = Node(value)
        new_node.next_node = self.tail.next_node
        self.tail.next_node = new_node
        new_node.prev_node = self.tail
        self.tail = new_node
        self.size += 1

    def insert_at(self, position, value):
        if position <= 0:
            self.insert_first(value)
        elif position >= self.size:
            self.insert_end(value)
        else:
            new_node = Node(value)
            if position > self.size//2:
                temp_node = self.tail
                while self.size - position > 0:
                    temp_node = temp_node.prev_node
                    position += 1
                new_node.next_node = temp_node
                new_node.prev_node = temp_node.prev_node
                temp_node.prev_node.next_node = new_node
                temp_node.prev_node = new_node

            else:
                temp_node = self.head
                while position > 0:
                    temp_node = temp_node.next_node
                    position -= 1
                new_node.next_node = temp_node
                new_node.prev_node = temp_node.prev_node
                temp_node.prev_node.next_node = new_node
                temp_node.prev_node = new_node
        self.size += 1

    def remove_element_at(self, position):
        if position <= 0:
            self.remove_first()
        elif position >= self.size:
            self.remove_last()
        else:
            temp_node = self.head
            while position > 0:
                temp_node = temp_node.next_node
                position -= 1
            temp_node.prev_node.next_node = temp_node.next_node
            temp_node.next_node.prev_node = temp_node.prev_node
        self.size -= 1

    def remove_last(self):
        self.tail.prev_node.next_node = self.tail.next_node
        self.tail = self.tail.prev_node
        self.head.prev_node = self.tail
        self.size -= 1

    def get_list(self):
        temp_node = self.head
        while temp_node != self.tail:
            print(temp_node.value)
            temp_node = temp_node.next_node
        print(temp_node.value)

    def get_list_rev(self):
        temp_node = self.tail
        while temp_node != self.head:
            print(temp_node.value)
            temp_node = temp_node.prev_node
        print(temp_node.value)

    def remove_first(self):
        self.head = self.head.next_node
        self.head.prev_node = self.tail
        self.tail.next_node = self.head
        self.size -= 1


circular_dll = CircularDLL(5)
circular_dll.insert_first(10)
circular_dll.insert_first(15)
circular_dll.insert_first(20)
circular_dll.insert_end(0)
circular_dll.insert_end(-5)
circular_dll.insert_end(-10)
circular_dll.remove_first()
circular_dll.remove_last()
circular_dll.remove_first()
circular_dll.remove_first()
circular_dll.insert_at(4, -15)
circular_dll.insert_at(3, -20)
circular_dll.remove_element_at(3)
# print(circular_dll.size)
circular_dll.get_list()
# circular_dll.get_list_rev()


