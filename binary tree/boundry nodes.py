class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
root = Node(1)
root.left = Node(2)
root.right = Node(23)
root.right.right = Node(32)
root.right.right.right = Node(34)
root.left.left = Node(4)
root.left.left.left= Node(9)
root.left.right = Node(5)
root.left.right.right = Node(7)
root.left.right.right.right = Node(10)
root.left.right.right.right.right = Node(11)
root.left.right.left = Node(6)
root.left.right.left.left = Node(12)
root.left.right.left.left.right = Node(19)

def left_nodes(root):
    if Node==None:
        return
    elif root.left != None:
        print(root.val)
        left_nodes(root.left)
    elif root.right != None:
        print(root.val)
        left_nodes(root.right)

def leaves(root):
    if root==None:
        return
    if root.left ==None and root.right==None:
        print(root.val)
        return
    leaves(root.left)
    leaves(root.right)

def right_nodes(root):
    if Node==None:
        return
    elif root.right != None:
        right_nodes(root.right)
        print(root.val)

    elif root.right != None:
        right_nodes(root.left)
        print(root.val)


left_nodes(root.left)
leaves(root)
right_nodes(root.right)

a=float('inf')
print(a)