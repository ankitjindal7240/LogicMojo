class LinkedList:
    def __init__(self):
        self.head=None

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

l1=LinkedList()

def insert(self,value):
    new_node=Node(value)
    if self.head==None:
        head=new_node
    else:
        temp=self.head
        while temp.next != None:
            temp=temp.next
        temp.next=new_node

insert(l1,5)
insert(l1,6)
insert(l1,7)
insert(l1,8)
insert(l1,9)
insert(l1,10)
insert(l1,11)


def delete(self,value):
    prev=self.head
    after=self.next
    while (after.next!=None) or prev.next.data !=value:
        prev=prev.next
        after=after.next
    if prev.next.data==value:
        prev.next=prev.next.next
    else:
        return

def search():
    pass

n1=Node(5)
n2=Node(6)
n3=Node(5)
n3.next=n2
