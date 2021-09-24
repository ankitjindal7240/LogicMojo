class LL():
    def __init__(self,data):
        LL.data=data
        LL.next=None

class DLL():
    def __init__(self,data):
        DLL.data=data
        DLL.next=None
        DLL.prev=None



n1=LL(1)
n2=LL(2)
n1.next=n2
print(n1.next.data)

n3=DLL(1)
n4=DLL(2)
n5=DLL(3)

n3.next=n4
n4.next=n5
n4.prev=n3
n5.prev=n4

print()