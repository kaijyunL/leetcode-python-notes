# 方法四：一维压缩动态规划
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n

        for _ in range(1, m):
            for col in range(1, n):
                dp[col] += dp[col - 1]

        return dp[-1]


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
