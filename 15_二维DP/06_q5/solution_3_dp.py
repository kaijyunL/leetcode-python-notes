# 方法三：动态规划
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        start, end = 0, 0

        for right in range(n):
            for left in range(right + 1):
                if s[left] == s[right] and (right - left <= 2 or dp[left + 1][right - 1]):
                    dp[left][right] = True
                    if right - left > end - start:
                        start, end = left, right

        return s[start:end + 1]


if __name__ == "__main__":
    solver = Solution()
    test_cases = [
        "babad",
        "cbbd",
        "a",
        "ac",
    ]

    for s in test_cases:
        print(f"s={s}, longest={solver.longestPalindrome(s)}")
