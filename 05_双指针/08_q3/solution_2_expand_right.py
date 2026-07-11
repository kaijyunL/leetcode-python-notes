# 方法2：固定起点，向右扩展到重复为止

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0

        for left in range(n):
            seen = set()

            for right in range(left, n):
                if s[right] in seen:
                    break

                seen.add(s[right])
                ans = max(ans, right - left + 1)

        return ans


if __name__ == "__main__":
    solution = Solution()

    assert solution.lengthOfLongestSubstring("abcabcbb") == 3
    assert solution.lengthOfLongestSubstring("bbbbb") == 1
    assert solution.lengthOfLongestSubstring("pwwkew") == 3
    assert solution.lengthOfLongestSubstring("") == 0
    assert solution.lengthOfLongestSubstring("abba") == 2
    assert solution.lengthOfLongestSubstring("dvdf") == 3

    print("all tests passed")
