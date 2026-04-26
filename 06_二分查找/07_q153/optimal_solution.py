class Solution:
    def findMin(self, nums: list[int]) -> int:
        """
        最优解法：根据 nums[mid] 和 nums[right] 的关系二分
        时间复杂度: O(log n)
        空间复杂度: O(1)
        """
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]


class SolutionBoundaryTemplate:
    def findMin(self, nums: list[int]) -> int:
        """
        边界模板写法：查找第一个小于等于 nums[-1] 的位置
        时间复杂度: O(log n)
        空间复杂度: O(1)
        """
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] > nums[-1]:
                left = mid + 1
            else:
                right = mid - 1

        return nums[right + 1]


if __name__ == "__main__":
    solution = Solution()
    solution_boundary_template = SolutionBoundaryTemplate()

    test_cases = [
        [3, 4, 5, 1, 2],
        [4, 5, 6, 7, 0, 1, 2],
        [11, 13, 15, 17],
        [1],
        [2, 1],
    ]

    for nums in test_cases:
        print(f"nums = {nums}, result = {solution.findMin(nums)}")
        print(f"边界模板 result = {solution_boundary_template.findMin(nums)}")
