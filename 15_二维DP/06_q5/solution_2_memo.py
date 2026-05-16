# 方法二：记忆化递归
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        memo = {}
        best_left = 0
        best_len = 1

        def dfs(left, right):
            if left >= right:
                return True
            if (left, right) in memo:
                return memo[(left, right)]
            if s[left] != s[right]:
                memo[(left, right)] = False
                return False

            memo[(left, right)] = dfs(left + 1, right - 1)
            return memo[(left, right)]

        for left in range(n):
            for right in range(left, n):
                if right - left + 1 > best_len and dfs(left, right):
                    best_left = left
                    best_len = right - left + 1

        return s[best_left:best_left + best_len]


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
