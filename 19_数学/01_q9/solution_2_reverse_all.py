# 方法2：反转整个整数


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        original = x
        reversed_num = 0

        while x:
            reversed_num = reversed_num * 10 + x % 10
            x //= 10

        return original == reversed_num


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
