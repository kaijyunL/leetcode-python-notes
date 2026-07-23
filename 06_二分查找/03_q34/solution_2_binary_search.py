# 方法2：二分查找（面试主推）


class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        left_bound = self.find_first_ge(nums, target)

        if left_bound == len(nums) or nums[left_bound] != target:
            return [-1, -1]

        right_bound = self.find_last_le(nums, target)
        return [left_bound, right_bound]

    def find_first_ge(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left

    def find_last_le(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1

        return right


if __name__ == "__main__":
    solution = Solution()

    assert solution.searchRange([5, 7, 7, 8, 8, 10], 8) == [3, 4]
    assert solution.searchRange([5, 7, 7, 8, 8, 10], 6) == [-1, -1]
    assert solution.searchRange([], 0) == [-1, -1]
    assert solution.searchRange([1], 1) == [0, 0]
    assert solution.searchRange([2, 2], 2) == [0, 1]
    assert solution.searchRange([1, 2, 3, 3, 3, 4], 3) == [2, 4]
    assert solution.searchRange([1, 1, 1], 1) == [0, 2]

    print("all tests passed")
