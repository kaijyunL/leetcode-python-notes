class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        """
        最优解法：在第 33 题基础上处理重复元素
        平均时间复杂度: O(log n)
        最坏时间复杂度: O(n)
        空间复杂度: O(1)
        """
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return True

            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1
            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return False


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([2, 5, 6, 0, 0, 1, 2], 0),
        ([2, 5, 6, 0, 0, 1, 2], 3),
        ([1, 0, 1, 1, 1], 0),
        ([1, 1, 1, 1, 1], 2),
        ([1], 1),
        ([1, 3, 1, 1, 1], 3),
    ]

    for nums, target in test_cases:
        print(f"nums = {nums}, target = {target}, result = {solution.search(nums, target)}")
