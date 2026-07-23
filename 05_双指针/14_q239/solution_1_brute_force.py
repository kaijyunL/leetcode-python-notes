# 方法1：每个窗口重新求最大值

from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []

        for left in range(len(nums) - k + 1):
            ans.append(max(nums[left:left + k]))

        return ans


if __name__ == "__main__":
    solution = Solution()

    assert solution.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]
    assert solution.maxSlidingWindow([1], 1) == [1]
    assert solution.maxSlidingWindow([1, -1], 1) == [1, -1]
    assert solution.maxSlidingWindow([9, 11], 2) == [11]
    assert solution.maxSlidingWindow([4, -2], 2) == [4]

    print("all tests passed")
