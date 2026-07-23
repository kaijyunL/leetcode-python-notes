# 方法3：滑动窗口维护合法性（面试主推）


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26
        left = 0
        max_freq = 0
        ans = 0

        for right, ch in enumerate(s):
            idx = ord(ch) - ord("A")
            count[idx] += 1
            max_freq = max(max_freq, count[idx])

            while right - left + 1 - max_freq > k:
                count[ord(s[left]) - ord("A")] -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans


if __name__ == "__main__":
    solution = Solution()

    assert solution.characterReplacement("ABAB", 2) == 4
    assert solution.characterReplacement("AABABBA", 1) == 4
    assert solution.characterReplacement("AAAA", 2) == 4
    assert solution.characterReplacement("ABCDE", 1) == 2
    assert solution.characterReplacement("", 3) == 0

    print("all tests passed")
