from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        """
        暴力解法：枚举每个窗口，重新统计字符频次
        时间复杂度: O(n * m)
        空间复杂度: O(m)
        """
        n = len(s)
        m = len(p)
        res = []

        if n < m:
            return res

        p_count = Counter(p)

        for i in range(n - m + 1):
            if Counter(s[i:i + m]) == p_count:
                res.append(i)

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
