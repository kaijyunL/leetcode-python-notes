# 方法2：哈希计数（面试主推）
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counts = {}
        for ch in s:
            counts[ch] = counts.get(ch, 0) + 1

        for ch in t:
            if ch not in counts:
                return False

            counts[ch] -= 1
            if counts[ch] < 0:
                return False

        return True


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
