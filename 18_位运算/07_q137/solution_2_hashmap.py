# 方法2：哈希表计数


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        counts = {}

        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        for num, count in counts.items():
            if count == 1:
                return num

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
