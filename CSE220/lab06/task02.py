#part A
def corresponding(num):
    if num == 0:
        return "0"
    elif num == 1:
        return "1"
    else:
        return corresponding(num//2)+str(num%2)

print(corresponding(5))

# part B
class Node:
    def __init__(self, elem, next, prev):
        self.element = elem
        self.next = next
        self.prev = prev

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

def recursiveList(node):
    if node is None:
        return 0
    else:
        return node.element + recursiveList(node.next)

a = doubly([0,1,2,3,4,5])

