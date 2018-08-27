class Solution:
    def deleteAndEarn(self, nums):
        if not nums:
            return 0
        dp = [0] * (max(nums) + 1)
        for n in nums:
            dp[n] += n
        for i in range(2, max(nums) + 1):
            dp[i] = max(dp[i - 1], dp[i] + dp[i - 2])
        return dp[-1]
