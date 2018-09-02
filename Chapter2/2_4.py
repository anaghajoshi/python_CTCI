"""
Partition: Write code to partition a linked list around a value x, such that all nodes less than x come before all nodes greater than or equal to x. If x is contained within the list, the values of x only need to be after the elements less than x (see below). The partition element x can appear anywhere in the "right partition"; it does not need to appear between the left and right partitions.
SOLUTION
EXAMPLE
Input: 3 -) 5 -) 8 -) 5 -) 113 -) 2 -) 1[partition=5] Output: 3 -) 1 -) 2 -) 113 -) 5 -) 5 -) 8

"""


class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


def traverse(head_node):
    node = head_node
    while node.next:
        print(node.data, end=" -> ")
        node = node.next
    print(node.data)
    return


def partition(head_node,partition):
    list_head = Node()
    list_tail = Node()
    og_list_head = list_head
    og_list_tail = list_tail
    current_node = head_node

    while current_node.next:
        print('current_node is ', current_node.data)
        traverse(og_list_head)
        traverse(og_list_tail)
        next_node = current_node.next
        print('next_node is ', next_node.data)
        print('')
        if current_node.data < partition:
            current_node.next = None
            list_head.next = current_node
            list_head = current_node
            current_node = next_node

        else:
            current_node.next = None
            list_tail.next = current_node
            list_tail = current_node
            current_node = next_node


    if current_node.data < partition:
        current_node.next = None
        list_head.next = current_node
        list_head = current_node
        current_node = next_node

    else:
        current_node.next = None
        list_tail.next = current_node
        list_tail = current_node

    og_list_head = og_list_head.next
    og_list_tail = og_list_tail.next

    traverse(og_list_head)
    traverse(og_list_tail)
    print(list_head.data)
    print(list_head.next)

    list_head.next = og_list_tail
    return og_list_head


basic_list_head = Node(4)
basic_list_head.next = Node(3)
basic_list_head.next.next = Node(1)
basic_list_head.next.next.next = Node(2)
basic_list_head.next.next.next.next = Node(6)
basic_list_head.next.next.next.next.next = Node(5)

traverse(basic_list_head)
traverse(partition(basic_list_head, 4))
