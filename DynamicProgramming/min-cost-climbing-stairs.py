# class Solution:
#     def minCostClimbingStairs(self, cost):
#         f1 = f2 = 0
#         for x in cost:
#             f1, f2 = x + min(f1, f2), f1
#         return min(f1, f2)


# class Solution:
#     def minCostClimbingStairs(self, cost):
#         dp = [0] * (len(cost) + 1)
#         dp[1], dp[2] = cost[0], cost[1]
#         for i in range(3, len(cost) + 1):
#             dp[i] = cost[i - 1] + min(dp[i - 1], dp[i - 2])
#         return min(dp[len(cost)], dp[len(cost)-1])

class Solution:
    def minCostClimbingStairs(self, cost):
        for i in range(2, len(cost)):
            cost[i] += min(cost[i - 1], cost[i - 2])
        return min(cost[-1], cost[-2])
