# 方法2：长除法 + 哈希表记录余数位置（面试主推）
# 余数决定后续小数；余数重复时，从第一次出现的位置开始加括号
# 时间 O(k)，空间 O(k)


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

        res = [sign + str(integer), "."]
        seen = {}

        while remainder != 0:
            if remainder in seen:
                start = seen[remainder]
                res.insert(start, "(")
                res.append(")")
                break

            seen[remainder] = len(res)

            remainder *= 10
            res.append(str(remainder // denominator))
            remainder %= denominator

        return "".join(res)


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
