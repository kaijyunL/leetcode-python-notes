# 方法3：固定窗口 + 26 位计数数组（面试主推）


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m = len(s1)
        n = len(s2)

        if n < m:
            return False

        target_count = [0] * 26
        window_count = [0] * 26

        for i in range(m):
            target_count[ord(s1[i]) - ord("a")] += 1
            window_count[ord(s2[i]) - ord("a")] += 1

        if window_count == target_count:
            return True

        for right in range(m, n):
            left = right - m
            window_count[ord(s2[left]) - ord("a")] -= 1
            window_count[ord(s2[right]) - ord("a")] += 1

            if window_count == target_count:
                return True

        return False


if __name__ == "__main__":
    solution = Solution()

    assert solution.checkInclusion("ab", "eidbaooo") is True
    assert solution.checkInclusion("ab", "eidboaoo") is False
    assert solution.checkInclusion("adc", "dcda") is True
    assert solution.checkInclusion("hello", "ooolleoooleh") is False
    assert solution.checkInclusion("a", "") is False

    print("all tests passed")
