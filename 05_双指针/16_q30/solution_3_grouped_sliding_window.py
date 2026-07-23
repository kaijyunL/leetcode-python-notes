# 方法3：按单词长度分组滑动窗口（面试主推）

from collections import Counter, defaultdict


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
                    ans.append(left)
                    left_word = s[left:left + word_len]
                    window[left_word] -= 1
                    count -= 1
                    left += word_len

        return sorted(ans)


if __name__ == "__main__":
    solution = Solution()

    assert solution.findSubstring("barfoothefoobarman", ["foo", "bar"]) == [0, 9]
    assert solution.findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "word"]) == []
    assert solution.findSubstring("barfoofoobarthefoobarman", ["bar", "foo", "the"]) == [6, 9, 12]
    assert solution.findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "good"]) == [8]
    assert solution.findSubstring("", ["foo", "bar"]) == []

    print("all tests passed")
