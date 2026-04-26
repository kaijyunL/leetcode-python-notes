import random


class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        """
        随机三路快速排序：按 pivot 分成小于、等于、大于三段
        平均时间复杂度: O(n log n)
        最坏时间复杂度: O(n^2)
        空间复杂度: O(log n)
        """
        def quick_sort(left: int, right: int) -> None:
            if left >= right:
                return

            pivot = nums[random.randint(left, right)]
            lt = left
            i = left
            gt = right

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

            quick_sort(left, lt - 1)
            quick_sort(gt + 1, right)

        quick_sort(0, len(nums) - 1)
        return nums


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        [5, 2, 3, 1],
        [5, 1, 1, 2, 0, 0],
        [],
        [1],
        [-1, 5, 3, 4, 0],
        [2, 2, 2],
    ]

    for nums in test_cases:
        print(f"nums = {nums}, result = {solution.sortArray(nums[:])}")
