# 方法2：前缀和 + 二分查找

from bisect import bisect_left
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)

        for i, num in enumerate(nums, start=1):
            prefix[i] = prefix[i - 1] + num

        ans = n + 1

        for left in range(n):
            need = prefix[left] + target
            right = bisect_left(prefix, need)
            if right <= n:
                ans = min(ans, right - left)

        return 0 if ans == n + 1 else ans


if __name__ == "__main__":
    solution = Solution()

    assert solution.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]) == 2
    assert solution.minSubArrayLen(4, [1, 4, 4]) == 1
    assert solution.minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert solution.minSubArrayLen(15, [1, 2, 3, 4, 5]) == 5
    assert solution.minSubArrayLen(100, []) == 0

    print("all tests passed")
