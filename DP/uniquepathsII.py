#https://leetcode.com/problems/unique-paths-ii/
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        #recursion
        # def f(i,j,obstacleGrid):
        #     if i >= 0 and j >= 0 and obstacleGrid[i][j] == 1:
        #         return 0
        #     if i == 0 and j ==0:
        #         return 1
        #     if i <0 or j <0:
        #         return 0
            
        #     up = f(i-1,j,obstacleGrid)
        #     left = f(i,j-1,obstacleGrid)

        #     return up+left
        # m = len(obstacleGrid)
        # n = len(obstacleGrid[0])
        # return f(m-1, n-1, obstacleGrid)

        #memoization
        def f(i,j,dp):
            if i >= 0 and j >= 0 and obstacleGrid[i][j] == 1:
                return 0
            if i == 0 and j ==0:
                return 1
            if i <0 or j <0:
                return 0
            if dp[i][j]!= -1:
                return dp[i][j]
            up = f(i-1,j,dp)
            left = f(i,j-1,dp)
            dp[i][j] = up + left

            return dp[i][j]
        
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[-1]*(n+1) for j in range(m+1)]
        return f(m-1,n-1, dp)
