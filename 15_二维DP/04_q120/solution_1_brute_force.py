from typing import List


# 方法一：暴力递归
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)

        def dfs(row, col):
            if row == n - 1:
                return triangle[row][col]

            return triangle[row][col] + min(dfs(row + 1, col), dfs(row + 1, col + 1))

        return dfs(0, 0)


if __name__ == "__main__":
    solver = Solution()
    test_cases = [
        [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]],
        [[-10]],
    ]

    for triangle in test_cases:
        print(f"triangle={triangle}, min_sum={solver.minimumTotal(triangle)}")
