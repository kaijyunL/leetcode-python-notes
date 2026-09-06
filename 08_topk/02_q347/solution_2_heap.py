import heapq
from collections import Counter


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        """
        方法2：哈希表 + 大小为 k 的最小堆（Top K 通用解）
        时间复杂度：O(n + m log k)
        空间复杂度：O(m + k)
        """
        freq = Counter(nums)
        heap = []

        for num, count in freq.items():
            if len(heap) < k:
                heapq.heappush(heap, (count, num))
            elif count > heap[0][0]:
                heapq.heapreplace(heap, (count, num))

        return [num for _, num in heap]


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
