# 方法3：回文预处理 + 一维动态规划
class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        is_pal = [[False] * n for _ in range(n)]

        for left in range(n - 1, -1, -1):
            for right in range(left, n):
                if s[left] == s[right] and (
                    right - left <= 2 or is_pal[left + 1][right - 1]
                ):
                    is_pal[left][right] = True

        dp = [0] * n
        for i in range(n):
            if is_pal[0][i]:
                dp[i] = 0
                continue

            dp[i] = i
            for j in range(1, i + 1):
                if is_pal[j][i]:
                    dp[i] = min(dp[i], dp[j - 1] + 1)

        return dp[-1]


if __name__ == "__main__":
    solver = Solution()
    test_cases = [
        "aab",
        "a",
        "ab",
        "aabaa",
        "cdd",
    ]

    for s in test_cases:
        print(f"s={s}, minCut={solver.minCut(s)}")
