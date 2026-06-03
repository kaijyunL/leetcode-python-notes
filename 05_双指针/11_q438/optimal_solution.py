class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        """
        最优解法：固定长度滑动窗口 + 26 位数组计数
        时间复杂度: O(n)
        空间复杂度: O(1)
        """
        n = len(s)
        m = len(p)
        res = []

        if n < m:
            return res

        p_count = [0] * 26
        window_count = [0] * 26

        for i in range(m):
            p_count[ord(p[i]) - ord("a")] += 1
            window_count[ord(s[i]) - ord("a")] += 1

        if window_count == p_count:
            res.append(0)

        for right in range(m, n):
            left = right - m
            window_count[ord(s[left]) - ord("a")] -= 1
            window_count[ord(s[right]) - ord("a")] += 1

            if window_count == p_count:
                res.append(left + 1)

        return res


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ("cbaebabacd", "abc"),
        ("abab", "ab"),
        ("baa", "aa"),
        ("", "a"),
    ]

    for s, p in test_cases:
        print(f's = "{s}", p = "{p}", result = {solution.findAnagrams(s, p)}')
