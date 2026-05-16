# 方法三：二维动态规划
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]

        for row in range(m):
            dp[row][0] = 1
        for col in range(n):
            dp[0][col] = 1

        for row in range(1, m):
            for col in range(1, n):
                dp[row][col] = dp[row - 1][col] + dp[row][col - 1]

        return dp[m - 1][n - 1]


if __name__ == "__main__":
    solver = Solution()
    test_cases = [
        (3, 7),
        (3, 2),
        (3, 3),
        (7, 3),
    ]

    for m, n in test_cases:
        print(f"m={m}, n={n}, paths={solver.uniquePaths(m, n)}")
