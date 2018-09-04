"""
Create a binary tree
            D
        /       \
    B            E
  /   \            \
A      C            F
"""
class Queue:
    def __init__(self):
        self.items = []

    def enque(self,item):
        self.items.insert(0,item)

    def deque(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def isempty(self):
        return self.items == []

    def size(self):
        return len(self.items)

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)


def print_tree(root,traversal_type):
    if traversal_type == 'preorder':
        return preorder(root)
    elif traversal_type == 'inorder':
        return inorder(root)
    elif traversal_type == 'postorder':
        return postorder(root)
    elif traversal_type == 'levelorder':
        return levelorder(root)


def preorder(root):
    traversal = ''
    if root:
        traversal += (str(root.data) + ' . ')
        traversal += preorder(root.left)
        traversal += preorder(root.right)
    return traversal


def preorder_search(root,find_value):
    if root:
        if root.data == find_value:
            return True
        else:
            return preorder_search(root.left,find_value) or preorder_search(root.right,find_value)
    return False

def inorder(root):
    traversal = ''
    if root:
        traversal += inorder(root.left)
        traversal += (str(root.data) + ' . ')
        traversal += inorder(root.right)
    return traversal


def postorder(root):
    traversal = ''
    if root:
        traversal += postorder(root.left)
        traversal += postorder(root.right)
        traversal += (str(root.data) + ' . ')

    return traversal


def levelorder(root):
    traversal = ''
    data_queue = Queue()
    if root:
        data_queue.enque(root)
        while not data_queue.isempty():
            current_node = data_queue.deque()
            traversal += (str(current_node.data) + ' . ')
            if current_node.left:
                data_queue.enque(current_node.left)
            if current_node.right:
                data_queue.enque(current_node.right)
    return traversal


if __name__ == '__main__':
    tree = BinaryTree('D').root
    tree.left = Node('B')
    tree.left.left = Node('A')
    tree.left.right = Node('C')
    tree.right = Node('E')
    tree.right.right = Node('F')

    print(print_tree(tree, 'preorder'))
    print(print_tree(tree, 'inorder'))
    print(print_tree(tree, 'postorder'))
    print(print_tree(tree, 'levelorder'))

    print(preorder_search(tree, 'G'))
    print(preorder_search(tree, 'F'))
