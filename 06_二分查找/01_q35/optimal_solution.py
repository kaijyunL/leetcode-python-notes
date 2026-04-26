class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        """
        最优解法：二分查找第一个大于等于 target 的位置
        时间复杂度: O(log n)
        空间复杂度: O(1)
        """
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1

        return left


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([1, 3, 5, 6], 5),
        ([1, 3, 5, 6], 2),
        ([1, 3, 5, 6], 7),
        ([1, 3, 5, 6], 0),
    ]

    for nums, target in test_cases:
        print(f"nums = {nums}, target = {target}, result = {solution.searchInsert(nums, target)}")
