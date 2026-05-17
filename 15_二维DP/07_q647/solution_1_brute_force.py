# 方法一：暴力枚举
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0

        def is_palindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        for left in range(n):
            for right in range(left, n):
                if is_palindrome(left, right):
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
