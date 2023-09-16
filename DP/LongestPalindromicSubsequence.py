
text1 = "bbbab"
text2 = text1[::-1]
n = len(text1)
m = len(text2)
dp = [[0]*(m+1) for _ in range(n+1)]
#both same
for i in range(n):
    dp[i][0] = 0
for j in range(m):
    dp[0][j] = 0
for i in range(1,n+1):
    for j in range(1,m+1):
        if text1[i-1] == text2[j-1]:
            dp[i][j] = 1 + dp[i-1][j-1]
        else:
            dp[i][j] = max (dp[i-1][j],dp[i][j-1])
print(dp[n][m])
