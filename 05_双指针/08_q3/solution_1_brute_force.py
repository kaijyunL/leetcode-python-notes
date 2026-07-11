# 方法1：暴力枚举所有子串

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0

        for left in range(n):
            for right in range(left, n):
                if self._has_no_repeat(s, left, right):
                    ans = max(ans, right - left + 1)

        return ans

    def _has_no_repeat(self, s: str, left: int, right: int) -> bool:
        seen = set()

        for i in range(left, right + 1):
            if s[i] in seen:
                return False
            seen.add(s[i])

        return True


if __name__ == "__main__":
    solution = Solution()

    assert solution.lengthOfLongestSubstring("abcabcbb") == 3
    assert solution.lengthOfLongestSubstring("bbbbb") == 1
    assert solution.lengthOfLongestSubstring("pwwkew") == 3
    assert solution.lengthOfLongestSubstring("") == 0
    assert solution.lengthOfLongestSubstring("abba") == 2
    assert solution.lengthOfLongestSubstring("dvdf") == 3

    print("all tests passed")
