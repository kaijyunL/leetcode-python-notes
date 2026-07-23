# 方法2：固定窗口，重新计数比较


class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        n = len(s)
        m = len(p)
        ans = []

        if n < m:
            return ans

        target_count = self._build_count(p)

        for left in range(n - m + 1):
            if self._build_count(s[left:left + m]) == target_count:
                ans.append(left)

        return ans

    def _build_count(self, text: str) -> list[int]:
        count = [0] * 26

        for ch in text:
            count[ord(ch) - ord("a")] += 1

        return count


if __name__ == "__main__":
    solution = Solution()

    assert solution.findAnagrams("cbaebabacd", "abc") == [0, 6]
    assert solution.findAnagrams("abab", "ab") == [0, 1, 2]
    assert solution.findAnagrams("baa", "aa") == [1]
    assert solution.findAnagrams("", "a") == []
    assert solution.findAnagrams("aaaaaaaaaa", "aaaaaaaaaaaaa") == []

    print("all tests passed")
