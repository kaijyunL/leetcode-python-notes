# 方法3：滑动窗口维护覆盖关系（面试主推）

from collections import Counter, defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        need = Counter(t)
        window = defaultdict(int)
        left = 0
        valid = 0
        start = 0
        min_len = float("inf")

        for right, ch in enumerate(s):
            if ch in need:
                window[ch] += 1
                if window[ch] == need[ch]:
                    valid += 1

            while valid == len(need):
                cur_len = right - left + 1
                if cur_len < min_len:
                    min_len = cur_len
                    start = left

                left_char = s[left]
                if left_char in need:
                    if window[left_char] == need[left_char]:
                        valid -= 1
                    window[left_char] -= 1

                left += 1

        if min_len == float("inf"):
            return ""
        return s[start:start + min_len]


if __name__ == "__main__":
    solution = Solution()

    assert solution.minWindow("ADOBECODEBANC", "ABC") == "BANC"
    assert solution.minWindow("a", "a") == "a"
    assert solution.minWindow("a", "aa") == ""
    assert solution.minWindow("aa", "aa") == "aa"
    assert solution.minWindow("ab", "b") == "b"
    assert solution.minWindow("bba", "ab") == "ba"

    print("all tests passed")
