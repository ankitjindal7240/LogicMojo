def sub_sets(arr,index,curr,size,result):
    if len(curr)==size:
        result.append(list(curr))
    for i in range(index,len(arr)):
        curr.append(arr[i])
        sub_sets(arr,i+1,curr,size,result)
        curr.pop()

def power_set(arr):
    result=[]
    curr=[]
    for set_len in range(len(arr)):
        sub_sets(arr,0,curr,set_len,result)

    print(result)

arr=[1,2,3,4]
power_set(arr)

