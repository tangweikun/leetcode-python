class Solution:
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])
        dp = grid[:]
        for j in range(1, n):
            dp[0][j] += grid[0][j - 1]
        for i in range(1, m):
            dp[i][0] += dp[i - 1][0]
            for j in range(1, n):
                dp[i][j] += min(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]
