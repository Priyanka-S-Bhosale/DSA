#https://leetcode.com/problems/distinct-subsequences/

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # def f(i,j):
        #     if j < 0:
        #         return 1
        #     if i <0:
        #         return 0
        #     if s[i] == t[j]:
        #         return f(i-1,j-1) + f(i-1,j)
        #     else:
        #         return f(i-1,j)
        # n = len(s)
        # m = len(t)
        # return f(n-1,m-1)

        #memoize

        # def f(i,j,dp):
        #     if j < 0:
        #         return 1
        #     if i <0:
        #         return 0
        #     if dp[i][j] != -1:
        #         return dp[i][j]
        #     if s[i] == t[j]:
        #         dp[i][j] = f(i-1,j-1,dp) + f(i-1,j,dp)
        #         return dp[i][j]
        #     else:
        #         dp[i][j] =  f(i-1,j,dp)
        #         return dp[i][j]
        # n = len(s)
        # m = len(t)
        # dp = [[-1]*(m+1) for _ in range(n+1)]
        # return f(n-1,m-1,dp)

        #tabulation

        n = len(s)
        m = len(t)
        dp = [[0]*(m+1) for _ in range(n+1)]
        for j in range(m+1):
            dp[0][j] = 0
        for i in range(n+1):
            dp[i][0] = 1
        for i in range(1, n+1):
            for j in range(1,m+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] 
        return dp[n][m]
