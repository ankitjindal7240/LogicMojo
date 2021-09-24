arr=[-2, -3, 4, -1, -2, 1, 5, -3]
max_sum=0
curr_sum=0
for i in range(len(arr)):
    curr_sum=arr[i] + curr_sum
    if curr_sum>max_sum:
        max_sum=curr_sum
    if curr_sum<0:
        curr_sum=0
print(max_sum)