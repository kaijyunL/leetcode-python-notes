from typing import List


# 方法二：记忆化递归
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        memo = {}
        max_side = 0

        def dfs(row, col):
            if row < 0 or col < 0:
                return 0
            if (row, col) in memo:
                return memo[(row, col)]
            if matrix[row][col] == "0":
                memo[(row, col)] = 0
                return 0

            memo[(row, col)] = min(
                dfs(row - 1, col),
                dfs(row, col - 1),
                dfs(row - 1, col - 1),
            ) + 1
            return memo[(row, col)]

        for row in range(m):
            for col in range(n):
                max_side = max(max_side, dfs(row, col))

        return max_side * max_side


if __name__ == "__main__":
    solver = Solution()
    test_cases = [
        [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]],
        [["0", "1"], ["1", "0"]],
        [["1"]],
    ]

    for matrix in test_cases:
        print(f"matrix={matrix}, area={solver.maximalSquare(matrix)}")
