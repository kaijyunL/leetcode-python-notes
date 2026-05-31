# 方法1：暴力减法
# 把除法理解成 dividend 里能减掉多少个 divisor
# 时间 O(|quotient|)，空间 O(1)，大商会超时


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
            dividend_abs -= divisor_abs
            quotient += 1

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
        (-2147483648, -1, 2147483647),
    ]

    for dividend, divisor, expected in test_cases:
        assert solver.divide(dividend, divisor) == expected

    print("all tests passed")
