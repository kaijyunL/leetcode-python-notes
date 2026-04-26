class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        改进解法：固定起点，向右扩展，遇到重复就停止
        时间复杂度: O(n^2)
        空间复杂度: O(min(n, m))
        """
        n = len(s)
        res = 0

        for left in range(n):
            seen = set()

            for right in range(left, n):
                if s[right] in seen:
                    break

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
