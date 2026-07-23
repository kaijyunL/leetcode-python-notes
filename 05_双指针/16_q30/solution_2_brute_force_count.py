# 方法2：切分后比较词频

from collections import Counter


class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        if not s or not words:
            return []

        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count
        ans = []

        if len(s) < total_len:
            return ans

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
                ans.append(start)

        return ans


if __name__ == "__main__":
    solution = Solution()

    assert solution.findSubstring("barfoothefoobarman", ["foo", "bar"]) == [0, 9]
    assert solution.findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "word"]) == []
    assert solution.findSubstring("barfoofoobarthefoobarman", ["bar", "foo", "the"]) == [6, 9, 12]
    assert solution.findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "good"]) == [8]
    assert solution.findSubstring("", ["foo", "bar"]) == []

    print("all tests passed")
