#https://www.codingninjas.com/studio/problems/selling-stock_630282?source=youtube&campaign=striver_dp_videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_dp_videos&leftPanelTab=0


from sys import stdin


def getMaximumProfit(values, n) :
	#Your code goes here
    #recursion
    # def f(i,buy):
    #     if i == n:
    #         return 0
    #     profit = 0
    #     if buy:
    #         profit = max(-values[i] + f(i+1, 0),
    #          0 + f(i+1, 1))
        
    #     else:
    #         profit = max(values[i] + f(i+1, 1),
    #          0 + f(i+1, 0))
        
    #     return profit

    
    # return f(0, 1)

    # def findstock(idx,buy,arr,dp):
    #     if idx==n:return 0
    #     if dp[idx][buy]!=-1:return dp[idx][buy]
    #     if buy:
    #         profit=max(-arr[idx]+findstock(idx+1,0,arr,dp),0+findstock(idx+1,1,arr,dp))
    #         dp[idx][buy]=profit
    #         return dp[idx][buy]
    #     else:
    #         profit=max(arr[idx]+findstock(idx+1,1,arr,dp),0+findstock(idx+1,0,arr,dp))
    #         dp[idx][buy]=profit
    #         return dp[idx][buy]


    # buy=1
    # dp=[[-1]*2 for _ in range(len(values))]
    # return findstock(0,buy,values,dp)

    dp = [[0] * 2 for _ in range(n + 1)]

    for i in range(n - 1, -1, -1):
        for j in range(2):
            if j == 0:
                dp[i][j] = max(values[i] + dp[i + 1][1], 0 + dp[i + 1][0])
            else:
                dp[i][j] = max(-values[i] + dp[i + 1][0], 0 + dp[i + 1][1])

    return dp[0][1]































#taking input using fast I/O
def takeInput() :
    n = int(stdin.readline().rstrip())

    if n == 0 :
        return list(), 0

    values = list(map(int, stdin.readline().rstrip().split(" ")))
    return values, n


#main
t = int(stdin.readline().rstrip())

while t > 0 :
    values, n = takeInput()
    print(getMaximumProfit(values, n))
    t -= 1
