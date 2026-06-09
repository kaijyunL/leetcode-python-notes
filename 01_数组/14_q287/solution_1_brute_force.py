# 方法1：暴力双循环

from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    return nums[i]

        return -1


if __name__ == "__main__":
    solution = Solution()

    assert solution.findDuplicate([1, 2, 3, 4, 2]) == 2
    assert solution.findDuplicate([3, 1, 3, 4, 2]) == 3
    assert solution.findDuplicate([1, 1]) == 1
    assert solution.findDuplicate([1, 1, 2]) == 1

    print("all tests passed")
