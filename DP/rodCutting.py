#https://www.codingninjas.com/studio/problems/rod-cutting-problem_800284?source=youtube&campaign=striver_dp_videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_dp_videos&leftPanelTab=1

from sys import stdin
import sys

# def cutRod(i,price, n, dp):

    # Write your code here.
    #recursion
    # if i == 0:
    #     return n* price[0]

    # notPick = 0+ cutRod(i-1,price,n)
    # rodLength = i+1

    # pick = float('-inf')
    # if rodLength <= n:
    #     pick = price[i] + cutRod(i, price,n- rodLength)
    # return max(pick, notPick)

    #memoize

    # if i == 0:
    #     return n* price[0]
    # if dp[i][n] != float('-inf'):
    #     return dp[i][n]
    # notPick = 0+ cutRod(i-1,price,n,dp)
    # rodLength = i+1

    # pick = float('-inf')
    # if rodLength <= n:
    #     pick = price[i] + cutRod(i, price,n- rodLength,dp)
    # dp[i][n] = max(pick, notPick)
    # return dp[i][n]

    #tabulation
def cutRod(price, n):
    dp = [[0] * (n + 1) for _ in range(len(price) + 1)]

    for i in range(len(price) + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif i <= j:
                dp[i][j] = max(dp[i - 1][j], price[i - 1] + dp[i][j - i])
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[len(price)][n]



# Taking input using fast I/O.
def takeInput():
    n = int(input())

    price = list(map(int, input().strip().split(" ")))

    return price, n


# Main.
t = int(input())
while t:
    price, n = takeInput()
    dp = [[float('-inf')]* (n+1) for j in range(n+1)]
    print(cutRod(price, n))
    t = t-1
