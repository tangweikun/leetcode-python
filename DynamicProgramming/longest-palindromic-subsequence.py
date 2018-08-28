class Solution:
    def longestPalindromeSubseq(self, s):
        dp = [0] * len(s)
        for i in range(len(s)):
            dp[i] = 1
            prev = 0
            for j in range(i - 1, -1, -1):
                temp = dp[j]
                if s[i] == s[j]:
                    dp[j] = 2 + prev
                else:
                    dp[j] = max(dp[j + 1], dp[j])
                prev = temp
        return dp[0]
