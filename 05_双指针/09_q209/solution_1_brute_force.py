# 方法1：固定起点，向右累加到达标为止

from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        ans = n + 1

        for left in range(n):
            total = 0

            for right in range(left, n):
                total += nums[right]
                if total >= target:
                    ans = min(ans, right - left + 1)
                    break

        return 0 if ans == n + 1 else ans


if __name__ == "__main__":
    solution = Solution()

    assert solution.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]) == 2
    assert solution.minSubArrayLen(4, [1, 4, 4]) == 1
    assert solution.minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert solution.minSubArrayLen(15, [1, 2, 3, 4, 5]) == 5
    assert solution.minSubArrayLen(100, []) == 0

    print("all tests passed")
