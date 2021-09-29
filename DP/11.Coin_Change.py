# max no of ways
coins=[2,3,4]
sum=7
dp=[[0 for i in range(sum+1)] for j in range(len(coins)+1)]
for j in range(len(coins)+1):
    dp[j][0]=1
for j in range(1,len(coins)+1):
    for i in range(1,sum+1):
        if i-coins[j-1]>=0:
            dp[j][i] = dp[j][i-coins[j-1]] + dp[j-1][i]
        else:
            dp[j][i] = dp[j - 1][i]

print(dp[-1][-1])