class Solution:
    def search(self, nums: list[int], target: int) -> int:
        """
        最优解法：判断哪一半有序后继续二分
        时间复杂度: O(log n)
        空间复杂度: O(1)
        """
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([4, 5, 6, 7, 0, 1, 2], 0),
        ([4, 5, 6, 7, 0, 1, 2], 3),
        ([1], 0),
        ([1], 1),
        ([3, 1], 1),
    ]

    for nums, target in test_cases:
        print(f"nums = {nums}, target = {target}, result = {solution.search(nums, target)}")
