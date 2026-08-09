import random


# 方法5：随机三路快速排序


class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        def quick_sort(left, right):
            # 递归较短一边，循环处理较长一边，递归栈保持 O(log n)。
            while left < right:
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

                if lt - left < right - gt:
                    quick_sort(left, lt - 1)
                    left = gt + 1
                else:
                    quick_sort(gt + 1, right)
                    right = lt - 1

        quick_sort(0, len(nums) - 1)
        return nums


if __name__ == "__main__":
    solution = Solution()

    assert solution.sortArray([5, 2, 3, 1]) == [1, 2, 3, 5]
    assert solution.sortArray([5, 1, 1, 2, 0, 0]) == [0, 0, 1, 1, 2, 5]
    assert solution.sortArray([]) == []
    assert solution.sortArray([-1, 5, 3, 4, 0]) == [-1, 0, 3, 4, 5]
    assert solution.sortArray([2, 2, 2]) == [2, 2, 2]

    print("all tests passed")
