# 方法1：额外数组收集唯一值

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        unique_nums = [nums[0]]

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                unique_nums.append(nums[i])

        for i, num in enumerate(unique_nums):
            nums[i] = num

        return len(unique_nums)


if __name__ == "__main__":
    solution = Solution()

    def check(nums, expected_k, expected_prefix):
        k = solution.removeDuplicates(nums)
        assert k == expected_k
        assert nums[:k] == expected_prefix

    check([1, 1, 2], 2, [1, 2])
    check([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5, [0, 1, 2, 3, 4])
    check([], 0, [])
    check([1, 1, 1], 1, [1])
    check([1, 2, 3], 3, [1, 2, 3])

    print("all tests passed")
