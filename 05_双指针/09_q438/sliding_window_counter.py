from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        """
        滑动窗口：维护长度为 len(p) 的窗口计数
        时间复杂度: O(n)
        空间复杂度: O(1)
        """
        n = len(s)
        m = len(p)
        res = []

        if n < m:
            return res

        p_count = Counter(p)
        s_count = Counter(s[:m])

        if s_count == p_count:
            res.append(0)

        for right in range(m, n):
            left = right - m

            s_count[s[left]] -= 1
            if s_count[s[left]] == 0:
                del s_count[s[left]]

            s_count[s[right]] += 1

            if s_count == p_count:
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
