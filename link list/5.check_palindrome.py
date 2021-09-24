length_odd =0
def mid(linkedlist):
        prev,slow,fast=linkedlist.head
        while fast!=None and fast.next!=None:
            prev=slow
            slow=slow.next
            fast=fast.next.next
        if fast!=None:
            global length_odd
            length_odd=1
        prev.next=None
        return slow

def reverse(linkedlist):
    prev=None
    current=linkedlist.head
    while current!=None:
        next=current.next
        current.next=prev
        prev=current
        current=next
    linkedlist.head=prev
def comapre(first_half ,second_half):
    while first_half!=None and second_half!=None:
        if first_half.data!=second_half.data:
            return "no"
        first_half=first_half.next
        second_half=second_half.next
    if first_half ==None and second_half==None:
        return "yes"
def palindrome(linkedlist):
    second_half=mid(linkedlist)
    first_half=linkedlist
    if length_odd==1:
        second_half=second_half.next
    reverse(second_half)
    return comapre(first_half,second_half)

