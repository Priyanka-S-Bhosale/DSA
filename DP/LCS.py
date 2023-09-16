#https://leetcode.com/problems/longest-common-subsequence/

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # def f(i,j):
        #     if i < 0 or j < 0:
        #         return 0 
        #     #both same
        #     if text1[i] == text2[j]:
        #         return 1 + f(i-1, j-1)
        #     return max(f(i-1, j), f(i, j-1))
        # n = len(text1)
        # m = len(text2)
        # return f(n-1,m-1)

        #memoize

        # def f(i,j,dp):
        #     if i < 0 or j < 0:
        #         return 0 
        #     if dp[i][j] != float('-inf'):
        #         return dp[i][j]
        #     #both same
        #     if text1[i] == text2[j]:
        #         dp[i][j] = 1 + f(i-1, j-1,dp)
        #         return dp[i][j]
        #     dp[i][j] = max(f(i-1, j,dp), f(i, j-1,dp))
        #     return dp[i][j]
        
        # n = len(text1)
        # m = len(text2)
        # dp = [[float('-inf')]*(m+1) for _ in range(n+1)]
        # return f(n-1,m-1,dp)
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
        return dp[n][m]
    
