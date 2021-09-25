str="adceca"

dp=[[0  for i in range(len(str))] for j in range(len(str))]
for j in range(len(str)-1,-1,-1):
    for i in range(j,len(str)):
        if i==j:
            dp[j][i]=1
        elif str[i]==str[j]:
            dp[j][i] = dp[j+1][i-1]+2
        else:
            dp[j][i] = max(dp[j][i - 1] ,dp[j+1][i])
for item in dp:
    print(item)