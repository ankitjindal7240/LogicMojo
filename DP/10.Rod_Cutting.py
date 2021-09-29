length=[1,2,3,4]
price=[2,5,7,8]
n=len(price)
max_len=5
# recursive
def max_profit(price,length,n,max_len):
    if n==0  :
        return 0
    if max_len-length[n-1]>=0:
        return  max((price[n-1]+max_profit(price,length,n,max_len-length[n-1])),
                (max_profit(price,length,n-1,max_len)))
    else:
        return max_profit(price,length,n-1,max_len)

print(max_profit(price,length,n,max_len))


# DP
t=[[0 for i in range(max_len+1)] for j in range(n+1)]
for item in t:
    print(item)
for j in range(1,n+1):
    for i in range(1,max_len+1):
        if i-length[j-1]>=0:
            t[j][i]= max( price[j-1]+ t[j][i-length[j-1]], t[j-1][i])

        else: t[j][i]= t[j-1][i]


print(t[-1][-1])