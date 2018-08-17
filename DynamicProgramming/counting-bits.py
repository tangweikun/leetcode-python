# class Solution:
#     def countBits(self, num):
#         res = [0]
#         while len(res) < num:
#             res.extend([x + 1 for x in res])
#         return res[:num+1]


class Solution:
    def countBits(self, num):
        dp = [0] * (num + 1)
        for i in range(1, num + 1):
            dp[i] = dp[i >> 1] + (i & 1)
        return dp
