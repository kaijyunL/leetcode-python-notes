# 方法1：排序后比较
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)


def run_case(s: str, t: str, expected: bool) -> None:
    actual = Solution().isAnagram(s, t)
    assert actual == expected


if __name__ == "__main__":
    run_case("anagram", "nagaram", True)
    run_case("rat", "car", False)
    run_case("aacc", "ccac", False)
    run_case("", "", True)
    run_case("ab", "a", False)

    print("all tests passed")
