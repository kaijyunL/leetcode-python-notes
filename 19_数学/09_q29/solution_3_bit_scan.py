# 方法3：从高位到低位扫描（面试主推）
# 商可以拆成若干个 2 的幂；能减掉 divisor << shift，就把 1 << shift 加进商
# 时间 O(32)，空间 O(1)


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

        for shift in range(31, -1, -1):
            if dividend_abs >= (divisor_abs << shift):
                dividend_abs -= divisor_abs << shift
                quotient += 1 << shift

        if negative:
            quotient = -quotient

        if quotient < int_min:
            return int_min
        if quotient > int_max:
            return int_max

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
