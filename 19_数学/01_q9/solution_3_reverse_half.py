# 方法3：只反转后一半数字


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0

        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        return x == reversed_half or x == reversed_half // 10


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
