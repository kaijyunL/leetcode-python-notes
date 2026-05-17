# 方法四：一维压缩动态规划
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(1, m + 1):
            for j in range(n, 0, -1):
                if s[i - 1] == t[j - 1]:
                    dp[j] = dp[j - 1] + dp[j]

        return dp[n]


if __name__ == "__main__":
    solver = Solution()
    test_cases = [
        ("rabbbit", "rabbit"),
        ("babgbag", "bag"),
        ("abc", "abc"),
        ("abc", "abcd"),
    ]

    for s, t in test_cases:
        print(f"s={s}, t={t}, count={solver.numDistinct(s, t)}")
