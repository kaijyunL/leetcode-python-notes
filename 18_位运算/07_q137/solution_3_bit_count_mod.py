# 方法3：逐位统计 mod 3


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result = 0

        for i in range(32):
            bit_count = 0
            for num in nums:
                bit_count += (num >> i) & 1

            if bit_count % 3:
                result |= 1 << i

        if result >= 1 << 31:
            result -= 1 << 32

        return result


if __name__ == "__main__":
    solver = Solution()
    test_cases = [
        ([2, 2, 3, 2], 3),
        ([0, 1, 0, 1, 0, 1, 99], 99),
        ([-2, -2, 1, 1, 4, 1, 4, 4, -4, -2], -4),
    ]

    for nums, expected in test_cases:
        assert solver.singleNumber(nums) == expected

    print("all tests passed")
