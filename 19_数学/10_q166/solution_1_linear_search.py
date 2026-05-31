# 方法1：长除法 + 列表线性查找重复余数
# 余数重复说明小数开始循环；用列表记录余数出现顺序
# 时间 O(k^2)，空间 O(k)


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        negative = (numerator < 0) != (denominator < 0)
        numerator = abs(numerator)
        denominator = abs(denominator)

        sign = "-" if negative else ""
        integer = numerator // denominator
        remainder = numerator % denominator

        if remainder == 0:
            return sign + str(integer)

        digits = []
        remainders = []

        while remainder != 0:
            if remainder in remainders:
                start = remainders.index(remainder)
                digits.insert(start, "(")
                digits.append(")")
                break

            remainders.append(remainder)
            remainder *= 10
            digits.append(str(remainder // denominator))
            remainder %= denominator

        return sign + str(integer) + "." + "".join(digits)


if __name__ == "__main__":
    solver = Solution()

    test_cases = [
        (1, 2, "0.5"),
        (2, 1, "2"),
        (4, 333, "0.(012)"),
        (1, 6, "0.1(6)"),
        (1, 3, "0.(3)"),
        (22, 7, "3.(142857)"),
        (-50, 8, "-6.25"),
        (7, -12, "-0.58(3)"),
        (0, -5, "0"),
    ]

    for numerator, denominator, expected in test_cases:
        assert solver.fractionToDecimal(numerator, denominator) == expected

    print("all tests passed")
