from typing import List


# 方法三：二维动态规划
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[0] * len(row) for row in triangle]
        dp[0][0] = triangle[0][0]

        for row in range(1, n):
            dp[row][0] = dp[row - 1][0] + triangle[row][0]
            dp[row][row] = dp[row - 1][row - 1] + triangle[row][row]

            for col in range(1, row):
                dp[row][col] = min(dp[row - 1][col - 1], dp[row - 1][col]) + triangle[row][col]

        return min(dp[-1])


if __name__ == "__main__":
    solver = Solution()
    test_cases = [
        [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]],
        [[-10]],
        [[1], [2, 3], [3, 6, 7], [8, 9, 6, 1]],
    ]

    for triangle in test_cases:
        print(f"triangle={triangle}, min_sum={solver.minimumTotal(triangle)}")
