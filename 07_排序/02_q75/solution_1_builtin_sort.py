class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        解法1：内置排序（最不符合题意）
        时间复杂度: O(n log n)
        空间复杂度: O(1)
        """
        nums.sort()


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        [2, 0, 2, 1, 1, 0],
        [2, 0, 1],
        [0],
        [1],
        [2],
        [0, 0, 0],
        [1, 2, 0, 1, 2, 0],
    ]

    for nums in test_cases:
        original = nums[:]
        solution.sortColors(nums)
        print(f"输入: {original}, 输出: {nums}")
