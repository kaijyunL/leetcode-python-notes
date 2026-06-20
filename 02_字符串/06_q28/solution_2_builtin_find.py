# 方法2：内置 find()
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


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
