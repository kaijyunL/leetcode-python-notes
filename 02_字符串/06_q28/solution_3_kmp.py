# 方法3：KMP（最优解）
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0

        lps = self.build_lps(needle)
        j = 0

        for i, ch in enumerate(haystack):
            while j > 0 and ch != needle[j]:
                j = lps[j - 1]

            if ch == needle[j]:
                j += 1

            if j == len(needle):
                return i - len(needle) + 1

        return -1

    def build_lps(self, pattern: str) -> list[int]:
        lps = [0] * len(pattern)
        length = 0

        for i in range(1, len(pattern)):
            while length > 0 and pattern[i] != pattern[length]:
                length = lps[length - 1]

            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length

        return lps


def run_case(haystack: str, needle: str, expected: int) -> None:
    actual = Solution().strStr(haystack, needle)
    assert actual == expected


if __name__ == "__main__":
    run_case("sadbutsad", "sad", 0)
    run_case("leetcode", "leeto", -1)
    run_case("hello", "ll", 2)
    run_case("aabaabaafa", "aabaaf", 3)
    run_case("abc", "", 0)
    run_case("a", "a", 0)

    print("all tests passed")
