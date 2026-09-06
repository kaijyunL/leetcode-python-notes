from collections import Counter


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        """
        方法1：哈希表 + 按频率排序（基线解法）
        时间复杂度：O(n + m log m)
        空间复杂度：O(m)
        """
        freq = Counter(nums)
        items = sorted(freq.items(), key=lambda item: item[1], reverse=True)
        return [num for num, _ in items[:k]]


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([1, 1, 1, 2, 2, 3], 2, {1, 2}),
        ([1], 1, {1}),
        ([4, 1, -1, 2, -1, 2, 3], 2, {-1, 2}),
        ([3, 3, 3, 3, 2, 2, 1], 3, {1, 2, 3}),
    ]

    for nums, k, expected in test_cases:
        assert set(solution.topKFrequent(nums, k)) == expected

    print("all tests passed")
