# 方法二：固定起点 + 向右扩展时滚动累加

from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0

        for left in range(n):
            current_sum = 0
            for right in range(left, n):
                current_sum += nums[right]
                if current_sum == k:
                    ans += 1

        return ans


if __name__ == "__main__":
    solution = Solution()

    assert solution.subarraySum([1, 1, 1], 2) == 2
    assert solution.subarraySum([1, 2, 3], 3) == 2
    assert solution.subarraySum([1, -1, 0], 0) == 3
    assert solution.subarraySum([3], 3) == 1

    print("all tests passed")
