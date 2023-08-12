class Node:
    def __init__(self, next_node, bottom_node, val):
        self.next = next_node  # for next item
        self.bottom = bottom_node  # for nested item check
        self.val = val  # The integer value.


def flattenList(given_list, output_list):
    if len(given_list) == 0:
        return output_list

    item = given_list[0]

    if isinstance(item, list):
        return flattenList(item + given_list[1:], output_list)
    else:
        output_list = flattenList(given_list[1:], output_list)
        output_list.insert(0, item)
        return output_list


given_list = [1, [2, [3, [4], 5], 6], 7, 8, [9, [[10, 11], 12], 13], 14, [15, [16, [17]]]]
output_list = flattenList(given_list, [])
print(output_list)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]


# def flattenListLinkedList(node, output_list):
#     while node is not None:
#         output_list.append(node.val)
#
#         # Recursively flatten the nested linked list
#         if node.bottom:
#             flattenListLinkedList(node.bottom, output_list)
#
#         node = node.next
#
#
# # Constructing the linked list structure
# node17 = Node(None, None, 17)
# node16 = Node(None, node17, 16)
# node15 = Node(None, node16, 15)
# node14 = Node(None, None, 14)
# node13 = Node(None, None, 13)
# node12 = Node(node14, None, 12)
# node11 = Node(None, None, 11)
# node10 = Node(node11, node12, 10)
# node9 = Node(None, node10, 9)
# node8 = Node(node9, node13, 8)
# node7 = Node(node8, None, 7)
# node6 = Node(node7, None, 6)
# node5 = Node(None, None, 5)
# node4 = Node(None, None, 4)
# node3 = Node(node4, node5, 3)
# node2 = Node(node3, node6, 2)
# node1 = Node(node2, node7, 1)
#
# output_list_linked = []
# flattenListLinkedList(node1, output_list_linked)
# print(output_list_linked)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
