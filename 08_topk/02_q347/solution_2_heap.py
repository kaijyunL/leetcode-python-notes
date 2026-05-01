import heapq
from collections import Counter


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        """
        解法2：哈希表 + 最小堆
        时间复杂度: O(n log k)
        空间复杂度: O(n + k)
        """
        freq = Counter(nums)
        heap = []

        for num, count in freq.items():
            heapq.heappush(heap, (count, num))
            if len(heap) > k:
                heapq.heappop(heap)

        return [num for _, num in heap]


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
