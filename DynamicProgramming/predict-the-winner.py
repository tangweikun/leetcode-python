# HELP:


class Solution:
    def PredictTheWinner(self, nums):
        dp = list(nums)
        print(dp)
        for j in range(1, len(nums)):
            for i in range(len(nums) - j):
                dp[i] = max(nums[i] - dp[i + 1], nums[i + j] - dp[i])
        return dp[0] >= 0
