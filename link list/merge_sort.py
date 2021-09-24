class LinkedList:
    def __init__(self):
        self.head=None

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

l1=LinkedList()
l2=LinkedList()
new_list=LinkedList()
l1_prev=None
l2_prev=None
def sum_list(l1,l2):
    if l1.next and l2.next:
        sum_list(l1.next,l2.next)
    elif l1.next:
        pass
    elif l2.next:
        pass
    else:
        pass