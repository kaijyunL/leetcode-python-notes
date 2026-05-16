from typing import List


# 方法一：暴力递归
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        def dfs(row, col):
            if row >= m or col >= n:
                return 0
            if obstacleGrid[row][col] == 1:
                return 0
            if row == m - 1 and col == n - 1:
                return 1

            return dfs(row + 1, col) + dfs(row, col + 1)

        return dfs(0, 0)


if __name__ == "__main__":
    solver = Solution()
    test_cases = [
        [[0, 0, 0], [0, 1, 0], [0, 0, 0]],
        [[0, 1], [0, 0]],
        [[1]],
    ]

    for grid in test_cases:
        print(f"grid={grid}, paths={solver.uniquePathsWithObstacles(grid)}")
