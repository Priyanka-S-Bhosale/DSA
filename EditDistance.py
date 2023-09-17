#https://leetcode.com/problems/edit-distance/

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # def f(i,j):
        #     if i<0: return j+1
        #     if j<0: return i+1

        #     if word1[i] == word2[j]:
        #         return 0 + f(i-1, j-1)
            
        #     #insert 
        #     a =  1 + f(i, j-1)

        #     #delete
        #     b = 1 + f(i-1,j)

        #     #replcae
        #     c = 1 + f(i-1,j-1)

        #     return min(a,b,c)
        # n = len(word1)
        # m = len(word2)
        # return f(n-1, m-1)

        # def f(i, j, dp):
        #     if i == 0:
        #         return j
        #     if j == 0:
        #         return i

        #     if dp[i][j] != -1:
        #         return dp[i][j]
            
        #     if word1[i - 1] == word2[j - 1]:
        #         dp[i][j] = f(i - 1, j - 1, dp)
        #     else:
        #         insert = 1 + f(i, j - 1, dp)
        #         delete = 1 + f(i - 1, j, dp)
        #         replace = 1 + f(i - 1, j - 1, dp)
        #         dp[i][j] = min(insert, delete, replace)

        #     return dp[i][j]
        # n = len(word1)
        # m = len(word2)
        # dp = [[-1] * (m + 1) for _ in range(n + 1)]
        # return f(n, m,dp)
        n = len(word1)
        m = len(word2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            for j in range(m + 1):
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                elif word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    insert = 1 + dp[i][j - 1]
                    delete = 1 + dp[i - 1][j]
                    replace = 1 + dp[i - 1][j - 1]
                    dp[i][j] = min(insert, delete, replace)

        return dp[n][m]
