# 方法2：固定左端点，向右扩展到第一次覆盖

from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        ans = ""

        for left in range(len(s)):
            window = Counter()

            for right in range(left, len(s)):
                window[s[right]] += 1

                if self._covers(window, need):
                    cur = s[left:right + 1]
                    if not ans or len(cur) < len(ans):
                        ans = cur
                    break

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
