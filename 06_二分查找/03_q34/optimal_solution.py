class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        """
        最优解法：两次二分查找
        时间复杂度: O(log n)
        空间复杂度: O(1)
        """
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        start = right + 1

        if start == len(nums) or nums[start] != target:
            return [-1, -1]

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1

        end = right
        return [start, end]


class SolutionStandardTemplate:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        """
        标准模板写法：遇到 target 后继续向左右收缩找边界
        时间复杂度: O(log n)
        空间复杂度: O(1)
        """
        left = 0
        right = len(nums) - 1
        start = -1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                start = mid
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        if start == -1:
            return [-1, -1]

        left = 0
        right = len(nums) - 1
        end = -1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                end = mid
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return [start, end]


if __name__ == "__main__":
    solution = Solution()
    solution_standard_template = SolutionStandardTemplate()

    test_cases = [
        ([5, 7, 7, 8, 8, 10], 8),
        ([5, 7, 7, 8, 8, 10], 6),
        ([], 0),
        ([1], 1),
        ([2, 2], 2),
    ]

    for nums, target in test_cases:
        print(f"nums = {nums}, target = {target}, result = {solution.searchRange(nums, target)}")
        print(f"标准模板 result = {solution_standard_template.searchRange(nums, target)}")
