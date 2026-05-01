from collections import Counter


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        """
        解法1：哈希表 + 排序
        时间复杂度: O(n log n)
        空间复杂度: O(n)
        """
        return [x for x, _ in Counter(nums).most_common(k)]


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([1, 1, 1, 2, 2, 3], 2),
        ([1], 1),
        ([4, 1, -1, 2, -1, 2, 3], 2),
        ([3, 3, 3, 3, 2, 2, 1], 2),
    ]

    for nums, k in test_cases:
        print(f"输入: {nums}, k={k}, 输出: {solution.topKFrequent(nums, k)}")
