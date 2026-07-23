# 方法2：固定窗口，重新计数比较


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m = len(s1)
        n = len(s2)

        if n < m:
            return False

        target_count = self._build_count(s1)

        for left in range(n - m + 1):
            if self._build_count(s2[left:left + m]) == target_count:
                return True

        return False

    def _build_count(self, s: str) -> list[int]:
        count = [0] * 26

        for ch in s:
            count[ord(ch) - ord("a")] += 1

        return count


if __name__ == "__main__":
    solution = Solution()

    assert solution.checkInclusion("ab", "eidbaooo") is True
    assert solution.checkInclusion("ab", "eidboaoo") is False
    assert solution.checkInclusion("adc", "dcda") is True
    assert solution.checkInclusion("hello", "ooolleoooleh") is False
    assert solution.checkInclusion("a", "") is False

    print("all tests passed")
