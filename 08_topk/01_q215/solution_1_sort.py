class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        """
        解法1：排序后取值
        时间复杂度: O(n log n)
        空间复杂度: O(1)
        """
        return sorted(nums)[-k]


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([3, 2, 1, 5, 6, 4], 2),
        ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4),
        ([1], 1),
        ([7, 9, 2, 8, 1], 3),
    ]

    for nums, k in test_cases:
        print(f"输入: {nums}, k={k}, 输出: {solution.findKthLargest(nums, k)}")
