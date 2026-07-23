# 方法1：枚举所有子串并检查覆盖

from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        ans = ""

        for left in range(len(s)):
            for right in range(left, len(s)):
                window = Counter(s[left:right + 1])
                if self._covers(window, need):
                    cur = s[left:right + 1]
                    if not ans or len(cur) < len(ans):
                        ans = cur

        return ans

    def _covers(self, window: Counter, need: Counter) -> bool:
        for ch, count in need.items():
            if window[ch] < count:
                return False
        return True


if __name__ == "__main__":
    solution = Solution()

    assert solution.minWindow("ADOBECODEBANC", "ABC") == "BANC"
    assert solution.minWindow("a", "a") == "a"
    assert solution.minWindow("a", "aa") == ""
    assert solution.minWindow("aa", "aa") == "aa"
    assert solution.minWindow("ab", "b") == "b"
    assert solution.minWindow("bba", "ab") == "ba"

    print("all tests passed")
