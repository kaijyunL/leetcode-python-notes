# 方法4：滑动窗口 + 上次出现位置

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_index = {}
        left = 0
        ans = 0

        for right, ch in enumerate(s):
            if ch in last_index:
                # left 不能回退，只能跳到当前窗口内上次重复位置的下一位。
                left = max(left, last_index[ch] + 1)

            last_index[ch] = right
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
