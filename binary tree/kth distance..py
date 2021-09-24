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

def kth_distance(root,k):
    if root:
        if k==0:
            print( root.val)
            return

        kth_distance(root.left,k-1)
        kth_distance(root.right,k-1)

kth_distance(root,3)