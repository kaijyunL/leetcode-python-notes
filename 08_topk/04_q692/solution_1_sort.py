from collections import Counter


class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        """
        解法1：哈希表 + 排序
        时间复杂度: O(n log n)
        空间复杂度: O(n)
        """
        freq = Counter(words)
        return sorted(freq.keys(), key=lambda w: (-freq[w], w))[:k]


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        (["i", "love", "leetcode", "i", "love", "coding"], 2),
        (["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4),
        (["a"], 1),
    ]

    for words, k in test_cases:
        print(f"输入: {words}, k={k}, 输出: {solution.topKFrequent(words, k)}")
