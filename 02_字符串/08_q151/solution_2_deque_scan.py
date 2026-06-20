# 方法2：双端队列扫描（面试主推）
from collections import deque


class Solution:
    def reverseWords(self, s: str) -> str:
        left = 0
        right = len(s) - 1

        while left <= right and s[left] == " ":
            left += 1

        while left <= right and s[right] == " ":
            right -= 1

        dq = deque()
        word = []

        while left <= right:
            if s[left] == " ":
                if word:
                    dq.appendleft("".join(word))
                    word = []
            else:
                word.append(s[left])

            left += 1

        if word:
            dq.appendleft("".join(word))

        return " ".join(dq)


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
