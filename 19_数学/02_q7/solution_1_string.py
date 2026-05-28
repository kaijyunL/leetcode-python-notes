# 方法1：字符串反转


class Solution:
    def reverse(self, x: int) -> int:
        int_min = -(1 << 31)
        int_max = (1 << 31) - 1

        sign = -1 if x < 0 else 1
        reversed_num = int(str(abs(x))[::-1]) * sign

        if reversed_num < int_min or reversed_num > int_max:
            return 0
        return reversed_num


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
