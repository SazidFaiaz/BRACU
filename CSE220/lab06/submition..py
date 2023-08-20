# class Node:
#     def __init__(self, next_node, bottom_node, val):
#         self.next = next_node
#         self.bottom = bottom_node
#         self.val = val
#
#
# def flattenList(given_list, output_list):
#     if len(given_list) == 0:
#         return output_list
#
#     item = given_list[0]
#
#     if isinstance(item, list):
#         return flattenList(item + given_list[1:], output_list)
#     else:
#         output_list = flattenList(given_list[1:], output_list)
#         output_list.insert(0, item)
#         return output_list
#
#
# given_list = [1, [2, [3, [4], 5], 6], 7, 8, [9, [[10, 11], 12], 13], 14, [15, [16, [17]]]]
# output_list = flattenList(given_list, [])
# print(output_list)

class Node:
    def __init__(self, next_node, bottom_node, val):
        self.next = next_node
        self.bottom = bottom_node
        self.val = val


def flattenList(given_list, output_list):
    if len(given_list) == 0:
        return output_list

    item = given_list[0]

    if type(item) == list:
        return flattenList(item + given_list[1:], output_list)
    else:
        output_list = flattenList(given_list[1:], output_list)
        output_list.insert(0, item)
        return output_list


given_list = [1, [2, [3, [4], 5], 6], 7, 8, [9, [[10, 11], 12], 13], 14, [15, [16, [17]]]]
output_list = flattenList(given_list, [])
print(output_list)
