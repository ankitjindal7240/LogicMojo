class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

root = Node(6)
root.right = Node(10)
root.right.left = Node(8)
root.right.right = Node(12)
root.right.right.left = Node(11)
root.left = Node(4)
root.left.right = Node(5)

def inorder_succesor(root):
    while root.left != None:
        root=root.left
    return root
def delete_node(root,key):
        if root==None:
            return root
        elif root.val>key:
            root.left = delete_node(root.left ,key)
        elif root.val<key:
            root.right = delete_node(root.right, key)
        else:

            if root.left==None and root.right==None:
                return None
            elif root.left==None:
                temp=root.right
                root=None
                return temp
            elif root.right==None:
                temp = root.left
                root = None
                return temp
            else:
                temp=inorder_succesor(root.right)
                root.val=temp.val
                root.right=delete_node(root.right,temp.val)

        return root

def inorder(root):
    if root is not None:
        inorder(root.left)
        print (root.val)
        inorder(root.right)

delete_node(root,10)
inorder(root)


