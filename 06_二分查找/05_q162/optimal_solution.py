class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        """
        最优解法：根据坡度二分
        时间复杂度: O(log n)
        空间复杂度: O(1)
        """
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid

        return left


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        [1, 2, 3, 1],
        [1, 2, 1, 3, 5, 6, 4],
        [1],
        [2, 1],
        [1, 2],
    ]

    for nums in test_cases:
        print(f"nums = {nums}, result = {solution.findPeakElement(nums)}")
