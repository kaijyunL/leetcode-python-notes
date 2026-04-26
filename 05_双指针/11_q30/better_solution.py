from collections import Counter


class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        """
        改进解法：枚举起点，切分单词后比较词频
        时间复杂度: O(n * k)
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

        for start in range(len(s) - total_len + 1):
            seen = Counter()

            for i in range(word_count):
                left = start + i * word_len
                word = s[left:left + word_len]

                if word not in need:
                    break

                seen[word] += 1
                if seen[word] > need[word]:
                    break
            else:
                res.append(start)

        return res


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ("barfoothefoobarman", ["foo", "bar"]),
        ("wordgoodgoodgoodbestword", ["word", "good", "best", "word"]),
        ("barfoofoobarthefoobarman", ["bar", "foo", "the"]),
    ]

    for s, words in test_cases:
        print(f's = "{s}", words = {words}, result = {solution.findSubstring(s, words)}')
