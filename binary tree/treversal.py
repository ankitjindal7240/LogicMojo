class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# def inorder(root):
#     if root:
#         inorder(root.left)
#         print(root.val)
#         inorder(root.right)


flag=0
parent=Node(None)
def convertDLL(node):
    global flag
    global parent
    if node:
        convertDLL(node.left)
        if flag:
            parent.right=node
            node.left=parent
            parent=node
        else:
            parent=node
            flag=flag+1
        convertDLL(node.right)
convertDLL(root)

while root.right:
    print(root.val)
    root=root.right