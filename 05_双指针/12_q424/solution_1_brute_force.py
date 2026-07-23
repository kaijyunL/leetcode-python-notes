# 方法1：暴力枚举所有子串并重新统计频次


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        ans = 0

        for left in range(n):
            for right in range(left, n):
                count = [0] * 26
                max_freq = 0

                for i in range(left, right + 1):
                    idx = ord(s[i]) - ord("A")
                    count[idx] += 1
                    max_freq = max(max_freq, count[idx])

                window_len = right - left + 1
                if window_len - max_freq <= k:
                    ans = max(ans, window_len)

        return ans


if __name__ == "__main__":
    solution = Solution()

    assert solution.characterReplacement("ABAB", 2) == 4
    assert solution.characterReplacement("AABABBA", 1) == 4
    assert solution.characterReplacement("AAAA", 2) == 4
    assert solution.characterReplacement("ABCDE", 1) == 2
    assert solution.characterReplacement("", 3) == 0

    print("all tests passed")
