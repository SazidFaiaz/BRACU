
class DoublyNode:

    def __init__(self, elem, next, prev):
        self.element = elem
        self.next = next
        self.prev = prev

    def createList(aray):
        dh = DoublyNode(None, None, None)
        dh.next = dh
        dh.prev = dh
        tail = dh

        for i in range(len(aray)):
            new = DoublyNode(aray[i], dh, tail)
            tail.next = new
            tail = tail.next
            dh.prev = tail

        return dh

    def iteration(dh):
        temp = dh.next
        while temp != dh:
            print(temp.element)
            temp = temp.next

    def nodeat(dh, index):
        temp = dh.next
        count = 0
        while temp != dh:
            if count == index:
                return temp
            count += 1
            temp = temp.next
        return None

    def insertion(dh, elem, idx):
        node_toInsert = DoublyNode(elem, None, None)
        index_node = nodeat(dh, idx)
        prevnode = index_node.prev
        node_toInsert.next = index_node
        node_toInsert.prev = prevnode
        prevnode.next = node_toInsert
        index_node.prev = node_toInsert

    def removal(dh, idx):
        # Assuming the idx is valid
        node_to_remove = nodeat(dh, idx)
        prev_node = node_to_remove.prev
        next_node = node_to_remove.next
        # Change the connection
        # No special case is needed
        prev_node.next = next_node
        next_node.prev = prev_node
        node_to_remove.next = None
        node_to_remove.prev = None
        return node_to_remove.elem  # Returning the removed element

