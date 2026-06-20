# 方法3：把数字放回对应下标位置（面试主推）

from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                target_i = nums[i] - 1
                nums[i], nums[target_i] = nums[target_i], nums[i]

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

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
