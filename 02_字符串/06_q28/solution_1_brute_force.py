# 方法1：暴力匹配（面试主推）
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(haystack)
        n = len(needle)

        if not needle:
            return 0

        for i in range(m - n + 1):
            if haystack[i : i + n] == needle:
                return i

        return -1


def run_case(haystack: str, needle: str, expected: int) -> None:
    actual = Solution().strStr(haystack, needle)
    assert actual == expected


if __name__ == "__main__":
    run_case("sadbutsad", "sad", 0)
    run_case("leetcode", "leeto", -1)
    run_case("hello", "ll", 2)
    run_case("aaaaa", "bba", -1)
    run_case("abc", "", 0)
    run_case("a", "a", 0)

    print("all tests passed")
