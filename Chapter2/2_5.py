"""
Sum Lists: You have two numbers represented by a linked list, where each node contains a single digit. The digits are stored in reverse order, such that the 1's digit is at the head of the list. Write a function that adds the two numbers and returns the sum as a linked list.
1
2
3 4} 5
return nullj
EXAMPLE
Input: (7-> 1 -> 6) + (5 -> 9 -> 2) .Thatis,617 + 295. Output:2 -> 1 -> 9.Thatis,912.
FOLLOW UP
Suppose the digits are stored in forward order. Repeat the above problem. Input: (6 -> 1 -> 7) + (2 -> 9 -> 5).Thatis,617 + 295. Output:9 -> 1 -> 2.Thatis,912.

"""
class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


def sum_list(list1, list2):
    carry = 0
    add_list = Node(None, None)
    add_list_head = add_list
    while list1.next and list2.next:
        print('digit ', list1.data, '+ digit ', list2.data, 'carry ', carry)
        digit_sum = list1.data + list2.data + carry
        carry = digit_sum//10
        digit_sum = digit_sum%10
        if add_list.data is None:
            add_list.data = digit_sum
        else:
            add_list.next = Node(digit_sum)
            add_list = add_list.next
        list1 = list1.next
        list2 = list2.next

    digit_sum = list1.data + list2.data + carry
    carry = digit_sum // 10
    digit_sum = digit_sum % 10
    add_list.next = Node(digit_sum)
    add_list = add_list.next
    if carry > 0:
        add_list.next = Node(carry)

    return add_list_head


def traverse(head_node):
    node = head_node
    while node.next:
        print(node.data, end=" -> ")
        node = node.next
    print(node.data)
    return


a_list = Node(7)
a_list.next = Node(1)
a_list.next.next = Node(6)

b_list = Node(5)
b_list.next = Node(9)
b_list.next.next = Node(2)

traverse(a_list)
traverse(b_list)
traverse(sum_list(a_list,b_list))

