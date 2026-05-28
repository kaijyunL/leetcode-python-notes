# 方法1：转字符串


class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        return s == s[::-1]


if __name__ == "__main__":
    solver = Solution()

    test_cases = [
        (121, True),
        (-121, False),
        (10, False),
        (0, True),
        (1221, True),
        (12321, True),
        (123, False),
    ]

    for x, expected in test_cases:
        assert solver.isPalindrome(x) == expected

    print("all tests passed")
