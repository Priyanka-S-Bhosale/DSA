#recursion
# def f(i,W, wt,val):
#     if i ==0:
#         if wt[0] <= W:
#             return val[0]
#         else:
#             return 0 
#     notPick = 0 + f(i-1,W, wt, val)
#     pick = float('-inf')
#     if wt[i] <= W:
#         pick = val[i] + f(i-1, W - wt[i], wt, val)
#     return max(pick,notPick)


# wt = [1, 2, 4, 5]
# val = [5, 4, 8, 6]
# W = 5
# n = len(wt)
# print(f(n-1,W, wt, val))

#memoize

# def f(i,W, wt,val,dp):
#     if i ==0:
#         if wt[0] <= W:
#             return val[0]
#         else:
#             return 0 
#     if dp[i][W] != float('-inf'):
#         return dp[i][W]
#     notPick = 0 + f(i-1,W, wt,val,dp)
#     pick = float('-inf')
#     if wt[i] <= W:
#         pick = val[i] + f(i-1,W-wt[i], wt,val,dp)
#     dp[i][W] = max(pick,notPick)
#     return dp[i][W]


# wt = [1, 2, 4, 5]
# val = [5, 4, 8, 6]
# W = 5
# n = len(wt)
# dp = [[float('-inf')]*(W+1) for i in range(n)]
# print(f(n-1,W, wt, val,dp))

# def f(i,W, wt,val,dp):
#     if i ==0:
#         if wt[0] <= W:
#             return val[0]
#         else:
#             return 0 
#     if dp[i][W] != float('-inf'):
#         return dp[i][W]
#     notPick = 0 + f(i-1,W, wt,val,dp)
#     pick = float('-inf')
#     if wt[i] <= W:
#         pick = val[i] + f(i-1,W-wt[i], wt,val,dp)
#     dp[i][W] = max(pick,notPick)
#     return dp[i][W]


# wt = [1, 2, 4, 5]
# val = [5, 4, 8, 6]
# W = 5
# n = len(wt)
# dp = [[float('-inf')]*(W+1) for i in range(n)]
# print(f(n-1,W, wt, val,dp))


def f(i,W, wt,val,dp):
    for i in range(wt[0], W):
        dp[0][i] = val[0]
    for i in range(1,n):
        for j in range(W+1):
            notPick = 0 + dp[i-1][j]
            pick = float('-inf')
            if wt[i] <= j:
                pick = val[i] + dp[i-1][j - wt[i]]
            dp[i][j] = max(pick,notPick)
    return dp[n-1][W]


wt = [1, 2, 4, 5]
val = [5, 4, 8, 6]
W = 5
n = len(wt)
dp = [[float('-inf')]*(W+1) for i in range(n)]
print(f(n-1,W, wt, val,dp))
