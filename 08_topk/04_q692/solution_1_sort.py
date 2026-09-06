from collections import Counter


class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        """
        方法1：哈希表 + 双关键字排序（面试首选）
        时间复杂度：O(n + m log m)
        空间复杂度：O(m)
        """
        freq = Counter(words)
        ordered_words = sorted(freq, key=lambda word: (-freq[word], word))
        return ordered_words[:k]


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
