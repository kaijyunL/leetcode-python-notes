# 方法1：线性扫描


class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return i

        return len(nums) - 1


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
