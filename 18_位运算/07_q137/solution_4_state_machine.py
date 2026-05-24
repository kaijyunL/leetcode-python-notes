# 方法4：有限状态机位运算


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        ones = 0
        twos = 0

        for num in nums:
            ones = (ones ^ num) & ~twos
            twos = (twos ^ num) & ~ones

        return ones


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
