class Solution:
    def findMin(self, nums: list[int]) -> int:
        """
        最优解法：在第 153 题基础上处理重复元素
        平均时间复杂度: O(log n)
        最坏时间复杂度: O(n)
        空间复杂度: O(1)
        """
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                right -= 1

        return nums[left]


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        [1, 3, 5],
        [2, 2, 2, 0, 1],
        [2, 2, 2, 0, 1, 2],
        [10, 1, 10, 10, 10],
        [1, 1, 1, 1],
        [1],
    ]

    for nums in test_cases:
        print(f"nums = {nums}, result = {solution.findMin(nums)}")
