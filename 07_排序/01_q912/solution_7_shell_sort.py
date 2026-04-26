class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        """
        希尔排序：按 gap 分组做插入排序
        平均时间复杂度: 取决于 gap 序列
        空间复杂度: O(1)
        """
        n = len(nums)
        gap = n // 2

        while gap > 0:
            for i in range(gap, n):
                current = nums[i]
                j = i

                while j >= gap and nums[j - gap] > current:
                    nums[j] = nums[j - gap]
                    j -= gap

                nums[j] = current

            gap //= 2

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
