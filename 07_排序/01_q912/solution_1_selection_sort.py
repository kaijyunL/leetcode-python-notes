# 方法1：选择排序


class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        n = len(nums)

        for i in range(n - 1):
            min_index = i

            for j in range(i + 1, n):
                if nums[j] < nums[min_index]:
                    min_index = j

            if min_index != i:
                nums[i], nums[min_index] = nums[min_index], nums[i]

        return nums


if __name__ == "__main__":
    solution = Solution()

    assert solution.sortArray([5, 2, 3, 1]) == [1, 2, 3, 5]
    assert solution.sortArray([5, 1, 1, 2, 0, 0]) == [0, 0, 1, 1, 2, 5]
    assert solution.sortArray([]) == []
    assert solution.sortArray([-1, 5, 3, 4, 0]) == [-1, 0, 3, 4, 5]
    assert solution.sortArray([2, 2, 2]) == [2, 2, 2]

    print("all tests passed")
