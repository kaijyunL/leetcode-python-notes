from typing import List


# 方法一：暴力递归
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(row, col):
            if row >= m or col >= n:
                return float("inf")
            if row == m - 1 and col == n - 1:
                return grid[row][col]

            return grid[row][col] + min(dfs(row + 1, col), dfs(row, col + 1))

        return dfs(0, 0)


if __name__ == "__main__":
    solver = Solution()
    test_cases = [
        [[1, 3, 1], [1, 5, 1], [4, 2, 1]],
        [[1, 2, 3], [4, 5, 6]],
    ]

    for grid in test_cases:
        print(f"grid={grid}, min_sum={solver.minPathSum(grid)}")
