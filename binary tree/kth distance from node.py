class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

root = Node(1)
root.right = Node(23)
root.right.right = Node(32)

root.left = Node(2)
root.left.right = Node(5)
root.left.right.right = Node(7)
root.left.right.right.right = Node(10)
root.left.right.right.right.right = Node(11)
root.left.right.left = Node(6)
root.left.right.left.left = Node(12)
root.left.right.left.left.right = Node(19)
root.left.left = Node(4)
root.left.left.left = Node(9)


def print_down(root,k):
    if root:
        if k==0:
            print( root.val)
            return

        print_down(root.left,k-1)
        print_down(root.right,k-1)

def kth_distance(root,k,value):
    if root==None:
        return -1
    if root.val==value:
        print_down(root,k)
        return 1
    else:
        dleft=kth_distance(root.left,k,value)
        if dleft!=(-1):
            if dleft==k:
                print(root.val)
                return 0
            print_down(root.right,k-dleft-1)
            return dleft+1






        dright=kth_distance(root.right,k,value)
        if dright!=(-1):
            if dleft==k:
                print(root.val)
                return 0
            print_down(root.left, k - dright - 1)
            return dright + 1
            pass
    return -1

kth_distance(root,3,5)