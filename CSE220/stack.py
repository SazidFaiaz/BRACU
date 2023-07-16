
class Node:
    def __init__(self, element, next):
        self.element = element
        self.next = next

    class Stack:
        def __init__(self):
            self.top = None

        def push(self, elem):
            if self.top == None:
                self.top = Node(elem, None)
            else:
                new = Node(elem, None)
                new.next = self.top
                self.top = new

        def pop(self):
            if self.top == None:
                return None
            else:
                poped = self.top
                self.top = self.top.next
                poped.next = None
                return poped.element

        def peek(self):
            if self.top == None:
                return None
            else:
                return self.top.element


