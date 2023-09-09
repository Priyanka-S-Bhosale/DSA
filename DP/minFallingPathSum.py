#https://leetcode.com/problems/minimum-falling-path-sum/
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        #recursion
        # def f(i,j,matrix):
        #     if j<0 or j >=len(matrix[0]):
        #         return float('inf')
        #     if i == 0:
        #         return matrix[i][j]
            
        #     up = matrix[i][j] + f(i-1,j,matrix)
        #     leftDiag = matrix[i][j] + f(i-1,j-1,matrix)
        #     rightDiag = matrix[i][j] + f(i-1,j+1,matrix)

        #     return min(up, min(leftDiag, rightDiag))
        

        # n = len(matrix)
        # m = len(matrix[0])
        # mini = float('inf')
        # for i in range(m): #start from columns0-m and it can end at any last row at any column
        #     mini = min(mini, f(n-1,i,matrix) )
        # return mini

        #memoization

        # def f(i,j,matrix,dp):
        #     if j<0 or j >=len(matrix[0]):
        #         return float('inf')
        #     if i == 0:
        #         return matrix[i][j]
        #     if dp[i][j] != float('inf'):
        #         return dp[i][j]            
        #     up = matrix[i][j] + f(i-1,j,matrix,dp)
        #     leftDiag = matrix[i][j] + f(i-1,j-1,matrix,dp)
        #     rightDiag = matrix[i][j] + f(i-1,j+1,matrix,dp)
        #     dp[i][j] = min(up, leftDiag, rightDiag)

        #     return dp[i][j] 
        
        # n = len(matrix)
        # m = len(matrix[0])
        # dp = [[float('inf')]*(n+1) for i in range(n+1)]
        # mini = float('inf')
        # for i in range(m): #start from columns0-m and it can end at any last row at any column
        #     mini = min(mini, f(n-1,i,matrix,dp) )
        # return mini

        #tabulation
        mini = float('inf')
        n = len(matrix)
        m = len(matrix[0])
        dp = [[float('inf')]*(n+1) for i in range(n+1)]
        for j in range(len(matrix)):
            dp[0][j] = matrix[0][j]
        for i in range(1,n):
            for j in range(m):         
                up = matrix[i][j] + dp[i-1][j]
                leftDiag = matrix[i][j]
                if (j-1) >=0:
                    leftDiag +=dp[i-1][j-1]
                else:
                    leftDiag +=float('inf')
                rightDiag = matrix[i][j]
                if (j+1) <len(matrix):
                    rightDiag += dp[i-1][j+1]
                else:
                    rightDiag +=float('inf')
                dp[i][j] = min(up, leftDiag, rightDiag)
        
        for i in range(m): #start from columns0-m and it can end at any last row at any column
            mini = min(mini, dp[n-1][i])
        return mini

    #Space optimization
        # mini = float('inf')
        # n = len(matrix)
        # m = len(matrix[0])
        # prev = [float('inf')]*m
        # curr = [float('inf')]*m
        # for j in range(len(matrix)):
        #     prev[j] = matrix[0][j]
        # for i in range(1,n):
        #     for j in range(m):         
        #         up = matrix[i][j] + prev[j]
        #         leftDiag = matrix[i][j]
        #         if (j-1) >=0:
        #             leftDiag +=prev[j-1]
        #         else:
        #             leftDiag +=float('inf')
        #         rightDiag = matrix[i][j]
        #         if (j+1) <len(matrix):
        #             rightDiag += prev[j+1]
        #         else:
        #             rightDiag +=float('inf')
        #         curr[j] = min(up, leftDiag, rightDiag)
        #     prev = curr
        
        # for i in range(m): #start from columns0-m and it can end at any last row at any column
        #     mini = min(mini, prev[i])
        # return mini
            
