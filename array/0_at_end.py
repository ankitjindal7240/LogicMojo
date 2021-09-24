arr=[1,3,0,0,4,0,9]
initial_index=0
next_swap=0
while next_swap<len(arr) and initial_index<len(arr):
    while arr[next_swap]==0 and next_swap<len(arr)-1:
        next_swap+=1
    if initial_index==next_swap and arr[initial_index]!=0:
        initial_index+=1
        next_swap+=1
    else:
        arr[initial_index],arr[next_swap]=arr[next_swap],arr[initial_index]
        initial_index=initial_index+1
print(arr)
