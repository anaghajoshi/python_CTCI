"""
Remove Dups: Write code to remove duplicates from an unsorted linked list.

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


def remove_duplicate_nodes(head_node):

    if head_node is None:
        return

    current_node = head_node
    seen_set = set()
    seen_set.add(current_node.data)
    while current_node.next:
        prev_node = current_node
        current_node = current_node.next

        if current_node.data in seen_set:
            prev_node.next = current_node.next
        else:
            seen_set.add(current_node.data)

    return head_node


def remove_duplicate_nodes_followup(head_node):
    if head_node is None:
        return

    unique_node = head_node
    while unique_node.next:
        current_node = unique_node
        while current_node.next:
            if current_node.next.data == unique_node.data:
                current_node.next = current_node.next.next
            else:
                current_node = current_node.next
        unique_node = unique_node.next

    return head_node


basic_list_head = Node(1)
basic_list_head.next = Node(2)
basic_list_head.next.next = Node(1)
basic_list_head.next.next.next = Node(3)
basic_list_head.next.next.next.next = Node(4)
basic_list_head.next.next.next.next.next = Node(1)

traverse(basic_list_head)
remove_duplicate_nodes(basic_list_head)
traverse(basic_list_head)


basic_list_head = Node(1)
basic_list_head.next = Node(2)
basic_list_head.next.next = Node(1)
basic_list_head.next.next.next = Node(3)
basic_list_head.next.next.next.next = Node(4)
basic_list_head.next.next.next.next.next = Node(1)

traverse(basic_list_head)
remove_duplicate_nodes_followup(basic_list_head)
traverse(basic_list_head)
