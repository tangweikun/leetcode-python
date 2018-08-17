# class Solution:
#     def rob(self, nums):
#         if len(nums) < 1:
#             return 0
#         else:
#             dp = [0] * (len(nums) + 1)
#             dp[0] = 0
#             dp[1] = nums[0]
#             for i in range(2, len(nums) + 1):
#                 dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])
#         return max(dp[len(nums)], dp[len(nums)-1])


class Solution:
    def rob(self, nums):
        dp = [0, 0] + nums
        for i in range(2, len(dp)):
            dp[i] = max(dp[i - 1], dp[i - 2] + dp[i])
        return dp[-1]
