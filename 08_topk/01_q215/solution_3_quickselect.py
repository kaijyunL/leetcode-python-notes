import random


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        """
        方法3：三路快速选择（面试主推）
        时间复杂度：平均 O(n)，最坏 O(n^2)
        空间复杂度：O(1)
        """
        target = k - 1
        left, right = 0, len(nums) - 1

        while True:
            pivot = nums[random.randint(left, right)]
            greater_end = left
            i = left
            less_start = right

            # 分区后：[left, greater_end - 1] > pivot，
            # [greater_end, less_start] == pivot，
            # [less_start + 1, right] < pivot。
            while i <= less_start:
                if nums[i] > pivot:
                    nums[greater_end], nums[i] = nums[i], nums[greater_end]
                    greater_end += 1
                    i += 1
                elif nums[i] < pivot:
                    nums[i], nums[less_start] = nums[less_start], nums[i]
                    less_start -= 1
                else:
                    i += 1

            if target < greater_end:
                right = greater_end - 1
            elif target > less_start:
                left = less_start + 1
            else:
                return nums[target]


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([3, 2, 1, 5, 6, 4], 2, 5),
        ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4),
        ([1], 1, 1),
        ([7, 9, 2, 8, 1], 3, 7),
        ([5, 5, 5], 2, 5),
    ]

    for nums, k, expected in test_cases:
        assert solution.findKthLargest(nums, k) == expected

    print("all tests passed")
