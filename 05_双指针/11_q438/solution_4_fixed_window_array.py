# 方法4：固定窗口 + 26 位计数数组（面试主推）


class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        n = len(s)
        m = len(p)
        ans = []

        if n < m:
            return ans

        target_count = [0] * 26
        window_count = [0] * 26

        for i in range(m):
            target_count[ord(p[i]) - ord("a")] += 1
            window_count[ord(s[i]) - ord("a")] += 1

        if window_count == target_count:
            ans.append(0)

        for right in range(m, n):
            left = right - m
            window_count[ord(s[left]) - ord("a")] -= 1
            window_count[ord(s[right]) - ord("a")] += 1

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
