"""
Linked List Implementation
"""


class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


def traverse(head_node):
    node = head_node
    while node.next:
        print(node.data, end=' -> ')
        node = node.next
    print(node.data)


def search(head_node, value):
    node = head_node
    while node.next is not None:
        if node.data == value:
            return True
        else:
            node = node.next
    if node.data == value:
        return True
    else:
        return False


if __name__ == '__main__':
    # list 1 -> 2 -> 3 -> 4
    basic_list_head = Node(1)
    basic_list_head.next = Node(2)
    basic_list_head.next.next = Node(3)
    basic_list_head.next.next.next = Node(4)

    traverse(basic_list_head)
    print(search(basic_list_head, 4))
    print(search(basic_list_head, 5))
