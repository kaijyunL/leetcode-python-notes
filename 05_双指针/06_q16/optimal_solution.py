from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        最优解法：排序 + 双指针
        时间复杂度: O(n^2)
        空间复杂度: O(1)
        """
        nums.sort()
        n = len(nums)
        res = nums[0] + nums[1] + nums[2]

        for i in range(n - 2):
            left = i + 1
            right = n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if abs(total - target) < abs(res - target):
                    res = total

                if total == target:
                    return total
                if total < target:
                    left += 1
                else:
                    right -= 1

        return res


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([-1, 2, 1, -4], 1),
        ([0, 0, 0], 1),
        ([1, 1, 1, 0], -100),
        ([4, 0, 5, -5, 3, 3, 0, -4, -5], -2),
    ]

    for nums, target in test_cases:
        print(f"nums = {nums}, target = {target}, result = {solution.threeSumClosest(nums, target)}")
