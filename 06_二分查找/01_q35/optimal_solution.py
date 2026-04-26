class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        """
        最优解法：二分查找最后一个小于 target 的位置
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

        return right + 1


class SolutionStandardTemplate:
    def searchInsert(self, nums: list[int], target: int) -> int:
        """
        标准模板写法：先找 target，找不到时 left 就是插入位置
        时间复杂度: O(log n)
        空间复杂度: O(1)
        """
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left


if __name__ == "__main__":
    solution = Solution()
    solution_standard_template = SolutionStandardTemplate()

    test_cases = [
        ([1, 3, 5, 6], 5),
        ([1, 3, 5, 6], 2),
        ([1, 3, 5, 6], 7),
        ([1, 3, 5, 6], 0),
    ]

    for nums, target in test_cases:
        print(f"nums = {nums}, target = {target}, result = {solution.searchInsert(nums, target)}")
        print(f"标准模板 result = {solution_standard_template.searchInsert(nums, target)}")
