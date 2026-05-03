import heapq
from collections import Counter


class ReverseWord:
    def __init__(self, word: str):
        self.word = word

    def __lt__(self, other: "ReverseWord") -> bool:
        return self.word > other.word


class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        """
        解法2：哈希表 + 堆 — 面试推荐
        时间复杂度: O(n + m log k + k log k), m 是不同单词数
        空间复杂度: O(m + k)
        """
        count = Counter(words)
        heap = []

        for word, frq in count.items():
            # 堆的比较规则: (频率, 字典序倒序)
            # 频率小的弹出；频率相同时，字典序大的弹出
            heapq.heappush(heap, (count, ReverseWord(word), word))
            if len(heap) > k:
                heapq.heappop(heap)

        return [word for frq, _, word in sorted(heap, key=lambda item: (-item[0], item[2]))]


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        (["i", "love", "leetcode", "i", "love", "coding"], 2),
        (["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4),
        (["a"], 1),
        (["a", "b", "c"], 2),
    ]

    for words, k in test_cases:
        print(f"输入: {words}, k={k}, 输出: {solution.topKFrequent(words, k)}")
