#https://leetcode.com/problems/triangle/

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        #start at index 0,0 and ending is variable
    #recursion
        # def f(i,j,triangle):
        #     if i == n-1: #reached last row so return values
        #         return triangle[n-1][j]
            
        #     down = triangle[i][j] + f(i+1,j,triangle)
        #     diagonal = triangle[i][j] + f(i+1,j+1, triangle)

        #     return min(down,diagonal)    

        # n = len(triangle)
        # m = len(triangle[0])
        # return f(0,0,triangle)

    #memoization

        # def f(i,j,triangle,dp):
        #     if i == n-1: #reached last row so return values
        #         return triangle[n-1][j]
        #     if dp[i][j] !=  -1:
        #         return dp[i][j]
        #     down = triangle[i][j] + f(i+1,j,triangle,dp)
        #     diagonal = triangle[i][j] + f(i+1,j+1, triangle,dp)
        #     dp[i][j] = min(down,diagonal) 

        #     return dp[i][j]    

        # n = len(triangle)
        # dp = [[-1]*(n+1) for j in range(n+1)]
        # return f(0,0,triangle,dp)


    #tabulation

        n = len(triangle)
        dp = [[-1]*(n+1) for j in range(n+1)]
        for i in range(n):
            dp[n-1][i] = triangle[n-1][i]
        for i in range(n-2,-1,-1):
            for j in range(i,-1,-1):
                down = triangle[i][j] + dp[i+1][j]
                diagonal = triangle[i][j] + dp[i+1][j+1]
                dp[i][j] = min(down,diagonal) 

        return dp[0][0]    

        #space optimization

        # n = len(triangle)
        # prev = [-1]*(n)
        # curr = [0]*(n)
        # for i in range(n):
        #     prev[i] = triangle[n-1][i]
        # for i in range(n-2,-1,-1):
        #     for j in range(i,-1,-1):
        #         down = triangle[i][j] + prev[j]
        #         diagonal = triangle[i][j] + prev[j+1]
        #         curr[j] = min(down,diagonal) 
        #     prev = curr

        # return prev[0]  
