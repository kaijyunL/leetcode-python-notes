from typing import List


# 方法二：记忆化递归
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        memo = {}

        def dfs(row, col):
            if row == n - 1:
                return triangle[row][col]
            if (row, col) in memo:
                return memo[(row, col)]

            memo[(row, col)] = triangle[row][col] + min(dfs(row + 1, col), dfs(row + 1, col + 1))
            return memo[(row, col)]

        return dfs(0, 0)


if __name__ == "__main__":
    solver = Solution()
    test_cases = [
        [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]],
        [[-10]],
        [[1], [2, 3], [3, 6, 7], [8, 9, 6, 1]],
    ]

    for triangle in test_cases:
        print(f"triangle={triangle}, min_sum={solver.minimumTotal(triangle)}")
