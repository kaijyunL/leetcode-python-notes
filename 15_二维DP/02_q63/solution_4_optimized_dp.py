from typing import List


# 方法四：一维压缩动态规划
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * n
        dp[0] = 1 if obstacleGrid[0][0] == 0 else 0

        for row in range(m):
            for col in range(n):
                if obstacleGrid[row][col] == 1:
                    dp[col] = 0
                elif col > 0:
                    dp[col] += dp[col - 1]

        return dp[-1]


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
