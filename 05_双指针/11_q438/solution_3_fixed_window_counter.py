# 方法3：固定窗口 + Counter

from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        n = len(s)
        m = len(p)
        ans = []

        if n < m:
            return ans

        target_count = Counter(p)
        window_count = Counter(s[:m])

        if window_count == target_count:
            ans.append(0)

        for right in range(m, n):
            left = right - m

            window_count[s[left]] -= 1
            if window_count[s[left]] == 0:
                del window_count[s[left]]

            window_count[s[right]] += 1

            if window_count == target_count:
                ans.append(left + 1)

        return ans


if __name__ == "__main__":
    solution = Solution()

    assert solution.findAnagrams("cbaebabacd", "abc") == [0, 6]
    assert solution.findAnagrams("abab", "ab") == [0, 1, 2]
    assert solution.findAnagrams("baa", "aa") == [1]
    assert solution.findAnagrams("", "a") == []
    assert solution.findAnagrams("aaaaaaaaaa", "aaaaaaaaaaaaa") == []

    print("all tests passed")
