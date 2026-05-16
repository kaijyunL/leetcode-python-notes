from typing import List


# 方法五：自底向上动态规划
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = triangle[-1][:]

        for row in range(len(triangle) - 2, -1, -1):
            for col in range(row + 1):
                dp[col] = triangle[row][col] + min(dp[col], dp[col + 1])

        return dp[0]


if __name__ == "__main__":
    solver = Solution()
    test_cases = [
        [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]],
        [[-10]],
        [[1], [2, 3], [3, 6, 7], [8, 9, 6, 1]],
    ]

    for triangle in test_cases:
        print(f"triangle={triangle}, min_sum={solver.minimumTotal(triangle)}")
