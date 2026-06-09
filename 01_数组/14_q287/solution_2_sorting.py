# 方法2：排序后扫描相邻元素

from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)

        for i in range(1, len(sorted_nums)):
            if sorted_nums[i] == sorted_nums[i - 1]:
                return sorted_nums[i]

        return -1


if __name__ == "__main__":
    solution = Solution()

    assert solution.findDuplicate([1, 2, 3, 4, 2]) == 2
    assert solution.findDuplicate([3, 1, 3, 4, 2]) == 3
    assert solution.findDuplicate([1, 1]) == 1
    assert solution.findDuplicate([1, 1, 2]) == 1

    print("all tests passed")
