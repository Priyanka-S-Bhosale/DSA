#Same as Fibo

class Solution:
    
    def climbStairs(self, n: int) -> int:
        # recursive
        # if n == 0: return 1

        # if n == 1: return 1

        # left = self.climbStairs(n-1)
        # right = self.climbStairs(n-2)

        # return left + right

        #memoized
        # def findTotal(dp,n):
        #     if n <= 1: return 1
        #     if dp[n] != -1:
        #         return dp[n]
        #     dp[n] = findTotal(dp,n-1) + findTotal(dp,n-2)
        #     return dp[n]
        # dp = [-1] * (n+1)
        # return findTotal(dp,n)

        #Tabulation
        # def findTotal(dp,n):
        #     dp[0] = 1
        #     dp[1] = 1
        #     for i in range(2, n+1):
        #         dp[i] = dp[i-1] + dp[i-2]
        #     return dp[n]
        # dp = [-1] * (n+1)
        # return findTotal(dp,n)

        #memory optimized

        def findTotal(n):
            prev2 = 1
            prev1 = 1
            for i in range(2, n+1):
                curr = prev1 + prev2
                prev2 = prev1
                prev1 = curr
            return prev1
        return findTotal(n)
        
