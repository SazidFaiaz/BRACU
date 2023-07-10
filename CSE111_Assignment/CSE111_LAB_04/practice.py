class Node:
    def __init__(self, value):
        self.val = value
        self.next = None
        self.prev = None


class Linked_list:
    def __init__(self):
        self.hed = None
        self.tail = None
        self.size = 0

    def add(self, new_val):
        node = Node(new_val)
        if self.tail is None:
            self.hed = node
            self.tail = node
            self.size += 1
        else:
            node.prev = self.hed
            self.tail.next = node
            self.tail = node
            self.size += 1

    def __remove_node(self, node):
        if node.prev is None:
            self.hed = node.next
        if node.next is None:
            self.tail = node.prev
        node.prev.next = node.next
        node.next.prev

    def remove(self, value):
        node = self.head
        while node is not None:
            if node.val == value:
                self.__remove_node(node)
            node = node.next


    def __str__(self):
        vals = []
        node = self.hed
        while node is not None:
            vals.append(node.val)
            node = node.next
        return f'[{",".join(str(val) for val in vals)} ]'


my_list = Linked_list()
my_list.add(1)
my_list.add(5)
my_list.add(2)
print(my_list)
print(my_list.size)
