# 方法2：二分查找（面试主推）


class Solution:
    def findMin(self, nums: list[int]) -> int:
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

    assert solution.findMin([1, 3, 5]) == 1
    assert solution.findMin([2, 2, 2, 0, 1]) == 0
    assert solution.findMin([2, 2, 2, 0, 1, 2]) == 0
    assert solution.findMin([10, 1, 10, 10, 10]) == 1
    assert solution.findMin([1, 1, 1, 1]) == 1
    assert solution.findMin([1]) == 1
    assert solution.findMin([3, 3, 1, 3]) == 1
    assert solution.findMin([4, 5, 6, 7, 0, 1, 4]) == 0

    print("all tests passed")
