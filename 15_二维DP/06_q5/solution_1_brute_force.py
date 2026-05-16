# 方法一：暴力枚举
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        best = s[0]

        def is_palindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        for left in range(n):
            for right in range(left, n):
                if right - left + 1 > len(best) and is_palindrome(left, right):
                    best = s[left:right + 1]

        return best


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
