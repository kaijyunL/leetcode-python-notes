from typing import List


# 方法三：二维动态规划
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1:
            return 0

        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        for row in range(1, m):
            if obstacleGrid[row][0] == 0:
                dp[row][0] = dp[row - 1][0]

        for col in range(1, n):
            if obstacleGrid[0][col] == 0:
                dp[0][col] = dp[0][col - 1]

        for row in range(1, m):
            for col in range(1, n):
                if obstacleGrid[row][col] == 0:
                    dp[row][col] = dp[row - 1][col] + dp[row][col - 1]

        return dp[m - 1][n - 1]


if __name__ == "__main__":
    solver = Solution()
    test_cases = [
        [[0, 0, 0], [0, 1, 0], [0, 0, 0]],
        [[0, 1], [0, 0]],
        [[1]],
        [[0, 0], [1, 0]],
    ]

    for grid in test_cases:
        print(f"grid={grid}, paths={solver.uniquePathsWithObstacles(grid)}")
