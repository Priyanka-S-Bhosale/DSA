#recursion
# def f(i,target):
#     if i == 0:
#         return target == arr[i]
#     if target == 0:
#         return True
        
#     notPick = f(i-1, target)
#     pick = False
#     if arr[i] <= target:
#         pick = f(i-1, target - arr[i])
#     return pick or notPick

# arr= [1,2,3]
# k = 7
# n = len(arr)
# print(f(n-1, k))

#memoization

# def f(i,target, dp):
#     if i == 0:
#         return target == arr[i]
#     if target == 0:
#         return True
    
#     if dp[i][target] != False:
#         return dp[i][target]
        
#     notPick = f(i-1, target, dp)
#     pick = False
#     if arr[i] <= target:
#         pick = f(i-1, target - arr[i], dp)
#     dp[i][target] = pick or notPick
#     return dp[i][target]

# arr= [1,2,3]
# target = 6
# n = len(arr)
# dp = [[False]*(target + 1) for i in range(n +1)]
# print(f(n-1, target, dp))


#tabulation

def f(k, dp):
    dp[0][arr[0]] = True
    for i in range(n):
        dp[i][0] = True

    for i in range(1,n):
        for target in range(1,k+1):
            notPick = dp[i-1][target]
            pick = False
            if arr[i] <= target:
                pick = dp[i-1][target - arr[i]]
            dp[i][target] = pick or notPick
    return dp[n-1][target]

arr= [1,2,3]
k = 6
n = len(arr)
dp = [[False]*(k + 1) for i in range(n +1)]
print(f(k, dp))
