# 方法3：滑动窗口（面试主推）

from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        window_sum = 0
        ans = len(nums) + 1

        for right, num in enumerate(nums):
            window_sum += num

            while window_sum >= target:
                ans = min(ans, right - left + 1)
                window_sum -= nums[left]
                left += 1

        return 0 if ans == len(nums) + 1 else ans


if __name__ == "__main__":
    solution = Solution()

    assert solution.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]) == 2
    assert solution.minSubArrayLen(4, [1, 4, 4]) == 1
    assert solution.minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert solution.minSubArrayLen(15, [1, 2, 3, 4, 5]) == 5
    assert solution.minSubArrayLen(100, []) == 0

    print("all tests passed")
