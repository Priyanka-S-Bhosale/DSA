def minInsertion(s):
    # Write the function here.
    def longestCommonSubsequence(text1, text2):
        n = len(text1)
        m = len(text2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[n][m]


    reversed_s = s[::-1]
    lcs = longestCommonSubsequence(s, reversed_s)
    return len(s) - lcs

s = "abcaa"
print(minInsertion(s))
