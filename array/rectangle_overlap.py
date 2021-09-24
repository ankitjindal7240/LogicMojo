class point():
    def __init__(self,x,y):
        self.x=x
        self.y=y

def overlap(l1,l2,r1,r2):
    if r1.x<l2.x or r2.x <l1.x:
        return False
    if r1.y> l2.y or r2.y>l1.y:
        return False
    return True

