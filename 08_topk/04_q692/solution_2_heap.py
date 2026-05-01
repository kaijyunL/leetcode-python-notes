import heapq
from collections import Counter


class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        """
        解法2：哈希表 + 堆 — 面试推荐
        时间复杂度: O(n log k)
        空间复杂度: O(n + k)
        """
        freq = Counter(words)
        heap = []

        for word, count in freq.items():
            # 堆的比较规则: (频率, 字典序倒序)
            # 频率小的弹出；频率相同时，字典序大的弹出
            heapq.heappush(heap, (count, word))
            if len(heap) > k:
                heapq.heappop(heap)

        return [w for _, w in sorted(heap, reverse=True)]


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        (["i", "love", "leetcode", "i", "love", "coding"], 2),
        (["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4),
        (["a"], 1),
    ]

    for words, k in test_cases:
        print(f"输入: {words}, k={k}, 输出: {solution.topKFrequent(words, k)}")
