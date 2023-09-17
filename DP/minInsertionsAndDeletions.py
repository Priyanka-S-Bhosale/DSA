#https://www.codingninjas.com/studio/problems/can-you-make_4244510?leftPanelTab=1

def canYouMake(s1: str, s2: str) -> int:
    # write your code here
    def f(text1, text2):
        n = len(text1)
        m = len(text2)
        dp = [[0]*(m+1) for _ in range(n+1)]
        #both same
        for i in range(n):
            dp[i][0] = 0
        for j in range(m):
            dp[0][j] = 0
        for i in range(1,n+1):
            for j in range(1,m+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max (dp[i-1][j],dp[i][j-1])
        return dp[n][m]
    
    lcs = f(s1,s2)
    n = len(s1)
    m = len(s2)
    insertions = n - lcs
    deletions = m - lcs
    return insertions + deletions
