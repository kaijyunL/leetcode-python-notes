# 方法1：split() 后翻转
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        return " ".join(reversed(words))


def run_case(s: str, expected: str) -> None:
    actual = Solution().reverseWords(s)
    assert actual == expected


if __name__ == "__main__":
    run_case("the sky is blue", "blue is sky the")
    run_case("  hello world  ", "world hello")
    run_case("a good   example", "example good a")
    run_case("one", "one")
    run_case("  Bob    Loves  Alice   ", "Alice Loves Bob")

    print("all tests passed")
