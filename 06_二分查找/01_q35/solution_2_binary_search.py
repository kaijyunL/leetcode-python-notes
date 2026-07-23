# 方法2：二分查找（面试主推）


class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left


if __name__ == "__main__":
    solution = Solution()

    assert solution.searchInsert([1, 3, 5, 6], 5) == 2
    assert solution.searchInsert([1, 3, 5, 6], 2) == 1
    assert solution.searchInsert([1, 3, 5, 6], 7) == 4
    assert solution.searchInsert([1, 3, 5, 6], 0) == 0
    assert solution.searchInsert([], 3) == 0

    print("all tests passed")
