#https://www.codingninjas.com/studio/problems/longest-common-substring_1235207?source=youtube&campaign=striver_dp_videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_dp_videos&leftPanelTab=1

def lcs(str1: str, str2: str) -> int:
    # write your code here
    n = len(str1)
    m = len(str2)
    dp = [[0]*(m+1) for _ in range(n+1)]
    ans = float('-inf')
    for i in range(n):
        dp[i][0] = 0
    for j in range(m):
        dp[0][j] = 0
    for i in range(1,n+1):
        for j in range(1,m+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
                ans = max(ans, dp[i][j])
            else:
                dp[i][j] = 0
    return ans
