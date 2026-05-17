# 方法三：二维动态规划
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        m, n = len(s1), len(s2)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        for i in range(1, m + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                k = i + j - 1
                dp[i][j] = (
                    dp[i - 1][j] and s1[i - 1] == s3[k]
                ) or (
                    dp[i][j - 1] and s2[j - 1] == s3[k]
                )

        return dp[m][n]


if __name__ == "__main__":
    solver = Solution()
    test_cases = [
        ("aabcc", "dbbca", "aadbbcbcac"),
        ("aabcc", "dbbca", "aadbbbaccc"),
        ("", "", ""),
        ("abc", "def", "adbcef"),
    ]

    for s1, s2, s3 in test_cases:
        print(f"s1={s1}, s2={s2}, s3={s3}, can={solver.isInterleave(s1, s2, s3)}")
