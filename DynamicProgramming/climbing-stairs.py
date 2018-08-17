# class Solution:
#     def climbStairs(self, n):
#         dp = [0] * (n + 2)
#         dp[1] = 1
#         dp[2] = 2
#         for i in range(3, n + 1):
#             dp[i] = dp[i - 1] + dp[i - 2]
#         return dp[n]


# class Solution:
#     def climbStairs(self, n):
#         a, b = 0, 1
#         for _ in range(n):
#             a, b = b, a + b
#         return b

class Solution:
    def climbStairs(self, n):
        dp = [0, 1, 2]
        for i in range(3, n + 1):
            dp.append(dp[i - 1] + dp[i - 2])
        return dp[n]
