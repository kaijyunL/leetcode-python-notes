# 方法2：倍增减法
# 每轮尽量减掉 divisor 的 2 的幂倍，避免一次只减一个 divisor
# 时间 O(log^2 N)，空间 O(1)


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        int_min = -(1 << 31)
        int_max = (1 << 31) - 1

        if dividend == int_min and divisor == -1:
            return int_max

        negative = (dividend < 0) != (divisor < 0)
        dividend_abs = abs(dividend)
        divisor_abs = abs(divisor)

        quotient = 0

        while dividend_abs >= divisor_abs:
            current = divisor_abs
            multiple = 1

            while dividend_abs >= (current << 1):
                current <<= 1
                multiple <<= 1

            dividend_abs -= current
            quotient += multiple

        if negative:
            quotient = -quotient

        return quotient


if __name__ == "__main__":
    solver = Solution()

    test_cases = [
        (10, 3, 3),
        (7, -3, -2),
        (0, 1, 0),
        (1, 1, 1),
        (-15, 2, -7),
        (43, 8, 5),
        (2147483647, 2, 1073741823),
        (-2147483648, 1, -2147483648),
        (-2147483648, -1, 2147483647),
    ]

    for dividend, divisor, expected in test_cases:
        assert solver.divide(dividend, divisor) == expected

    print("all tests passed")
