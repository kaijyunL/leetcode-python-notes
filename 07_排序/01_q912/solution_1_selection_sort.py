class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        """
        选择排序：每轮把未排序部分的最小值放到当前位置
        时间复杂度: O(n^2)
        空间复杂度: O(1)
        """
        n = len(nums)

        for i in range(n):
            min_index = i

            for j in range(i + 1, n):
                if nums[j] < nums[min_index]:
                    min_index = j

            nums[i], nums[min_index] = nums[min_index], nums[i]

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
