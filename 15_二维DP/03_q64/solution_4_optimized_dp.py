from typing import List


# 方法四：一维压缩动态规划
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [0] * n
        dp[0] = grid[0][0]

        for col in range(1, n):
            dp[col] = dp[col - 1] + grid[0][col]

        for row in range(1, m):
            dp[0] += grid[row][0]
            for col in range(1, n):
                dp[col] = min(dp[col], dp[col - 1]) + grid[row][col]

        return dp[-1]


if __name__ == "__main__":
    solver = Solution()
    test_cases = [
        [[1, 3, 1], [1, 5, 1], [4, 2, 1]],
        [[1, 2, 3], [4, 5, 6]],
        [[5]],
    ]

    for grid in test_cases:
        print(f"grid={grid}, min_sum={solver.minPathSum(grid)}")
