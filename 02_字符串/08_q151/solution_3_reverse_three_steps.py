# 方法3：三步翻转
class Solution:
    def reverseWords(self, s: str) -> str:
        chars = self.trim_spaces(s)
        self.reverse_range(chars, 0, len(chars) - 1)
        self.reverse_each_word(chars)
        return "".join(chars)

    def trim_spaces(self, s: str) -> list[str]:
        chars = []
        i = 0
        n = len(s)

        while i < n:
            while i < n and s[i] == " ":
                i += 1

            if i >= n:
                break

            if chars:
                chars.append(" ")

            while i < n and s[i] != " ":
                chars.append(s[i])
                i += 1

        return chars

    def reverse_range(self, chars: list[str], left: int, right: int) -> None:
        while left < right:
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1

    def reverse_each_word(self, chars: list[str]) -> None:
        n = len(chars)
        start = 0

        while start < n:
            end = start
            while end < n and chars[end] != " ":
                end += 1

            self.reverse_range(chars, start, end - 1)
            start = end + 1


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
