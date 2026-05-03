import random


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        """
        解法3：快速选择（Quick Select）— 面试推荐
        时间复杂度: O(n) 平均
        空间复杂度: O(1)
        """
        target = len(nums) - k
        left, right = 0, len(nums) - 1

        while True:
            pivot = nums[random.randint(left, right)]
            lt, i, gt = left, left, right

            while i <= gt:
                if nums[i] < pivot:
                    nums[lt], nums[i] = nums[i], nums[lt]
                    lt += 1
                    i += 1
                elif nums[i] > pivot:
                    nums[i], nums[gt] = nums[gt], nums[i]
                    gt -= 1
                else:
                    i += 1

            if lt <= target <= gt:
                return nums[target]
            elif target < lt:
                right = lt - 1
            else:
                left = gt + 1


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([3, 2, 1, 5, 6, 4], 2),
        ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4),
        ([1], 1),
        ([7, 9, 2, 8, 1], 3),
    ]

    for nums, k in test_cases:
        print(f"输入: {nums}, k={k}, 输出: {solution.findKthLargest(nums, k)}")
