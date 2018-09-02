"""
Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.
"""
class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = None


def traverse(head_node):
    node = head_node
    while node.next:
        print(node.data, end=' -> ')
        node = node.next
    print(node.data)


def kth_element_from_last(head_node, k):
    current_node = head_node
    pointer_node = current_node
    for i in range(1,k):
        if pointer_node.next is None:
            return
        else:
            pointer_node = pointer_node.next

    while pointer_node.next:
        current_node = current_node.next
        pointer_node = pointer_node.next

    return current_node


basic_list_head = Node(1)
basic_list_head.next = Node(2)
basic_list_head.next.next = Node(1)
basic_list_head.next.next.next = Node(3)
basic_list_head.next.next.next.next = Node(4)
basic_list_head.next.next.next.next.next = Node(1)

traverse(basic_list_head)
print(kth_element_from_last(basic_list_head, 3).data)
traverse(basic_list_head)