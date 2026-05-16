from typing import List


# 方法三：二维动态规划
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = grid[0][0]

        for row in range(1, m):
            dp[row][0] = dp[row - 1][0] + grid[row][0]

        for col in range(1, n):
            dp[0][col] = dp[0][col - 1] + grid[0][col]

        for row in range(1, m):
            for col in range(1, n):
                dp[row][col] = min(dp[row - 1][col], dp[row][col - 1]) + grid[row][col]

        return dp[m - 1][n - 1]


if __name__ == "__main__":
    solver = Solution()
    test_cases = [
        [[1, 3, 1], [1, 5, 1], [4, 2, 1]],
        [[1, 2, 3], [4, 5, 6]],
        [[5]],
    ]

    for grid in test_cases:
        print(f"grid={grid}, min_sum={solver.minPathSum(grid)}")
