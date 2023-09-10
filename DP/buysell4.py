#https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/description/

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp=[[[0 for i in range(k+1)]for j in range(2)]for l in range(n+1)]
        for ind in range(n-1,-1,-1):
            for buy in range(2):
                for cap in range(1,k+1):
                    if buy==1:
                        dp[ind][buy][cap]=max(-prices[ind]+dp[ind+1][0][cap],0+dp[ind+1][1][cap])
                    else:
                        dp[ind][buy][cap]=max(prices[ind]+dp[ind+1][1][cap-1],0+dp[ind+1][0][cap])
        return dp[0][1][k]
        
