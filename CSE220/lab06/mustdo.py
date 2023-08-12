class Node:
    def __init__(self, next_node, bottom_node, val):
        self.next = next_node  # for next item
        self.bottom = bottom_node  # for nested item check
        self.val = val  # The integer value.


def flattenList(given_list, output_list):
    for item in given_list:
        if isinstance(item, list):
            flattenList(item, output_list)
        else:
            output_list.append(item)
    return output_list

given_list = [1, [2, [3, [4], 5], 6], 7, 8, [9, [[10, 11], 12], 13], 14, [15, [16, [17]]]]
output_list = flattenList(given_list, [])
print(output_list)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
