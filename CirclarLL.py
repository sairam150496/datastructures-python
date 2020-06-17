class Node:
    def __init__(self, value, next_node):
        self.value = value,
        self.next_node = next_node


class CircularLL:

    def __init__(self, value):
        self.tail = self.head = Node(value, None)
        self.size = 1

    def insert_first(self, value):
        new_node = Node(value, None)
        new_node.next_node = self.head
        self.tail.next_node = new_node
        self.head = new_node
        self.size += 1

    def get_circular_list(self):
        temp_node = self.head
        while temp_node != self.tail:
            print(temp_node.value[0])
            temp_node = temp_node.next_node
        print(temp_node.value[0])

    def insert_end(self, value):
        new_node = Node(value, None)
        new_node.next_node = self.tail.next_node
        self.tail.next_node = new_node
        self.tail = new_node
        self.size += 1

    def remove_first(self):
        self.head = self.head.next_node
        self.tail.next_node = self.head
        self.size -= 1

    def remove_last(self):
        temp_node = self.head
        while temp_node.next_node != self.tail:
            temp_node = temp_node.next_node
        temp_node.next_node = self.head
        self.tail = temp_node
        self.size -= 1


cll = CircularLL(5)
cll.insert_first(10)
cll.insert_first(15)
cll.insert_first(120)
cll.insert_first(244)
cll.insert_first(434)
cll.insert_end(1000)
cll.insert_end(20000)
cll.remove_first()
cll.remove_first()
cll.remove_last()
cll.remove_last()
print(cll.size)
cll.get_circular_list()

