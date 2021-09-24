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


def IsLeaf(root):
    if root.right ==None and root.left==None:
        return True
    return False
arr=[]
printed=[]
def print_nodes(root,k,arr,printed,count):
    if root==None:
        return
    arr[count]=root.val
    printed[count]=False

    if IsLeaf(root) and (count-k) >= 0  and printed[count-k]==False:
        print(arr[count-k])
        printed[count-k]==True

        return

    print_nodes(root.left,k,arr,printed,count+1)
    print_nodes(root.right,k,arr,printed,count+1)