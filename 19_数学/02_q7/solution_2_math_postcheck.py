# 方法2：数学反转，最后检查溢出


class Solution:
    def reverse(self, x: int) -> int:
        int_min = -(1 << 31)
        int_max = (1 << 31) - 1

        sign = -1 if x < 0 else 1
        num = abs(x)
        res = 0

        while num:
            res = res * 10 + num % 10
            num //= 10

        res *= sign

        if res < int_min or res > int_max:
            return 0
        return res


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
