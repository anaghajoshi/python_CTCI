"""
Delete Middle Node: Implement an algorithm to delete a node in the middle (Le., any node but the first and last node, not necessarily the exact middle) of a singly linked list, given only access to that node.
SOLUTION
EXAMPLE
Input: the node c from the linked list a- >b- >c - >d - >e- >f
Result: nothing is returned, but the new linked list looks like a->b->d->e->f

"""


class Node:
    def __init__(self,data=0, next=None):
        self.data = data
        self.next = next


def travese(head_node):
    node = head_node
    while node.next:
        print(node.data, end=' -> ')
        node = node.next
    print(node.data)


def remove_from_middle(rem_node):
    rem_node.data = rem_node.next.data
    rem_node.next = rem_node.next.next


node1 = Node('A')
node2 = Node('B')
node3 = Node('C')
node4 = Node('D')
node5 = Node('E')

basic_list_head = node1
basic_list_head.next = node2
basic_list_head.next.next = node3
basic_list_head.next.next.next = node4
basic_list_head.next.next.next.next = node5
travese(basic_list_head)
remove_from_middle(node3)
travese(basic_list_head)
