class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        最优解法：滑动窗口 + 哈希表记录字符上次出现位置
        时间复杂度: O(n)
        空间复杂度: O(min(n, m))
        """
        last_index = {}
        left = 0
        res = 0

        for right, ch in enumerate(s):
            if ch in last_index:
                left = max(left, last_index[ch] + 1)

            last_index[ch] = right
            res = max(res, right - left + 1)

        return res


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
