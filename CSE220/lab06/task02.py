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

def recursiveList_sum(head):
    temp = head
    if temp is None:
        return 0
    else:
        return temp.element + recursiveList_sum(temp.next)

linked_list = linked([10, 20, 30, 40])
print_linked(linked_list)
print(recursiveList_sum(linked_list))

#part C

def print_revers(head):
    if head is None:
        return
    print_revers(head.next)
    print(head.element)

linked_list = linked([10, 20, 30, 40])
print_revers(linked_list)


