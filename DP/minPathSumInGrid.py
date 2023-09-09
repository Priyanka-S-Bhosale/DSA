#https://leetcode.com/problems/minimum-path-sum/

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        #recursion

        # def f(i,j,grid):
        #     if i == 0 and j == 0:
        #         return grid[0][0]
        #     if i<0 or j<0:
        #         return float('inf')
            
        #     up =  grid[i][j] + f(i-1,j, grid)
        #     left = grid[i][j] + f(i,j-1, grid)
        #     return min(up,left) 
        # n = len(grid)
        # m = len(grid[0])
        # return f(n-1,m-1,grid)

        #memoization

        # def f(i,j,grid,dp):
        #     if i == 0 and j == 0:
        #         return grid[0][0]
        #     if i<0 or j<0:
        #         return float('inf')
        #     if dp[i][j] != float('inf'):
        #         return dp[i][j]
        #     up =  grid[i][j] + f(i-1,j, grid,dp)
        #     left = grid[i][j] + f(i,j-1, grid,dp)
        #     dp[i][j] = min(up,left)
        #     return dp[i][j] 
        # n = len(grid)
        # m = len(grid[0])
        # dp = [[float('inf')]*(m+1) for j in range(n+1)]
        # return f(n-1,m-1,grid, dp)

        #tabulation
        n = len(grid)
        m = len(grid[0])
        dp = [[float('inf')]*(m+1) for j in range(n+1)]
        
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    dp[0][0] = grid[0][0]
                else:
                    up =  grid[i][j]
                    if (i>0):
                        up +=dp[i-1][j]
                    else:
                        up += float('inf')
                    left =  grid[i][j]
                    if j >0:
                        left +=  dp[i][j-1]
                    else:
                        left += float('inf')
                    dp[i][j] = min(up,left)
        return dp[n-1][m-1] 
        
