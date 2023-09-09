#https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #recursion
        # def f(i,j):
        #     if i == 0 and j ==0:
        #         return 1
        #     if i <0 or j <0:
        #         return 0
            
        #     up = f(i-1,j)
        #     left = f(i,j-1)

        #     return up+left


        # return f(m-1,n-1)
        #memoization
        # def f(i,j,dp):
        #     if i == 0 and j ==0:
        #         return 1
        #     if i <0 or j <0:
        #         return 0
        #     if dp[i][j]!= -1:
        #         return dp[i][j]
        #     up = f(i-1,j,dp)
        #     left = f(i,j-1,dp)
        #     dp[i][j] = up + left

        #     return dp[i][j]

        # dp = [[-1]*(n+1) for j in range(m+1)]
        # return f(m-1,n-1, dp)

        #tabulation
        # dp = [[-1]*(n+1) for j in range(m+1)]
        # for i in range(m):
        #     for j in range(n):
        #         if i == 0 and j ==0:
        #             dp[i][j] = 1
        #         else:
        #             up = 0
        #             left = 0
        #             if i > 0:
        #                 up = dp[i-1][j]
        #             if j >0:
        #                 left = dp[i][j-1]
        #             dp[i][j] = up + left

        # return dp[m-1][n-1]

       # memory optimized

        prev = [-1]*n
        for i in range(m):
            curr = [-1]*n
            for j in range(n):
                if i == 0 and j ==0:
                    curr[j] = 1
                else:
                    up = 0
                    left = 0
                    if i > 0:
                        up = prev[j]
                    if j >0:
                        left = curr[j-1]
                    curr[j] = up + left
            prev = curr

        return prev[n-1]

    

        

