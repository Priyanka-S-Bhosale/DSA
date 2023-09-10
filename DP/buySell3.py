#https://www.codingninjas.com/studio/problems/buy-and-sell-stock_1071012?source=youtube&campaign=striver_dp_videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_dp_videos&leftPanelTab=1
#https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # def f(i,buy,cap,dp):
        #     if i == n or cap ==0:
        #         return 0
        #     profit = 0
        #     if dp[i][buy][cap] != 0:
        #         return dp[i][buy][cap]
        #     if buy:
        #         profit = max(-prices[i] + f(i+1, 0, cap,dp),
        #         0 + f(i+1, 1, cap,dp))
        #         dp[i][buy][cap] = profit
        #         return dp[i][buy][cap]
            
        #     else:
        #         profit = max(prices[i] + f(i+1, 1, cap -1,dp),
        #         0 + f(i+1, 0, cap,dp))
        #         dp[i][buy][cap] = profit
        #         return dp[i][buy][cap]


        n = len(prices)
        # dp = [[[0] * 3 for _ in range(2)] for _ in range(n)]#cap, buy,len
        # return f(0,1,2,dp)

        dp=[[[0 for i in range(3)]for j in range(2)]for k in range(n+1)]
        for ind in range(n-1,-1,-1):
            for buy in range(2):
                for cap in range(1,3):
                    if buy==1:
                        dp[ind][buy][cap]=max(-prices[ind]+dp[ind+1][0][cap],0+dp[ind+1][1][cap])
                    else:
                        dp[ind][buy][cap]=max(prices[ind]+dp[ind+1][1][cap-1],0+dp[ind+1][0][cap])
        return dp[0][1][2]
