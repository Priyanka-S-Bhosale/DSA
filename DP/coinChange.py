#Min No of coins
# https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #recusrison
        # def f(i, target):
        #     # if i <0:
        #     #     return -1
        #     if i == 0:
        #         if target %coins[i] ==0:
        #             return target // coins[i]
        #         else:
        #             return maxsize

        #     notPick = 0 + f(i-1, target)

        #     pick = maxsize

        #     if coins[i] <= target:
        #         pick = 1 + f(i, target -coins[i])
            
        #     return min(pick, notPick)
        # n = len(coins)
        # if amount ==0:
        #     return 0
        # ans = f(n-1, amount)
        # if ans >=maxsize:
        #     return -1
        # return ans

        #memoize
        def f(i, target, dp):
            # if i <0:
            #     return -1
            if i == 0:
                if target %coins[i] ==0:
                    return target // coins[i]
                else:
                    return maxsize
            
            if dp[i][target] != -1:
                return dp[i][target]

            notPick = 0 + f(i-1, target,dp)

            pick = maxsize

            if coins[i] <= target:
                pick = 1 + f(i, target -coins[i],dp)
            dp[i][target] = min(pick, notPick)
            return dp[i][target]
        n = len(coins)
        if amount ==0:
            return 0
        dp=[[-1 for j in range(amount+1)] for i in range(n)]
        ans = f(n-1, amount, dp)
        if ans >=maxsize:
            return -1
        return ans
        
