# 方法1：逐位模拟二进制加法


class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF

        a &= mask
        b &= mask

        result = 0
        carry = 0

        for i in range(32):
            bit_a = (a >> i) & 1
            bit_b = (b >> i) & 1

            sum_bit = bit_a ^ bit_b ^ carry
            carry = (bit_a & bit_b) | (bit_a & carry) | (bit_b & carry)

            result |= sum_bit << i

        if result <= max_int:
            return result
        return ~(result ^ mask)


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
