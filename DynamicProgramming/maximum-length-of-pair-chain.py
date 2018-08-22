# Greedy
# class Solution:
#     def findLongestChain(self, pairs):
#         pairs.sort(key=lambda x: x[1])
#         cur = -float('inf')
#         res = 0
#         for pair in pairs:
#             if cur < pair[0]:
#                 cur = pair[1]
#                 res += 1
#         return res


class Solution:
    def findLongestChain(self, pairs):
        pairs.sort(key=lambda x: x[0])
        dp = [1] * len(pairs)
        for j in range(1, len(pairs)):
            for i in range(0, j):
                if pairs[i][1] < pairs[j][0]:
                    dp[j] = max(dp[j], dp[i] + 1)
        return dp[len(dp) - 1]
