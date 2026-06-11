# 方法2：找到转折点后交换并反转后缀（面试主推）

from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        pivot = n - 2

        while pivot >= 0 and nums[pivot] >= nums[pivot + 1]:
            pivot -= 1

        if pivot >= 0:
            successor = n - 1
            while nums[successor] <= nums[pivot]:
                successor -= 1
            nums[pivot], nums[successor] = nums[successor], nums[pivot]

        left = pivot + 1
        right = n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


def run_case(nums, expected):
    actual = nums[:]
    Solution().nextPermutation(actual)
    assert actual == expected


if __name__ == "__main__":
    run_case([1, 2, 3], [1, 3, 2])
    run_case([3, 2, 1], [1, 2, 3])
    run_case([1, 1, 5], [1, 5, 1])
    run_case([1, 5, 8, 4, 7, 6, 5, 3, 1], [1, 5, 8, 5, 1, 3, 4, 6, 7])
    run_case([1], [1])

    print("all tests passed")
