from typing import List


# 方法四：一维压缩动态规划
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [0] * (n + 1)
        max_side = 0

        for row in range(1, m + 1):
            prev = 0
            for col in range(1, n + 1):
                temp = dp[col]

                if matrix[row - 1][col - 1] == "1":
                    dp[col] = min(dp[col], dp[col - 1], prev) + 1
                    max_side = max(max_side, dp[col])
                else:
                    dp[col] = 0

                prev = temp

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
