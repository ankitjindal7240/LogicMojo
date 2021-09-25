s = "catscat"
wordDict = {"cats","dog","sand","and","cat"}
dp=[[0 for i in range(len(s))] for j in range(len(s))]
# for i in range(len(s)):
#     dp[0][i]=i
#     dp[i][0]=i

for column in range(len(s)):
    for row in range(column+1):
        if row==column and s[:row+1] in wordDict:
            dp[column][row]=1

        elif (s[column-row:column+1] in wordDict ) and dp[column-row-1][column-row-1]:
            dp[column][column]=1
            break
for item in dp:
    print(item)