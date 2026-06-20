# 方法3：定长 26 数组计数
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counts = [0] * 26

        for ch in s:
            counts[ord(ch) - ord("a")] += 1

        for ch in t:
            counts[ord(ch) - ord("a")] -= 1

        return all(count == 0 for count in counts)


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
