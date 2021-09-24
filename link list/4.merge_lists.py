def merge(first,second):
    if first==None:
        return second
    if second==None:
        return first
    if first.data <= second.data:
        temp=first
        first=first.next
    else:
        temp = second
        second = second.next

    new_list=temp
    while first!=None and second!=None:
        if first.data <= second.data:
            temp.next = first
            first = first.next
        else:
            temp.next = second
            second = second.next
        temp = temp.next
    if first!=None:
        temp.next=first
    if second!=None:
        temp.next=second
    return new_list
