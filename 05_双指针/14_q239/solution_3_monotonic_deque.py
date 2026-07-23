# 方法3：单调递减队列（面试主推）

from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        ans = []

        for right, num in enumerate(nums):
            left = right - k + 1

            while dq and dq[0] < left:
                dq.popleft()

            while dq and nums[dq[-1]] <= num:
                dq.pop()

            dq.append(right)

            if right >= k - 1:
                ans.append(nums[dq[0]])

        return ans


if __name__ == "__main__":
    solution = Solution()

    assert solution.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]
    assert solution.maxSlidingWindow([1], 1) == [1]
    assert solution.maxSlidingWindow([1, -1], 1) == [1, -1]
    assert solution.maxSlidingWindow([9, 11], 2) == [11]
    assert solution.maxSlidingWindow([4, -2], 2) == [4]

    print("all tests passed")
