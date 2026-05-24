# 方法1：暴力计数


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        for target in nums:
            count = 0
            for num in nums:
                if num == target:
                    count += 1

            if count == 1:
                return target

        return 0


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
