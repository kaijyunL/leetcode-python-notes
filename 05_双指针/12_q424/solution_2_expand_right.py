# 方法2：固定起点，向右扩展并维护频次


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        ans = 0

        for left in range(n):
            count = [0] * 26
            max_freq = 0

            for right in range(left, n):
                idx = ord(s[right]) - ord("A")
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
