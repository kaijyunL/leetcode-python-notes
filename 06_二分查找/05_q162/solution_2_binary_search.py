# 方法2：二分查找（面试主推）


class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid

        return left


def is_peak(nums: list[int], index: int) -> bool:
    left = nums[index - 1] if index > 0 else float("-inf")
    right = nums[index + 1] if index < len(nums) - 1 else float("-inf")
    return nums[index] > left and nums[index] > right


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        [1, 2, 3, 1],
        [1, 2, 1, 3, 5, 6, 4],
        [1],
        [2, 1],
        [1, 2],
        [1, 3, 2, 1],
    ]

    for nums in test_cases:
        ans = solution.findPeakElement(nums)
        assert is_peak(nums, ans)

    print("all tests passed")
