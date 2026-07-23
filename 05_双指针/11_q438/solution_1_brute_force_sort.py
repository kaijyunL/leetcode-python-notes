# 方法1：固定窗口，排序比较


class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        n = len(s)
        m = len(p)
        ans = []

        if n < m:
            return ans

        sorted_p = sorted(p)

        for left in range(n - m + 1):
            if sorted(s[left:left + m]) == sorted_p:
                ans.append(left)

        return ans


if __name__ == "__main__":
    solution = Solution()

    assert solution.findAnagrams("cbaebabacd", "abc") == [0, 6]
    assert solution.findAnagrams("abab", "ab") == [0, 1, 2]
    assert solution.findAnagrams("baa", "aa") == [1]
    assert solution.findAnagrams("", "a") == []
    assert solution.findAnagrams("aaaaaaaaaa", "aaaaaaaaaaaaa") == []

    print("all tests passed")
