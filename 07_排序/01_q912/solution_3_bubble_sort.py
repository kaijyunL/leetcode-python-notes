class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        """
        冒泡排序：相邻元素两两比较，把较大的元素逐步交换到后面
        时间复杂度: O(n^2)
        空间复杂度: O(1)
        """
        n = len(nums)

        for end in range(n - 1, 0, -1):
            swapped = False

            for i in range(end):
                if nums[i] > nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                    swapped = True

            if not swapped:
                break

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
