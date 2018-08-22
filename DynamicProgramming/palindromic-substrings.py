# HELP:

# class Solution:
#     def countSubstrings(self, s):
#         i = 0
#         length = len(s)
#         res = 0
#         while i < length:
#             j = i
#             cnt = 0
#             while j < length and s[i] == s[j]:
#                 j += 1
#                 cnt += 1
#             res += (cnt * (cnt + 1)) // 2
#             l = i - 1
#             r = j
#             while l >= 0 and r < length and s[l] == s[r]:
#                 res += 1
#                 l -= 1
#                 r += 1
#             i = j
#         return res


# class Solution:
#     def countSubstrings(self, S):
#         N = len(S)
#         ans = 0
#         for center in range(2 * N - 1):
#             left = center // 2
#             right = left + center % 2
#             while left >= 0 and right < N and S[left] == S[right]:
#                 ans += 1
#                 left -= 1
#                 right += 1
#         return ans

class Solution:
    def countSubstrings(self, s):
        dp = [0] * len(s)
        result = 0
        for i in range(len(s) - 1, -1, -1):
            dp[i] = 1
            for j in range(len(s) - 1, i, -1):
                if s[i] == s[j] and dp[j - 1] == 1:
                    dp[j] = 1
                    result += 1
                else:
                    dp[j] = 0
            result += 1
        return result
