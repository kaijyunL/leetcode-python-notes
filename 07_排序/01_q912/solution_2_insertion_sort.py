class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        """
        插入排序：把当前元素插入到前面已经有序的部分
        时间复杂度: O(n^2)
        空间复杂度: O(1)
        """
        for i in range(1, len(nums)):
            current = nums[i]
            j = i - 1

            while j >= 0 and nums[j] > current:
                nums[j + 1] = nums[j]
                j -= 1

            nums[j + 1] = current

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
