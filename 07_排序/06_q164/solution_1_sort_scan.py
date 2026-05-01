class Solution:
    def maximumGap(self, nums: list[int]) -> int:
        """
        解法1：排序后扫描
        时间复杂度: O(n log n)
        空间复杂度: O(1)
        """
        if len(nums) < 2:
            return 0

        nums.sort()

        max_gap = 0
        for i in range(1, len(nums)):
            max_gap = max(max_gap, nums[i] - nums[i - 1])

        return max_gap


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        [3, 6, 9, 1],
        [10],
        [1, 1, 1, 1],
        [1, 10000000],
        [],
    ]

    for nums in test_cases:
        print(f"输入: {nums}, 输出: {solution.maximumGap(nums)}")
