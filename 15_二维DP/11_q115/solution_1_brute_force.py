# 方法一：暴力递归
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)

        def dfs(i, j):
            if j == n:
                return 1
            if i == m:
                return 0
            if s[i] == t[j]:
                return dfs(i + 1, j + 1) + dfs(i + 1, j)
            return dfs(i + 1, j)

        return dfs(0, 0)


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
