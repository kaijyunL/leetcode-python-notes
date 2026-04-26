from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        暴力解法：枚举所有子串，检查是否覆盖 t
        时间复杂度: O(n^3)
        空间复杂度: O(m)
        """
        need = Counter(t)
        res = ""

        for left in range(len(s)):
            for right in range(left, len(s)):
                window = Counter(s[left:right + 1])
                if self._covers(window, need):
                    cur = s[left:right + 1]
                    if not res or len(cur) < len(res):
                        res = cur

        return res

    def _covers(self, window: Counter, need: Counter) -> bool:
        for ch, count in need.items():
            if window[ch] < count:
                return False
        return True


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ("ADOBECODEBANC", "ABC"),
        ("a", "a"),
        ("a", "aa"),
        ("aa", "aa"),
    ]

    for s, t in test_cases:
        print(f's = "{s}", t = "{t}", result = "{solution.minWindow(s, t)}"')
