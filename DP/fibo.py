#https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, n: int) -> int:
        #Recrursion
        # if n <=1:
        #     return n
        # return self.fib(n-1) + self.fib(n-2)

        #Top Down
        # def fibo(n,dp):
        #     if n<=1:
        #         return n
        #     if dp[n] != -1:
        #         return dp[n]
        #     dp[n] = fibo(n-1,dp) + fibo(n-2,dp)
        #     return dp[n]
    
        # dp = [-1]*(n+1)
        # return fibo(n,dp)

        #Bottom Up

        # def fibo(n,dp):
        #     dp[0] = 0
        #     if n >= 1:
        #         dp[1] = 1
        #     for i in range(2,n+1):
        #         dp[i] = dp[i-1] + dp[i-2]
        #     return dp[n]
    
        # dp = [-1]*(n+1)
        # return fibo(n,dp)

        #Space oprimized

        def fibo(n):
            prev2 = 0
            if n== 0:
                return prev2
            prev1 = 1
            
            for i in range(2,n+1):
                curr = prev1 + prev2
                prev2 = prev1
                prev1 = curr
            return prev1
    
        return fibo(n)
