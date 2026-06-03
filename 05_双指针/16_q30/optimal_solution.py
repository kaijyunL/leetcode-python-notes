from collections import Counter, defaultdict


class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        """
        最优解法：按单词长度分组滑动窗口
        时间复杂度: O(n)
        空间复杂度: O(k)
        """
        if not s or not words:
            return []

        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count
        res = []

        if len(s) < total_len:
            return res

        need = Counter(words)

        for offset in range(word_len):
            left = offset
            count = 0
            window = defaultdict(int)

            for right in range(offset, len(s) - word_len + 1, word_len):
                word = s[right:right + word_len]

                if word not in need:
                    window.clear()
                    count = 0
                    left = right + word_len
                    continue

                window[word] += 1
                count += 1

                while window[word] > need[word]:
                    left_word = s[left:left + word_len]
                    window[left_word] -= 1
                    count -= 1
                    left += word_len

                if count == word_count:
                    res.append(left)
                    left_word = s[left:left + word_len]
                    window[left_word] -= 1
                    count -= 1
                    left += word_len

        return sorted(res)


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ("barfoothefoobarman", ["foo", "bar"]),
        ("wordgoodgoodgoodbestword", ["word", "good", "best", "word"]),
        ("barfoofoobarthefoobarman", ["bar", "foo", "the"]),
        ("wordgoodgoodgoodbestword", ["word", "good", "best", "good"]),
    ]

    for s, words in test_cases:
        print(f's = "{s}", words = {words}, result = {solution.findSubstring(s, words)}')
