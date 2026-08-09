class Solution:
    def maximumGap(self, nums: list[int]) -> int:
        """
        方法1：排序后扫描
        时间复杂度：O(n log n)
        空间复杂度：取决于排序实现
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

    assert solution.maximumGap([3, 6, 9, 1]) == 3
    assert solution.maximumGap([10]) == 0
    assert solution.maximumGap([1, 1, 1, 1]) == 0
    assert solution.maximumGap([1, 10_000_000]) == 9_999_999
    assert solution.maximumGap([]) == 0

    print("all tests passed")
