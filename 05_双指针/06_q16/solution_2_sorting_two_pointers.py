# 方法2：排序 + 双指针（面试主推）

from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        best_sum = nums[0] + nums[1] + nums[2]

        for i in range(n - 2):
            left = i + 1
            right = n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if abs(total - target) < abs(best_sum - target):
                    best_sum = total

                if total == target:
                    return total
                if total < target:
                    left += 1
                else:
                    right -= 1

        return best_sum


if __name__ == "__main__":
    solution = Solution()

    assert solution.threeSumClosest([-1, 2, 1, -4], 1) == 2
    assert solution.threeSumClosest([0, 0, 0], 1) == 0
    assert solution.threeSumClosest([1, 1, 1, 0], -100) == 2
    assert solution.threeSumClosest([4, 0, 5, -5, 3, 3, 0, -4, -5], -2) == -2

    print("all tests passed")
