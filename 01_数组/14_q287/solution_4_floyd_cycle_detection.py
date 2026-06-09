# 方法4：Floyd 判圈

from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        finder = nums[0]
        while finder != slow:
            finder = nums[finder]
            slow = nums[slow]

        return finder


if __name__ == "__main__":
    solution = Solution()

    assert solution.findDuplicate([1, 2, 3, 4, 2]) == 2
    assert solution.findDuplicate([3, 1, 3, 4, 2]) == 3
    assert solution.findDuplicate([1, 1]) == 1
    assert solution.findDuplicate([1, 1, 2]) == 1
    assert solution.findDuplicate([2, 2, 2, 2, 2]) == 2

    print("all tests passed")
