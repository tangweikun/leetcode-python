class Solution:
    def numberOfArithmeticSlices(self, A):
        dp = [0] * len(A)
        sum = 0
        for i in range(2, len(A)):
            if A[i - 2] + A[i] == A[i - 1] * 2:
                dp[i] = dp[i - 1] + 1
                sum += dp[i]
        return sum
