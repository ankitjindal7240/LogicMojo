class DoublyLinkedList:
    def __init__(self):
        self.head=None

class Node:
    def __init__(self,data):
        self.prev=None
        self.next=None

l1=DoublyLinkedList()

def insert(self,value):
    new_node=Node(value)
    if self.head==None:
        self.head=new_node
    else:
        temp=self.head
        while temp.next!=None:
            temp=temp.next
        temp.next=new_node
        new_node.prev=temp


def delete(self,value):
    temp=self.head
    if self.head ==None:
        return
    else:
        while temp!=None:
            if temp.data==value:
                if temp==self.head:
                    self.head=temp.next
                elif temp.next!=None:
                    temp.prev.next=temp.next
                    temp.next.prev=temp.prev
                else:
                    temp.prev.next=None
            break
        temp.next


