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


# def iteration(head):
#     temp = head
#     while temp:
#         print(temp.element)
#         temp = temp.next


def print_linked(head):
    temp = head
    while temp != None:
        print(temp.element, end="-->")
        temp = temp.next
    print(None)


def countnode(head):
    count = 0
    temp = head
    while temp != None:
        count += 1
        temp = temp.next
    return count


def NodeAt(head, index):
    count = 0
    temp = head
    while temp:
        if count == index:
            return temp
        count += 1
        temp = temp.next
    return "Invalid"


def elemAt(head, index):
    temp = head
    count = 0
    obj = None
    while temp:
        if count == index:
            obj = temp.element
            break
        temp = temp.next
        count += 1
    if obj == None:
        print("Invalid index")
    return obj


def element(head, value):
    temp = head
    while temp:
        if temp.element == value:
            return head
        temp = temp.next
    return "dosen't exist"


def contains(head, value):
    temp = head

    while temp:
        if temp.element == value:
            return True
        temp = temp.next
    return False


def indexof(head, value):
    count = 0
    temp = head
    while temp:
        if temp.element == value:
            return count
        count = count+1
        temp = temp.next
    return 'Invalid'

#Update value of specific index:
def set(head, index, elem):
    count = 0
    temp = head
    isUpdated =  False
    while temp:
        if count == index:
            temp.next = elem
            isUpdated = True
            break
        temp = temp.next
        count += 1
    if isUpdated:
        print("successfull!")
    else:
        print("invalid index!")


# Inserting an element into a list:

def inserting(head, elem, index):
    total_nodes = countnode(head)
    if index == 0:
        new = Node(elem, head)
        head = new
    elif index >= 1 and index < total_nodes:
        new = Node(elem, head)
        new1 = NodeAt(head, index-1)
        new2 = NodeAt(head, index)
        new.next = new2
        new1.next = new
    elif index == total_nodes:
        new = Node(elem, None)
        new1 = NodeAt(head, total_nodes-1)
        new1.next = new
    else:
        print("Invalid")
    return head





linked_list = linked([1, 2, 3, 4])
print_linked(linked_list)
print(countnode(linked_list))
print(element(linked_list, 4))
print(NodeAt(linked_list, 3).element)