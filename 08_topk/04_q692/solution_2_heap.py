import heapq
from collections import Counter


class ReverseWord:
    """让字典序更大的单词在最小堆中更靠近堆顶。"""

    def __init__(self, word: str):
        self.word = word

    def __lt__(self, other: "ReverseWord") -> bool:
        return self.word > other.word


class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        """
        方法2：哈希表 + 大小为 k 的最小堆（Top K 进阶解）
        时间复杂度：O(n + m log k + k log k)
        空间复杂度：O(m + k)
        """
        freq = Counter(words)
        heap = []

        for word, count in freq.items():
            heapq.heappush(heap, (count, ReverseWord(word)))
            if len(heap) > k:
                heapq.heappop(heap)

        return [
            reverse_word.word
            for _, reverse_word in sorted(heap, key=lambda item: (-item[0], item[1].word))
        ]


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        (["i", "love", "leetcode", "i", "love", "coding"], 2, ["i", "love"]),
        (["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4, ["the", "is", "sunny", "day"]),
        (["a"], 1, ["a"]),
        (["a", "b", "c"], 2, ["a", "b"]),
    ]

    for words, k, expected in test_cases:
        assert solution.topKFrequent(words, k) == expected

    print("all tests passed")
