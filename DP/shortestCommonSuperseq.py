# def f(text1, text2):
#     n = len(text1)
#     m = len(text2)
#     dp = [[0]*(m+1) for _ in range(n+1)]
#     #both same
#     for i in range(n):
#         dp[i][0] = 0
#     for j in range(m):
#         dp[0][j] = 0
#     for i in range(1,n+1):
#         for j in range(1,m+1):
#             if text1[i-1] == text2[j-1]:
#                 dp[i][j] = 1 + dp[i-1][j-1]
#             else:
#                 dp[i][j] = max (dp[i-1][j],dp[i][j-1])
#     return dp[n][m]
# s1= "brute"
# s2 = "groot"
# lcs = f(s1,s2)
# n = len(s1)
# m = len(s2)
# shortestCommonSuperseq = lcs + (n - lcs) + (m - lcs)
# print(shortestCommonSuperseq)

text1= "brute"
text2 = "groot"
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


i = len(text1)
j = len(text2)
arr = []
while i>0 and j>0:
    if text1[i-1] == text2[j-1]:
        arr.append(text1[i-1])
        i = i-1
        j = j-1
    
    elif dp[i-1][j] > dp[i][j-1]:
        arr.append(text1[i-1])
        i = i-1
    
    else:
        arr.append(text1[j-1])
        j = j-1
while i>0:
    arr.append(text1[i-1])
    i -=1
while j>0:
    arr.append(text1[j-1])
    j -=1


arr = arr[::-1]
string = "".join(arr)
print(string)
