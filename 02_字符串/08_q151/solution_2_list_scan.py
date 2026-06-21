# 方法2：手动扫描 + 列表反转（面试主推）


class Solution:
    def reverseWords(self, s: str) -> str:
        left = 0
        right = len(s) - 1

        while left <= right and s[left] == " ":
            left += 1

        while left <= right and s[right] == " ":
            right -= 1

        word = []
        ans = []

        while left <= right:
            if s[left] == " ":
                if word:
                    ans.append("".join(word))
                    word = []
            else:
                word.append(s[left])

            left += 1

        if word:
            ans.append("".join(word))

        return " ".join(reversed(ans))


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
