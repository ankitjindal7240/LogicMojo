class Node:
    def __init__(self,value):
        self.left=None
        self.right=None
        self.value =value

#traversal

def treversal(node):
    if node==None:
        return
    treversal(node.left)
    treversal(node.right)
    