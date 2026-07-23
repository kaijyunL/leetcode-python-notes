# 方法1：固定窗口，排序比较


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m = len(s1)
        n = len(s2)

        if n < m:
            return False

        sorted_s1 = sorted(s1)

        for left in range(n - m + 1):
            if sorted(s2[left:left + m]) == sorted_s1:
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
