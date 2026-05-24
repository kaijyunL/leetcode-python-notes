# 方法2：异或加进位迭代


class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF

        a &= mask
        b &= mask

        while b:
            carry = ((a & b) << 1) & mask
            a = (a ^ b) & mask
            b = carry

        if a <= max_int:
            return a
        return ~(a ^ mask)


if __name__ == "__main__":
    solver = Solution()
    test_cases = [
        (1, 2, 3),
        (2, 3, 5),
        (0, 0, 0),
        (-1, 1, 0),
        (-2, 3, 1),
        (-5, -7, -12),
        (123, 456, 579),
    ]

    for a, b, expected in test_cases:
        assert solver.getSum(a, b) == expected

    print("all tests passed")
