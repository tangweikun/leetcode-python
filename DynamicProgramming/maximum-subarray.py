# class Solution:
#     def maxSubArray(self, nums):
#         dp = [0] * (len(nums))
#         sum = nums[0]
#         dp[0] = nums[0]
#         for i in range(1, len(nums)):
#             dp[i] = max(dp[i - 1], 0) + nums[i]
#             sum = max(sum, dp[i])
#         return sum


class Solution:
    def maxSubArray(self, nums):
        for i in range(1, len(nums)):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
        return max(nums)
