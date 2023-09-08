from os import *
from sys import *
from collections import *
from math import *

from typing import *

  
def frogJump(n: int, heights: List[int]) -> int:
    #recursion
    # def f(i):

    #     if i ==0:
    #         return 0

    #     l = f(i-1) + abs(heights[i] - heights[i-1])
    #     r = float('inf')

    #     if i>1:
    #         r = f(i-2) + abs(heights[i] - heights[i-2])
        
    #     return min(l,r)
    
    # return f(n-1)

    #top down

    # def f(i,dp):

    #     if i ==0:
    #         return 0
    #     if dp[i] != float('inf'):
    #         return dp[i]

    #     l = f(i-1,dp) + abs(heights[i] - heights[i-1])
    #     r = float('inf')

    #     if i>1:
    #         r = f(i-2,dp) + abs(heights[i] - heights[i-2])
    #     dp[i] = min(l,r)
    #     return dp[i]
    
    # dp = [float('inf')] * (n+1)
    # return f(n-1, dp)

    #bottom up

    # def f(dp):

    #     dp[0] = 0
    #     for i in range(1, n):
    #         l = dp[i-1] + abs(heights[i] - heights[i-1])
    #         r = float('inf')

    #         if i>1:
    #             r = dp[i-2] + abs(heights[i] - heights[i-2])
    #         dp[i] = min(l,r)
    #     return dp[n-1]
    
    # dp = [float('inf')] * (n+1)
    # return f(dp)

    #Space optimized

    def f(dp):

        prev2 = 0
        prev1 = 0
        for i in range(1, n):
            l = prev1 + abs(heights[i] - heights[i-1])
            r = float('inf')

            if i>1:
                r = prev2 + abs(heights[i] - heights[i-2])
            curr = min(l,r)
            prev2 = prev1
            prev1 = curr
        return prev1
    
    dp = [float('inf')] * (n+1)
    return f(dp)







    

    
