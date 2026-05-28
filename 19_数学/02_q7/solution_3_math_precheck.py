# 方法3：数学反转，提前检查溢出


class Solution:
    def reverse(self, x: int) -> int:
        int_max = (1 << 31) - 1
        negative_limit = 1 << 31

        sign = -1 if x < 0 else 1
        limit = negative_limit if x < 0 else int_max

        num = abs(x)
        res = 0

        while num:
            digit = num % 10
            num //= 10

            if res > (limit - digit) // 10:
                return 0

            res = res * 10 + digit

        return sign * res


if __name__ == "__main__":
    solver = Solution()

    test_cases = [
        (123, 321),
        (-123, -321),
        (120, 21),
        (0, 0),
        (1534236469, 0),
        (-2147483412, -2143847412),
        (-1563847412, 0),
    ]

    for x, expected in test_cases:
        assert solver.reverse(x) == expected

    print("all tests passed")
