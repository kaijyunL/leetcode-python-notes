from typing import List


# 方法三：二维动态规划
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        max_side = 0

        for row in range(m):
            for col in range(n):
                if matrix[row][col] == "1":
                    if row == 0 or col == 0:
                        dp[row][col] = 1
                    else:
                        dp[row][col] = min(
                            dp[row - 1][col],
                            dp[row][col - 1],
                            dp[row - 1][col - 1],
                        ) + 1

                    max_side = max(max_side, dp[row][col])

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
