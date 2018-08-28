# HELP:

# class Solution:
#     def findTargetSumWays(self, nums, S):
#         dp = [0] * 2001
#         dp[nums[0] + 1000] = 1
#         dp[-nums[0] + 1000] += 1
#         for i in range(1, len(nums)):
#             next = [0] * 2001
#             for sum in range(-1000, 1001):
#                 if dp[sum + 1000] > 0:
#                     next[sum + nums[i] + 1000] += dp[sum + 1000]
#                     next[sum - nums[i] + 1000] += dp[sum + 1000]
#             dp = next
#         return 0 if S > 1000 else dp[S + 1000]


class Solution:
    def findTargetSumWays(self, nums, S):
        if sum(nums) < S or (S + sum(nums)) % 2 != 0:
            return 0
        nS = (S + sum(nums)) // 2
        dp = [0 for i in range(nS + 1)]
        dp[0] = 1
        for i in nums:
            for j in range(nS, i - 1, -1):
                dp[j] += dp[j - i]
        return dp[nS]
