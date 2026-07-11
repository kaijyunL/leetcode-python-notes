# 方法1：三重循环暴力枚举

from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        ans = nums[0] + nums[1] + nums[2]

        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    total = nums[i] + nums[j] + nums[k]
                    if abs(total - target) < abs(ans - target):
                        ans = total

        return ans


if __name__ == "__main__":
    solution = Solution()

    assert solution.threeSumClosest([-1, 2, 1, -4], 1) == 2
    assert solution.threeSumClosest([0, 0, 0], 1) == 0
    assert solution.threeSumClosest([1, 1, 1, 0], -100) == 2
    assert solution.threeSumClosest([4, 0, 5, -5, 3, 3, 0, -4, -5], -2) == -2

    print("all tests passed")
