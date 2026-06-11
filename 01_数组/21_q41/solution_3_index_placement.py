# 方法3：把数字放回对应下标位置（面试主推）

from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        for index in range(n):
            while 1 <= nums[index] <= n and nums[nums[index] - 1] != nums[index]:
                target_index = nums[index] - 1
                nums[index], nums[target_index] = nums[target_index], nums[index]

        for index in range(n):
            if nums[index] != index + 1:
                return index + 1

        return n + 1


def run_case(nums, expected):
    actual = Solution().firstMissingPositive(nums[:])
    assert actual == expected


if __name__ == "__main__":
    run_case([1, 2, 0], 3)
    run_case([3, 4, -1, 1], 2)
    run_case([7, 8, 9, 11, 12], 1)
    run_case([1, 2, 3, 4], 5)
    run_case([1, 1, 2, 2], 3)

    print("all tests passed")
