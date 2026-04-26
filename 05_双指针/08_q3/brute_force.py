class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        暴力解法：枚举所有子串，再判断是否有重复字符
        时间复杂度: O(n^3)
        空间复杂度: O(min(n, m))
        """
        n = len(s)
        res = 0

        for left in range(n):
            for right in range(left, n):
                if self._has_no_repeat(s, left, right):
                    res = max(res, right - left + 1)

        return res

    def _has_no_repeat(self, s: str, left: int, right: int) -> bool:
        seen = set()

        for i in range(left, right + 1):
            if s[i] in seen:
                return False
            seen.add(s[i])

        return True


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        "abcabcbb",
        "bbbbb",
        "pwwkew",
        "",
        "abba",
    ]

    for s in test_cases:
        print(f's = "{s}", result = {solution.lengthOfLongestSubstring(s)}')
