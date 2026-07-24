# 方法2：二分查找（面试主推）


class Solution:
    def findMin(self, nums: list[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]


if __name__ == "__main__":
    solution = Solution()

    assert solution.findMin([3, 4, 5, 1, 2]) == 1
    assert solution.findMin([4, 5, 6, 7, 0, 1, 2]) == 0
    assert solution.findMin([11, 13, 15, 17]) == 11
    assert solution.findMin([1]) == 1
    assert solution.findMin([2, 1]) == 1
    assert solution.findMin([5, 1, 2, 3, 4]) == 1
    assert solution.findMin([2, 3, 4, 5, 1]) == 1

    print("all tests passed")
