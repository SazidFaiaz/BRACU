class Node:
    def __init__(self, e, n):
        self.element = e
        self.next = n

def linked(arr):

    head = Node(arr[0], None)
    tail = head
    for i in range(1, len(arr)):
        new = Node(arr[i], None)
        tail.next = new
        tail = tail.next
    return head


def print_linked(head):
    temp = head
    while temp != None:
        print(temp.element, end="-->")
        temp = temp.next
    print(None)

def countnode(head):
    count = 0
    temp = head
    while temp != None :
        count += 1
        temp = temp.next
    return count


def NodeAt(head, index):
    count = 0
    temp = head
    while temp:
        if count == index:
            return head
        count += 1
        temp = temp.next
    return "Invalid "

def element(head, value):
    temp =head
    while temp:
        if temp.element == value:
            return head
        temp = temp.next
    return "dosen't exist"

linked_list = linked([1,2,3,4])
print_linked(linked_list)
print(countnode(linked_list))
print(element(linked_list,4))