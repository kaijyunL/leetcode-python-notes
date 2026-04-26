class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        最优解法：滑动窗口 + 哈希集合
        时间复杂度: O(n)
        空间复杂度: O(min(n, m))
        """
        seen = set()
        left = 0
        res = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])
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
