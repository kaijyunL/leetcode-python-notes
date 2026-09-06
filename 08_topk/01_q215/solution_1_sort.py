class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        """
        方法1：排序后取值（基线解法）
        时间复杂度：O(n log n)
        空间复杂度：取决于排序实现
        """
        nums.sort()
        return nums[-k]


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([3, 2, 1, 5, 6, 4], 2, 5),
        ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4),
        ([1], 1, 1),
        ([7, 9, 2, 8, 1], 3, 7),
        ([5, 5, 5], 2, 5),
    ]

    for nums, k, expected in test_cases:
        assert solution.findKthLargest(nums, k) == expected

    print("all tests passed")
