
class Node:
    def __init__(self, elem, next, prev):
        self.element = elem
        self.next = next
        self.prev = prev

####### Q1 ######

class doubly:
    def __init__(self, alist):
        self.head = None
        self.tail = None
        Node = None

        if type(alist) == Node:
            self.head = alist

        elif type(alist) == list:
            for i in range(len(alist)):
                new_node = Node(alist[i], None, None)

                if self.head == None:
                    self.head = new_node
                    Node = new_node

                else:
                    Node.next = new_node
                    new_node.prev = Node
                    Node = Node.next

        self.tail = Node

    ## Q1 ##

    def palindrome(self):
        temp = self.head
        count = 0
        while temp != None:
            count += 1
            temp = temp.next


  ## Q3 ##

    def largest(self):
        head = self.head
        tail = self.tail
        head.prev = tail
        tail.next = head
        node = head.next
        large = head.element

        while node != head:
            if node.element > large:
                large = node.element
            node = node.next
        print(large)



a = doubly([1,7,7,1])
