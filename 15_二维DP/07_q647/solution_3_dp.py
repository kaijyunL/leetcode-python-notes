# 方法三：动态规划
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        count = 0

        for right in range(n):
            for left in range(right + 1):
                if s[left] == s[right] and (right - left <= 1 or dp[left + 1][right - 1]):
                    dp[left][right] = True
                    count += 1

        return count


if __name__ == "__main__":
    solver = Solution()
    test_cases = [
        "abc",
        "aaa",
        "abba",
        "abac",
    ]

    for s in test_cases:
        print(f"s={s}, count={solver.countSubstrings(s)}")
