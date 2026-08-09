# 方法7：希尔排序


class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        n = len(nums)
        gap = n // 2

        while gap > 0:
            for i in range(gap, n):
                value = nums[i]
                j = i

                while j >= gap and nums[j - gap] > value:
                    nums[j] = nums[j - gap]
                    j -= gap

                nums[j] = value

            gap //= 2

        return nums


if __name__ == "__main__":
    solution = Solution()

    assert solution.sortArray([5, 2, 3, 1]) == [1, 2, 3, 5]
    assert solution.sortArray([5, 1, 1, 2, 0, 0]) == [0, 0, 1, 1, 2, 5]
    assert solution.sortArray([]) == []
    assert solution.sortArray([-1, 5, 3, 4, 0]) == [-1, 0, 3, 4, 5]
    assert solution.sortArray([2, 2, 2]) == [2, 2, 2]

    print("all tests passed")
