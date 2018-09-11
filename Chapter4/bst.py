"""
Create a binary search tree
            5
        /       \
    3            8
  /          /      \
1           7       10

"""


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self, root):
        self.root = Node(root)


def inorder(root):
    traversal = ''
    if root:
        traversal += inorder(root.left)
        traversal += (str(root.data) + ' . ')
        traversal += inorder(root.right)
    return traversal


def BST_search(root, find_value):
    if root:
        if root.data == find_value:
            return True
        elif root.data < find_value:
            return BST_search(root.right, find_value)
        else:
            return BST_search(root.left, find_value)

    return False


if __name__ == '__main__':
    bst = BinarySearchTree(5)

    bst.root.left = Node(3)
    bst.root.left.left = Node(1)

    bst.root.right = Node(8)
    bst.root.right.left = Node(7)
    bst.root.right.right = Node(10)
    print(inorder(bst.root))

    print(BST_search(bst.root, 4))
    print(BST_search(bst.root, 7))

