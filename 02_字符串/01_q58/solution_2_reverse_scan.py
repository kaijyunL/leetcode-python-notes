# 方法2：从后往前扫描（面试主推）
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1

        while i >= 0 and s[i] == " ":
            i -= 1

        length = 0
        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1

        return length


def run_case(s: str, expected: int) -> None:
    actual = Solution().lengthOfLastWord(s)
    assert actual == expected


if __name__ == "__main__":
    run_case("Hello World", 5)
    run_case("   fly me   to   the moon  ", 4)
    run_case("luffy is still joyboy", 6)
    run_case(" ", 0)
    run_case("a", 1)

    print("all tests passed")
